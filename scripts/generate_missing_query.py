import csv

espaces = {}
with open('/Users/mattcomroe/tormentnexus/espace_table_contents.csv') as f:
    for r in csv.DictReader(f):
        espaces[r['ID']] = r['NAME']

entities = {}
with open('/Users/mattcomroe/tormentnexus/Entity_Mapping - Sheet1.csv') as f:
    for r in csv.DictReader(f):
        if r['IS_ACTIVE'] == '1' and r['IS_SYSTEM'] == '0':
            entities[r['PHYSICAL_TABLE_NAME'].upper()] = r['PHYSICAL_TABLE_NAME']

# Find tables that exist in docs but have no column data (placeholder text)
import os, re
tables_with_cols = set()
for fname in os.listdir('/Users/mattcomroe/tormentnexus/docs/schema'):
    current_physical = None
    with open(f'/Users/mattcomroe/tormentnexus/docs/schema/{fname}') as f:
        for line in f:
            m = re.match(r'\*\*Physical table:\*\* `(.+)`', line.strip())
            if m:
                current_physical = m.group(1).upper()
            if current_physical and line.startswith('| ') and 'Column' not in line and '---' not in line:
                tables_with_cols.add(current_physical)

missing = [orig for upper, orig in entities.items() if upper not in tables_with_cols]
missing.sort()
print(f'Missing tables: {len(missing)}')

table_list = ',\n  '.join(f"'{t}'" for t in missing)

query = f"""SELECT
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

with open('/Users/mattcomroe/tormentnexus/scripts/missing_tables.sql', 'w') as f:
    f.write(query)

print('Written to scripts/missing_tables.sql')
