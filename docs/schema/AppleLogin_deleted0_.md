# AppleLogin(deleted0)

## Tables

- [LocalUserApple](#localuserapple)
- [UserApple](#userapple)

## LocalUserApple
**Physical table:** `OSUSR_d90_LocalUserApple`  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## UserApple
**Physical table:** `OSUSR_d90_UserApple`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| APPLEUSERID | nvarchar | 50 | YES | ('') |
| GIVENNAME | nvarchar | 50 | YES | ('') |
| FAMILYNAME | nvarchar | 50 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
