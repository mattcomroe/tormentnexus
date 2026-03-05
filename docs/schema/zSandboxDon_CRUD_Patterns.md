# zSandboxDon_CRUD_Patterns

## Tables

- [SampleEntity](#sampleentity)
- [SampleEntity_Extension](#sampleentity-extension)

## SampleEntity
**Physical table:** `OSUSR_BZE_SAMPLEENTITY`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| NAME | nvarchar | 50 | YES | ('') |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| MESSAGETYPEID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## SampleEntity_Extension
**Physical table:** `OSUSR_BZE_SAMPLEENTITY_EXTENSION`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SAMPLEENTITYID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| NAME | nvarchar | 50 | YES | ('') |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| MESSAGETYPEID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
