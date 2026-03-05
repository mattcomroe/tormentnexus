import csv, os, re

SCHEMA_DIR = '/Users/mattcomroe/tormentnexus/docs/schema'

# ── Parse oslogdb_schema.csv for new column data ───────────────────────────
new_cols = {}  # table_name_upper -> list of markdown column rows
for csvfile in ['oslogdb_schema.csv', 'outsystems_schema2.csv']:
    path = f'/Users/mattcomroe/tormentnexus/{csvfile}'
    with open(path) as f:
        for r in csv.DictReader(f):
            if not r.get('TABLE_NAME') or r['TABLE_NAME'].startswith('-') or not r['TABLE_NAME'].strip():
                continue
            t = r['TABLE_NAME'].strip().upper()
            if t not in new_cols:
                new_cols[t] = ['| Column | Data Type | Max Length | Nullable | Default |',
                               '| --- | --- | --- | --- | --- |']
            new_cols[t].append(
                f'| {r["COLUMN_NAME"].strip()} | {r["DATA_TYPE"].strip()} | {r["CHARACTER_MAXIMUM_LENGTH"].strip()} | {r["IS_NULLABLE"].strip()} | {r["COLUMN_DEFAULT"].strip()} |'
            )

print(f'Tables with new column data: {len(new_cols)}')

# ── Update docs ────────────────────────────────────────────────────────────
merged = 0
updated_pending = 0

PENDING_OUTSYSTEMS = '_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._'
PENDING_OSLOGDB    = '_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_OSLogDB.sql` against that database to populate._'
NOT_IN_DEV         = '_Table not present in the dev environment — schema unavailable. May exist in production only._'

for fname in sorted(os.listdir(SCHEMA_DIR)):
    fpath = os.path.join(SCHEMA_DIR, fname)
    with open(fpath) as f:
        content = f.read()

    new_content = content

    # Replace pending entries that now have column data
    for t_upper, col_rows in new_cols.items():
        col_block = '\n'.join(col_rows)
        # Match physical table names (could be plain or bracket-prefixed)
        pattern = rf'(\*\*Physical table:\*\* `[^`]*{re.escape(t_upper)}[^`]*`[^\n]*\n(?:\*\*Description:\*\*[^\n]*\n)?)\n_Column definitions pending[^_]*_'
        replacement = rf'\1\n{col_block}'
        result = re.sub(pattern, replacement, new_content, flags=re.IGNORECASE)
        if result != new_content:
            merged += 1
            new_content = result

    # Replace remaining "pending outsystems" and "pending oslogdb" with "not in dev"
    for placeholder in [PENDING_OUTSYSTEMS, PENDING_OSLOGDB]:
        count = new_content.count(placeholder)
        if count:
            new_content = new_content.replace(placeholder, NOT_IN_DEV)
            updated_pending += count

    if new_content != content:
        with open(fpath, 'w') as f:
            f.write(new_content)

print(f'Merged new column data:        {merged}')
print(f'Marked as not-in-dev:          {updated_pending}')
