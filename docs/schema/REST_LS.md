# REST_LS

## Tables

- [AuthenticationToken](#authenticationtoken)
- [HTTPStatus](#httpstatus)

## AuthenticationToken
**Physical table:** `OSUSR_4N4_AUTHENTICATIONTOKEN`  
**Description:** The AuthenticationToken is a small temporary key that will identify an user. See the action GenerateToken for more information about the process of creating a new token.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TOKEN | nvarchar | 501 | YES | ('') |
| EXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| REFRESHTOKEN | nvarchar | 251 | YES | ('') |
| REFRESHEXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| USERID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | ((0)) |

## HTTPStatus
**Physical table:** `OSUSR_4N4_HTTPSTATUS`  
**Description:** Contains all HTTP Status (from wikipedia)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TYPE | nvarchar | 50 | YES | ('') |
| MESSAGE | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 1000 | YES | ('') |
