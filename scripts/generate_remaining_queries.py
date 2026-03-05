import csv, os, re

SCHEMA_DIR = '/Users/mattcomroe/tormentnexus/docs/schema'
ENTITY_MAP = '/Users/mattcomroe/tormentnexus/Entity_Mapping - Sheet1.csv'

# Find tables with column data in docs
tables_with_cols = set()
for fname in os.listdir(SCHEMA_DIR):
    with open(f'{SCHEMA_DIR}/{fname}') as f:
        current_physical = None
        for line in f:
            m = re.match(r'\*\*Physical table:\*\* `(.+)`', line.strip())
            if m:
                current_physical = m.group(1).upper()
            if current_physical and line.startswith('| ') and 'Column' not in line and '---' not in line:
                tables_with_cols.add(current_physical)

entities = {}
with open(ENTITY_MAP) as f:
    for r in csv.DictReader(f):
        if r['IS_ACTIVE'] == '1' and r['IS_SYSTEM'] == '0':
            entities[r['PHYSICAL_TABLE_NAME'].upper()] = r['PHYSICAL_TABLE_NAME']

missing = [orig for upper, orig in entities.items() if upper not in tables_with_cols]

plain       = sorted([t for t in missing if '[' not in t])
oslogdb     = sorted([t.split('.')[-1].strip('[]') for t in missing if '[OSLOGDB]' in t.upper()])
outsystems_prefixed = sorted([t.split('.')[-1].strip('[]') for t in missing
                               if '[' in t and '[OSLOGDB]' not in t.upper()
                               and t.upper().split(']')[0].strip('[') == 'OUTSYSTEMS'])

# ── Query 1: plain tables in outsystems DB ─────────────────────────────────
table_list = ',\n  '.join(f"'{t}'" for t in plain + outsystems_prefixed)
q1 = f"""SELECT
    t.TABLE_SCHEMA,
    t.TABLE_NAME,
    c.COLUMN_NAME,
    c.DATA_TYPE,
    c.CHARACTER_MAXIMUM_LENGTH,
    c.IS_NULLABLE,
    c.COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.TABLES t
JOIN INFORMATION_SCHEMA.COLUMNS c
    ON t.TABLE_NAME = c.TABLE_NAME
    AND t.TABLE_SCHEMA = c.TABLE_SCHEMA
WHERE t.TABLE_TYPE = 'BASE TABLE'
AND t.TABLE_NAME IN (
  {table_list}
)
ORDER BY t.TABLE_NAME, c.ORDINAL_POSITION;
"""

with open('/Users/mattcomroe/tormentnexus/scripts/missing_outsystems.sql', 'w') as f:
    f.write(q1)

# ── Query 2: OSLogDB tables ────────────────────────────────────────────────
if oslogdb:
    table_list2 = ',\n  '.join(f"'{t}'" for t in oslogdb)
    q2 = f"""-- Run this against the OSLogDB database
SELECT
    t.TABLE_SCHEMA,
    t.TABLE_NAME,
    c.COLUMN_NAME,
    c.DATA_TYPE,
    c.CHARACTER_MAXIMUM_LENGTH,
    c.IS_NULLABLE,
    c.COLUMN_DEFAULT
FROM INFORMATION_SCHEMA.TABLES t
JOIN INFORMATION_SCHEMA.COLUMNS c
    ON t.TABLE_NAME = c.TABLE_NAME
    AND t.TABLE_SCHEMA = c.TABLE_SCHEMA
WHERE t.TABLE_TYPE = 'BASE TABLE'
AND t.TABLE_NAME IN (
  {table_list2}
)
ORDER BY t.TABLE_NAME, c.ORDINAL_POSITION;
"""
    with open('/Users/mattcomroe/tormentnexus/scripts/missing_oslogdb.sql', 'w') as f:
        f.write(q2)

print(f'Plain/outsystems tables query: {len(plain + outsystems_prefixed)} tables -> scripts/missing_outsystems.sql')
print(f'OSLogDB tables query: {len(oslogdb)} tables -> scripts/missing_oslogdb.sql')
print(f'Restricted (skip): {len(missing) - len(plain) - len(outsystems_prefixed) - len(oslogdb)} tables')
