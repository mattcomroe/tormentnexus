# DiscoveryAPI_Auth_LIB

## Tables

- [AuthDetail](#authdetail)

## AuthDetail
**Physical table:** `OSUSR_NMO_AUTHDETAIL`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PRIVATEKEY | nvarchar | -1 | YES | ('') |
| CREATEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENVIRONMENT | nvarchar | 2000 | YES | ('') |
| GUID | nvarchar | 150 | YES | ('') |
