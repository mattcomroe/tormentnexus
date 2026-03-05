# RichWidgets

## Tables

- [IconName](#iconname)
- [IconSize](#iconsize)
- [MessageType](#messagetype)
- [RecentItem](#recentitem)
- [UploadCache](#uploadcache)
- [UploadToken](#uploadtoken)

## IconName
**Physical table:** `OSUSR_5z9_IconName`  
**Description:** The list of icons you can use. For more information, please refer to http://fontawesome.io/icons/  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASS | nvarchar | 50 | NO |  |

## IconSize
**Physical table:** `OSUSR_5z9_IconSize`  
**Description:** Awesome icon size  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASS | nvarchar | 50 | NO |  |

## MessageType
**Physical table:** `OSUSR_5z9_MessageType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## RecentItem
**Physical table:** `OSUSR_5z9_RecentItem1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ESPACEID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| LABEL | nvarchar | 100 | YES | ('') |
| TAG | nvarchar | 50 | YES | ('') |
| URL | nvarchar | 150 | YES | ('') |
| INSTANT | datetime |  | YES | ('1900-01-01 00:00:00') |

## UploadCache
**Physical table:** `OSUSR_5z9_UploadCache`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CONTENT | image | 2147483647 | YES | (NULL) |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 100 | YES | ('') |

## UploadToken
**Physical table:** `OSUSR_5z9_UploadToken`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TOKEN | nvarchar | 50 | YES | ('') |
