import csv, os, re

SCHEMA_DIR = '/Users/mattcomroe/tormentnexus/docs/schema'
ENTITY_MAP = '/Users/mattcomroe/tormentnexus/Entity_Mapping - Sheet1.csv'

RESTRICTED_DBS = {'OSLOG_SUMMARY', 'REPORTINGOUTSYSTEMSINTEGRATION', 'YEARREVIEWDB'}

# Find restricted physical table names
restricted_physicals = set()
with open(ENTITY_MAP) as f:
    for r in csv.DictReader(f):
        if r['IS_ACTIVE'] == '1' and r['IS_SYSTEM'] == '0' and '[' in r['PHYSICAL_TABLE_NAME']:
            parts = r['PHYSICAL_TABLE_NAME'].split('.')
            db = parts[0].strip('[]').upper()
            if db in RESTRICTED_DBS:
                restricted_physicals.add(r['PHYSICAL_TABLE_NAME'])

print(f'Restricted tables to flag: {len(restricted_physicals)}')

flagged = 0
for fname in sorted(os.listdir(SCHEMA_DIR)):
    fpath = os.path.join(SCHEMA_DIR, fname)
    with open(fpath) as f:
        content = f.read()

    new_content = content
    for phys in restricted_physicals:
        if phys in new_content:
            new_content = new_content.replace(
                '_Column definitions not found in schema export._',
                f'_Column definitions unavailable — table lives in a restricted external database (`{phys.split(".")[0].strip("[]")}`) requiring elevated access._'
            )
            flagged += 1

    if new_content != content:
        with open(fpath, 'w') as f:
            f.write(new_content)

print(f'Flagged: {flagged}')
