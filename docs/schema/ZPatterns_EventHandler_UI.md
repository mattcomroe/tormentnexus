# ZPatterns_EventHandler_UI

## Tables

- [ActivityFeedPOCOld](#activityfeedpocold)
- [DummyTest](#dummytest)
- [Entity1](#entity1)

## ActivityFeedPOCOld
**Physical table:** `OSUSR_9D7_ACTIVITYFEED`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| IS_ACTIVE | bit |  | YES | ((0)) |
| BUSINESSACTION | nvarchar | 50 | YES | ('') |
| BUSINESSACTIONTYPE | nvarchar | 50 | YES | ('') |
| CRUDACTION | nvarchar | 50 | YES | ('') |
| ENTITYNAME | nvarchar | 50 | YES | ('') |
| ISUSERACTION | bit |  | YES | ((0)) |

## DummyTest
**Physical table:** `OSUSR_9D7_DUMMYTEST`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |

## Entity1
**Physical table:** `OSUSR_9D7_ENTITY1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ATTRIBUTE1 | varbinary | -1 | YES | (NULL) |
