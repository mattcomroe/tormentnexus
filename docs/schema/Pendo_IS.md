# Pendo_IS

## Tables

- [Kind](#kind)
- [Type](#type)

## Kind
**Physical table:** `OSUSR_VIN_KIND`  
**Description:** visitor or "account"  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Type
**Physical table:** `OSUSR_VIN_TYPE`  
**Description:** type of metadata field  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
