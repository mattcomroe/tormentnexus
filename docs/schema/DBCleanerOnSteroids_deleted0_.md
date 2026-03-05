# DBCleanerOnSteroids(deleted0)

## Tables

- [AutomatedCleanup](#automatedcleanup)
- [LogTableType](#logtabletype)
- [Plugin](#plugin)

## AutomatedCleanup
**Physical table:** `OSUSR_00b_AutomatedCleanup`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOGTABLETYPEID | int |  | YES | (NULL) |
| MAXDAYSTOKEEP | int |  | YES | ((0)) |
| MAXRECORDS | bigint |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## LogTableType
**Physical table:** `OSUSR_00b_LogTableType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| PHYSICALTABLE | nvarchar | 50 | YES | ('') |
| PHYSICALTABLEPREFIX | nvarchar | 50 | YES | ('') |
| PHYSICALDETAILSTABLEPREFIX | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Plugin
**Physical table:** `OSUSR_00b_Plugin`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 125 | YES | ('') |
| DESCRIPTION | nvarchar | 256 | YES | ('') |
| MENULABEL | nvarchar | 50 | YES | ('') |
| ENTRYPOINTURL | nvarchar | 256 | YES | ('') |
