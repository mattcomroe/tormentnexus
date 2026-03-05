import csv
import os
import re
from collections import defaultdict

RESTRICTED_DBS = {'OSLOG_SUMMARY', 'REPORTINGOUTSYSTEMSINTEGRATION', 'YEARREVIEWDB'}
EXTERNAL_DBS   = {'OSLOGDB'} | RESTRICTED_DBS

# ── Load eSpace ID → name mapping ──────────────────────────────────────────
espaces = {}
with open('/Users/mattcomroe/tormentnexus/espace_table_contents.csv') as f:
    for r in csv.DictReader(f):
        espaces[r['ID']] = r['NAME']

# ── Load active non-system entities ────────────────────────────────────────
entities = {}
with open('/Users/mattcomroe/tormentnexus/Entity_Mapping - Sheet1.csv') as f:
    for r in csv.DictReader(f):
        if r['IS_ACTIVE'] == '1' and r['IS_SYSTEM'] == '0':
            espace_name = espaces.get(r['ESPACE_ID'], 'Unknown')
            phys = r['PHYSICAL_TABLE_NAME']

            # Detect external DB tables (e.g. [OSLogDB].[dbo].[tablename])
            external_db = None
            if phys.startswith('['):
                db_part = phys.split('.')[0].strip('[]').upper()
                if db_part in EXTERNAL_DBS:
                    external_db = phys.split('.')[0].strip('[]')  # preserve original casing

            entities[phys.upper()] = {
                'espace': espace_name,
                'name': r['NAME'],
                'description': r['DESCRIPTION'].strip(),
                'physical_original': phys,
                'external_db': external_db,
            }

# ── Parse SCHEMA.md into table → column rows ───────────────────────────────
table_columns = {}
current_table = None
collecting = False

with open('/Users/mattcomroe/tormentnexus/docs/SCHEMA.md') as f:
    for line in f:
        line = line.rstrip('\n')
        if line.startswith('## ') and not line.startswith('## Table'):
            current_table = line[3:].strip().upper()
            table_columns[current_table] = []
            collecting = True
        elif collecting and line.startswith('|'):
            table_columns[current_table].append(line)
        elif collecting and line == '':
            pass
        elif collecting and not line.startswith('|') and line != '':
            collecting = False

# ── Group entities by eSpace ───────────────────────────────────────────────
by_espace = defaultdict(list)
for phys_upper, meta in entities.items():
    by_espace[meta['espace']].append((phys_upper, meta))

for espace in by_espace:
    by_espace[espace].sort(key=lambda x: x[1]['name'].lower())

# ── Write output files ─────────────────────────────────────────────────────
out_dir = '/Users/mattcomroe/tormentnexus/docs/schema'
os.makedirs(out_dir, exist_ok=True)

# Clear existing files
for f in os.listdir(out_dir):
    os.remove(os.path.join(out_dir, f))

def safe_filename(name):
    return re.sub(r'[^\w\-]', '_', name) + '.md'

stats = {'with_cols': 0, 'pending': 0, 'restricted': 0, 'external': 0}

for espace_name, tables in sorted(by_espace.items()):
    lines = [f'# {espace_name}\n', '## Tables\n']

    for phys_upper, meta in tables:
        anchor = meta['name'].lower().replace('_', '-').replace(' ', '-')
        lines.append(f'- [{meta["name"]}](#{anchor})')
    lines.append('')

    for phys_upper, meta in tables:
        phys = meta['physical_original']
        lines.append(f'## {meta["name"]}')
        lines.append(f'**Physical table:** `{phys}`  ')
        if meta['description']:
            lines.append(f'**Description:** {meta["description"]}  ')
        lines.append('')

        # Determine the lookup key for schema (plain table name for external DB tables)
        if meta['external_db']:
            lookup_key = phys.split('.')[-1].strip('[]').upper()
        else:
            lookup_key = phys_upper

        cols = table_columns.get(lookup_key)
        ext_db = meta['external_db']

        if cols:
            for col_line in cols:
                lines.append(col_line)
            stats['with_cols'] += 1
        elif ext_db and ext_db.upper() in RESTRICTED_DBS:
            lines.append(f'_Column definitions unavailable — table is in a restricted external database (`{ext_db}`). Elevated database access required._')
            stats['restricted'] += 1
        elif ext_db:
            lines.append(f'_Column definitions pending — table is in an external database (`{ext_db}`). Run `scripts/missing_{ext_db.lower()}.sql` against that database to populate._')
            stats['external'] += 1
        else:
            lines.append('_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._')
            stats['pending'] += 1

        lines.append('')

    filename = os.path.join(out_dir, safe_filename(espace_name))
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))

print(f'Files written:          {len(by_espace)}')
print(f'Tables with columns:    {stats["with_cols"]}')
print(f'Pending (outsystems):   {stats["pending"]}')
print(f'Pending (OSLogDB):      {stats["external"]}')
print(f'Restricted (no access): {stats["restricted"]}')
