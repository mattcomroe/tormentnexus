# Sample_Task_CS

## Tables

- [Task](#task)
- [TaskAttachment](#taskattachment)
- [TaskAttachmentBinary](#taskattachmentbinary)
- [TaskProject](#taskproject)
- [TaskSort](#tasksort)
- [TaskTag](#tasktag)

## Task
**Physical table:** `OSUSR_RJ6_TASK`  
**Description:** Represents a task that needs to be carried out  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| DUEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TAGID | int |  | YES | (NULL) |
| ISDONE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| DUETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISTIMEDEFINEDBYUSER | bit |  | YES | ((0)) |
| TASKPROJECTID | bigint |  | YES | (NULL) |
| TASKTAGID | int |  | YES | (NULL) |
| COMPLETEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((1)) |

## TaskAttachment
**Physical table:** `OSUSR_RJ6_TASKATTACHMENT`  
**Description:** Entity that holds the metadata of the task's attachments.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TASKID | bigint |  | YES | (NULL) |
| FILENAME | nvarchar | 100 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## TaskAttachmentBinary
**Physical table:** `OSUSR_RJ6_TASKATTACHMENTBINARY`  
**Description:** Entity that holds the binary content of the task's attachments.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TASKATTACHMENTID | bigint |  | NO |  |
| BINARY | varbinary | -1 | YES | (NULL) |

## TaskProject
**Physical table:** `OSUSR_RJ6_TASKPROJECT`  
**Description:** Represents a project that groups several tasks that need to be carried out.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## TaskSort
**Physical table:** `OSUSR_RJ6_TASKSORT`  
**Description:** Holds the possible values for the sorting of tasks' list  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| SORTVALUE | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TaskTag
**Physical table:** `OSUSR_RJ6_TAG`  
**Description:** Holds the possible values for a task's tag  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| BACKGROUNDCLASS | nvarchar | 50 | YES | ('') |
| TEXTCLASS | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
