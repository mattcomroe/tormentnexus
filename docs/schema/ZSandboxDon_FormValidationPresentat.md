# ZSandboxDon_FormValidationPresentat

## Tables

- [AllMandatoryTable](#allmandatorytable)
- [NoRequirementsTable](#norequirementstable)

## AllMandatoryTable
**Physical table:** `OSUSR_QCR_ALLMANDATORYTABLE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| BINARYDATA | varbinary | -1 | YES | (NULL) |
| BOOLEAN | bit |  | YES | ((0)) |
| CURRENCY | nvarchar | 50 | YES | ('') |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| DATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAIL | nvarchar | 250 | YES | ('') |
| INTEGER | int |  | YES | ((0)) |
| LONGINTEGER | bigint |  | YES | ((0)) |
| PHONE | nvarchar | 20 | YES | ('') |
| TIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| TEXT | nvarchar | 50 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## NoRequirementsTable
**Physical table:** `OSUSR_QCR_NOREQUIREMENTSTABLE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| BINARYDATA | varbinary | -1 | YES | (NULL) |
| BOOLEAN | bit |  | YES | ((0)) |
| CURRENCY | nvarchar | 50 | YES | ('') |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| DATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAIL | nvarchar | 250 | YES | ('') |
| INTEGER | int |  | YES | ((0)) |
| LONGINTEGER | bigint |  | YES | ((0)) |
| PHONE | nvarchar | 20 | YES | ('') |
| TIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| TEXT | nvarchar | 50 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
