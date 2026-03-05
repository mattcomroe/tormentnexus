# AppleLogin(deleted0)

## Tables

- [LocalUserApple](#localuserapple)
- [UserApple](#userapple)

## LocalUserApple
**Physical table:** `OSUSR_d90_LocalUserApple`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## UserApple
**Physical table:** `OSUSR_d90_UserApple`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| APPLEUSERID | nvarchar | 50 | YES | ('') |
| GIVENNAME | nvarchar | 50 | YES | ('') |
| FAMILYNAME | nvarchar | 50 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
