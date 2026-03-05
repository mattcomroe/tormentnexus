# W_Management_SH_CS

## Tables

- [CustomerUserCount](#customerusercount)
- [DefaultCustomerValues](#defaultcustomervalues)

## CustomerUserCount
**Physical table:** `OSUSR_72o_TenantUserCount`  
**Description:** Contains total active users at a customer location  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TOTALUSERS | int |  | YES | ((0)) |
| TOTALACTIVEUSERS | int |  | YES | ((0)) |
| TOTALINACTIVEUSERS | nvarchar | 50 | YES | ('') |
| TOTALSTEVESCLUB | nvarchar | 50 | YES | ('') |
| TOTALACTIVESTEVESCLUB | nvarchar | 50 | YES | ('') |
| TOTALINACTIVESTEVESCLUB | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| LOCATIONID | int |  | YES | (NULL) |
| INACTIVEUSERCOUNT | int |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |

## DefaultCustomerValues
**Physical table:** `OSUSR_72o_DefaultTenantValues`  
**Description:** contains the default welcome email used for a customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| VALUE | ntext | 1073741823 | YES | ('') |
