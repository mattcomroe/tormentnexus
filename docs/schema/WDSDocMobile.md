# WDSDocMobile

## Tables

- [DummyDropdown](#dummydropdown)
- [DummyList](#dummylist)

## DummyDropdown
**Physical table:** `OSUSR_iv7_DummyDropdown`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## DummyList
**Physical table:** `OSUSR_iv7_DummyList`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TITLE | nvarchar | 50 | YES | ('') |
| SUBTITLE | nvarchar | 50 | YES | ('') |
