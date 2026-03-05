import csv
import os
import re
from collections import defaultdict

# ── Load eSpace ID → name mapping ──────────────────────────────────────────
espaces = {}
with open('/Users/mattcomroe/tormentnexus/espace_table_contents.csv') as f:
    for r in csv.DictReader(f):
        espaces[r['ID']] = r['NAME']

# ── Load active non-system entities ────────────────────────────────────────
entities = {}  # physical_table_name → {espace_name, logical_name, description}
with open('/Users/mattcomroe/tormentnexus/Entity_Mapping - Sheet1.csv') as f:
    for r in csv.DictReader(f):
        if r['IS_ACTIVE'] == '1' and r['IS_SYSTEM'] == '0':
            espace_name = espaces.get(r['ESPACE_ID'], 'Unknown')
            entities[r['PHYSICAL_TABLE_NAME'].upper()] = {
                'espace': espace_name,
                'name': r['NAME'],
                'description': r['DESCRIPTION'].strip(),
            }

# ── Parse SCHEMA.md into table → column rows ───────────────────────────────
table_columns = {}  # table_name_upper → list of raw markdown rows
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
        elif collecting and line == '' and current_table:
            pass  # allow blank lines inside table
        elif collecting and not line.startswith('|') and line != '':
            collecting = False

# ── Group entities by eSpace ───────────────────────────────────────────────
by_espace = defaultdict(list)
for phys, meta in entities.items():
    by_espace[meta['espace']].append((phys, meta))

# Sort tables within each eSpace by logical name
for espace in by_espace:
    by_espace[espace].sort(key=lambda x: x[1]['name'].lower())

# ── Write output files ─────────────────────────────────────────────────────
out_dir = '/Users/mattcomroe/tormentnexus/docs/schema'
os.makedirs(out_dir, exist_ok=True)

def safe_filename(name):
    return re.sub(r'[^\w\-]', '_', name) + '.md'

written = 0
skipped = 0

for espace_name, tables in sorted(by_espace.items()):
    lines = [f'# {espace_name}\n']

    # Table of contents
    lines.append('## Tables\n')
    for phys, meta in tables:
        anchor = meta['name'].lower().replace('_', '-').replace(' ', '-')
        lines.append(f'- [{meta["name"]}](#{anchor})')
    lines.append('')

    for phys, meta in tables:
        lines.append(f'## {meta["name"]}')
        lines.append(f'**Physical table:** `{phys}`  ')
        if meta['description']:
            lines.append(f'**Description:** {meta["description"]}  ')
        lines.append('')

        cols = table_columns.get(phys)
        if cols:
            for col_line in cols:
                lines.append(col_line)
        else:
            lines.append('_Column definitions not found in schema export._')
        lines.append('')

    filename = os.path.join(out_dir, safe_filename(espace_name))
    with open(filename, 'w') as f:
        f.write('\n'.join(lines))
    written += 1

print(f'Written: {written} files, Skipped: {skipped}')
print(f'Tables with column data: {sum(1 for p, _ in [(p, m) for tables in by_espace.values() for p, m in tables] if table_columns.get(p))}')
print(f'Tables missing column data: {sum(1 for p, _ in [(p, m) for tables in by_espace.values() for p, m in tables] if not table_columns.get(p))}')
