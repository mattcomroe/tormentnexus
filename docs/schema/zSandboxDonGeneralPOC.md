# zSandboxDonGeneralPOC

## Tables

- [Feature_SE](#feature-se)
- [UnitTest](#unittest)

## Feature_SE
**Physical table:** `OSUSR_gpn_Feature_SE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## UnitTest
**Physical table:** `OSUSR_gpn_UnitTest`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
