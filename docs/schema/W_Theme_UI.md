# W_Theme_UI

## Tables

- [AuthenticationToken](#authenticationtoken)
- [Session](#session)

## AuthenticationToken
**Physical table:** `OSUSR_I68_AUTHENTICATIONTOKEN`  
**Description:** Contains all cookie tokens created by users during login  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TOKEN | nvarchar | 50 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| ISPERSISTENT | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Session
**Physical table:** `OSUSR_0SP_SESSION`  
**Description:** Contains data that is supposed to be in session, but because there is no session in REACT, we use an entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| KIOSKLOCATIONID | bigint |  | YES | ((0)) |
| KIOSKCUSTOMERID | bigint |  | YES | ((0)) |
| GUARDIANUSERID | int |  | YES | (NULL) |
