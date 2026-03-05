# RocketUI_DBSampleData

## Tables

- [Sample_KanbanCard](#sample-kanbancard)
- [Sample_KanbanCardPerson](#sample-kanbancardperson)
- [Sample_KanbanCardTags](#sample-kanbancardtags)
- [Sample_KanbanColumn](#sample-kanbancolumn)
- [Sample_KanbanProjectPerson](#sample-kanbanprojectperson)
- [Sample_Project](#sample-project)
- [Sample_Status](#sample-status)
- [Sample_Tag](#sample-tag)

## Sample_KanbanCard
**Physical table:** `OSUSR_PCU_SAMPLE_KANBANCARD`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TITLE | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| KANBANCOLUMNID | bigint |  | YES | (NULL) |
| PROJECTID | bigint |  | YES | (NULL) |
| STATUSID | bigint |  | YES | (NULL) |

## Sample_KanbanCardPerson
**Physical table:** `OSUSR_PCU_SAMPLE_KANBANCARDPERSON`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| KANBANCARDID | bigint |  | YES | (NULL) |
| SAMPLE_EMPLOYEEID | int |  | YES | (NULL) |

## Sample_KanbanCardTags
**Physical table:** `OSUSR_PCU_SAMPLE_KANBANCARDTAGS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SMPLE_KANBANCARDID | bigint |  | YES | (NULL) |
| SAMPLE_TAGID | bigint |  | YES | (NULL) |

## Sample_KanbanColumn
**Physical table:** `OSUSR_PCU_SAMPLE_KANBANCOLUMN`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |

## Sample_KanbanProjectPerson
**Physical table:** `OSUSR_PCU_SAMPLE_KANBANPROJECTPERSON`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROJECTID | bigint |  | YES | (NULL) |
| SAMPLE_EMPLOYEEID | int |  | YES | (NULL) |

## Sample_Project
**Physical table:** `OSUSR_PCU_SAMPLE_PROJECT`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TITLE | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 1000 | YES | ('') |
| TIMEWORKED | int |  | YES | ((0)) |
| TIMEESTIMATED | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Sample_Status
**Physical table:** `OSUSR_PCU_SAMPLE_STATUS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STATUS | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Sample_Tag
**Physical table:** `OSUSR_PCU_SAMPLE_TAG`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
