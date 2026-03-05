# Metabase_IS

## Tables

- [MetabaseDashboard](#metabasedashboard)

## MetabaseDashboard
**Physical table:** `OSUSR_RYO_METABASEDASHBOARD`  
**Description:** All available dashboards from Metabase.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| STATUS | nvarchar | 50 | YES | ('') |
