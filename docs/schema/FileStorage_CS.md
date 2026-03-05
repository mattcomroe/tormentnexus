# FileStorage_CS

## Tables

- [FileStorage](#filestorage)

## FileStorage
**Physical table:** `OSUSR_MRI_FILESTORAGE`  
**Description:** Contains files information to get from an external provider  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TITLE | nvarchar | 250 | YES | ('') |
| CONTAINER | nvarchar | 500 | YES | ('') |
| EXTERNALIDENTIFIER | nvarchar | 1000 | YES | ('') |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 1000 | YES | ('') |
| FILESIZE | int |  | YES | ((0)) |
| URI | nvarchar | 2000 | YES | ('') |
| SSLURI | nvarchar | 2000 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ISSTILLINRACKSPACE | bit |  | YES | ((0)) |
