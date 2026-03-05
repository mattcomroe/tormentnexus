# MultipleFileUpload(deleted0)

## Tables

- [UploadCache](#uploadcache)

## UploadCache
**Physical table:** `OSUSR_hyr_UploadCache`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SESSIONID | nvarchar | 100 | YES | ('') |
| FILENAME | nvarchar | 100 | YES | ('') |
| FILETYPE | nvarchar | 100 | YES | ('') |
| FILESIZE | decimal |  | YES | ((0)) |
| CONTENT | varbinary | -1 | YES | (NULL) |
| CREATED | datetime |  | YES | ('1900-01-01 00:00:00') |
