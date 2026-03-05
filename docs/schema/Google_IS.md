# Google_IS

## Tables

- [GoogleAccount](#googleaccount)

## GoogleAccount
**Physical table:** `OSUSR_xob_GoogleAccount`  
**Description:** A google account.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EMAIL | nvarchar | 250 | YES | ('') |
| REFRESHTOKEN | nvarchar | 1000 | YES | ('') |
| SCOPE | nvarchar | 2000 | YES | ('') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISVALID | bit |  | YES | ((0)) |
| ACCESS_TOKEN | nvarchar | 900 | YES | ('') |
| ACCESS_TOKENEXPIRATION | datetime |  | YES | ('1900-01-01 00:00:00') |
| TOKEN_TYPE | nvarchar | 50 | YES | ('') |
