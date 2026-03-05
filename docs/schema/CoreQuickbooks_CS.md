# CoreQuickbooks_CS

## Tables

- [QuickbooksDesktopExport](#quickbooksdesktopexport)

## QuickbooksDesktopExport
**Physical table:** `OSUSR_1kz_QuickbooksDesktopExport`  
**Description:** Contains all information needed to export Payments configurations to Quickbooks  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| TAXESACCOUNTNAME | nvarchar | 31 | YES | ('') |
| BANKACCOUNTNAME | nvarchar | 31 | YES | ('') |
| PROCESSINGFEESACCOUNTNAME | nvarchar | 31 | YES | ('') |
| FAILEDPAYMENTSFEESACCOUNTNAM | nvarchar | 31 | YES | ('') |
| CHARGEBACKFEESACCOUNTNAME | nvarchar | 31 | YES | ('') |
| WODIFYARENAACCOUNTNAME | nvarchar | 31 | YES | ('') |
| WODIFYRISEACCOUNTNAME | nvarchar | 31 | YES | ('') |
| WODIFYLIVEACCOUNTNAME | nvarchar | 31 | YES | ('') |
| ISDEFAULTCONFIGURATION | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| STRIPELOANACCOUNTNAME | nvarchar | 31 | YES | ('') |
