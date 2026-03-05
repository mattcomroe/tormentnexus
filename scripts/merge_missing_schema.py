import csv, os, re

SCHEMA_DIR = '/Users/mattcomroe/tormentnexus/docs/schema'
ENTITY_MAP = '/Users/mattcomroe/tormentnexus/Entity_Mapping - Sheet1.csv'
MISSING_CSV = '/Users/mattcomroe/tormentnexus/missing_schema.csv'

RESTRICTED = {'OSLog_Summary', 'ReportingOutsystemsIntegration', 'YearReviewDB'}

# ── Load new column data from missing_schema.csv ───────────────────────────
new_cols = {}  # physical_upper -> markdown column rows
with open(MISSING_CSV) as f:
    for r in csv.DictReader(f):
        t = r['TABLE_NAME'].upper()
        if t not in new_cols:
            new_cols[t] = ['| Column | Data Type | Max Length | Nullable | Default |',
                           '| --- | --- | --- | --- | --- |']
        new_cols[t].append(
            f'| {r["COLUMN_NAME"]} | {r["DATA_TYPE"]} | {r["CHARACTER_MAXIMUM_LENGTH"]} | {r["IS_NULLABLE"]} | {r["COLUMN_DEFAULT"]} |'
        )

# ── Load entity map: physical_upper -> logical name ────────────────────────
logical_names = {}
with open(ENTITY_MAP) as f:
    for r in csv.DictReader(f):
        logical_names[r['PHYSICAL_TABLE_NAME'].upper()] = r['NAME']

# ── Process each schema doc ────────────────────────────────────────────────
updated = 0
removed = 0
restricted_flagged = 0

for fname in sorted(os.listdir(SCHEMA_DIR)):
    fpath = os.path.join(SCHEMA_DIR, fname)
    with open(fpath) as f:
        content = f.read()

    # Split into per-table blocks
    # Each block starts with "## <EntityName>"
    blocks = re.split(r'(?=^## )', content, flags=re.MULTILINE)
    header = blocks[0]  # eSpace title + TOC
    table_blocks = blocks[1:]

    new_blocks = [header]
    file_changed = False
    kept_names = []

    for block in table_blocks:
        # Get logical name from heading
        name_match = re.match(r'^## (.+)', block)
        if not name_match:
            new_blocks.append(block)
            continue
        logical_name = name_match.group(1).strip()

        # Get physical table name from block
        phys_match = re.search(r'\*\*Physical table:\*\* `(.+?)`', block)
        if not phys_match:
            new_blocks.append(block)
            kept_names.append(logical_name)
            continue
        physical = phys_match.group(1)
        physical_upper = physical.upper()

        # Case 1: restricted table — add access note
        if logical_name in RESTRICTED:
            block = re.sub(
                r'_Column definitions not found in schema export\._',
                '_Column definitions unavailable — elevated database access required._',
                block
            )
            new_blocks.append(block)
            kept_names.append(logical_name)
            restricted_flagged += 1
            file_changed = True
            continue

        # Case 2: new column data available — replace placeholder
        if physical_upper in new_cols:
            col_lines = '\n'.join(new_cols[physical_upper])
            block = re.sub(
                r'_Column definitions not found in schema export\._',
                col_lines,
                block
            )
            new_blocks.append(block)
            kept_names.append(logical_name)
            updated += 1
            file_changed = True
            continue

        # Case 3: still no column data — remove the entry
        if '_Column definitions not found in schema export._' in block:
            removed += 1
            file_changed = True
            continue

        # Case 4: has real column data — keep as-is
        new_blocks.append(block)
        kept_names.append(logical_name)

    if file_changed:
        # Rebuild TOC from kept table names
        toc_lines = ['## Tables\n']
        for name in kept_names:
            anchor = name.lower().replace('_', '-').replace(' ', '-')
            toc_lines.append(f'- [{name}](#{anchor})')
        toc_lines.append('')
        toc_block = '\n'.join(toc_lines)

        new_content = ''.join(new_blocks)
        # Replace old TOC
        new_content = re.sub(
            r'## Tables\n.*?(?=\n## |\Z)',
            toc_block + '\n',
            new_content,
            count=1,
            flags=re.DOTALL
        )

        if kept_names:
            with open(fpath, 'w') as f:
                f.write(new_content)
        else:
            # All tables removed — delete the file
            os.remove(fpath)
            removed += 1

print(f'Updated with new column data: {updated}')
print(f'Flagged as access-restricted: {restricted_flagged}')
print(f'Removed (no physical table):  {removed}')
