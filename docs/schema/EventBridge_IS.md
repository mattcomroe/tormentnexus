# EventBridge_IS

## Tables

- [PublishEventBackup](#publisheventbackup)
- [PublishEventFailure](#publisheventfailure)

## PublishEventBackup
**Physical table:** `OSUSR_cv7_PublishEventBackup`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUEST | nvarchar | -1 | YES | ('') |
| RETRIES | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ERROR | nvarchar | 50 | YES | ('') |

## PublishEventFailure
**Physical table:** `OSUSR_cv7_PublishEventFailure`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUEST | nvarchar | -1 | YES | ('') |
| RETRIES | int |  | YES | ((0)) |
| BACKUPCREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ERROR | nvarchar | 50 | YES | ('') |
| FAILEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
