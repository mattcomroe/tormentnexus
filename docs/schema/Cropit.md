# Cropit

## Tables

- [Image](#image)
- [MenuItem](#menuitem)
- [MenuSubItem](#menusubitem)

## Image
**Physical table:** `OSUSR_hjr_Image`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| CODE | nvarchar | 255 | YES | ('') |
| FILENAME | nvarchar | 255 | YES | ('') |
| TYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| CREATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |

## MenuItem
**Physical table:** `OSUSR_hjr_MenuItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## MenuSubItem
**Physical table:** `OSUSR_hjr_MenuSubItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |
| MENUITEMID | int |  | YES | (NULL) |
