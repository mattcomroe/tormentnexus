# FileStorage_API

## Tables

- [APIMethod](#apimethod)

## APIMethod
**Physical table:** `OSUSR_WV5_APIMETHOD`  
**Description:** Specific API methods.   Update the following support document everytime a record it's created: https://docs.google.com/document/d/1IAsZosiKY0vJL1fMrSi6pI1eMhxQWvNaB0R9vtv-LwA/  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 500 | YES | ('') |
| FILETYPEID | int |  | YES | (NULL) |
| REQUESTER | nvarchar | 500 | YES | ('') |
| DESCRIPTION | nvarchar | 1000 | YES | ('') |
