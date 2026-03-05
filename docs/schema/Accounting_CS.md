# Accounting_CS

## Tables

- [AccountingType](#accountingtype)
- [CustomerAccounting](#customeraccounting)

## AccountingType
**Physical table:** `OSUSR_0MH_ACCOUNTINGTYPE`  
**Description:** Accounting integrations supported by Wodify  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CustomerAccounting
**Physical table:** `OSUSR_0MH_CUSTOMERACCOUNTING`  
**Description:** Entity that have accounting types for each Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ACCOUNTINGTYPEID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
