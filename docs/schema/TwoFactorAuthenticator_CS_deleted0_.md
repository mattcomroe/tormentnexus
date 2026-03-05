# TwoFactorAuthenticator_CS(deleted0)

## Tables

- [UserSecret](#usersecret)
- [UserTempStorage](#usertempstorage)

## UserSecret
**Physical table:** `OSUSR_HUK_USERSECRET`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SECRET | nvarchar | 16 | YES | ('') |
| ISTWOFACTORENABLED | bit |  | YES | ((0)) |
| OTPAUTH | nvarchar | 500 | YES | ('') |

## UserTempStorage
**Physical table:** `OSUSR_HUK_USERTEMPSTORAGE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 36 | NO |  |
| REMEMBERLOGIN | bit |  | YES | ((0)) |
| USERID | int |  | YES | (NULL) |
| CREATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
