# Discovery

## Tables

- [Category](#category)
- [Comparator](#comparator)
- [MenuItem](#menuitem)
- [MenuSubItem](#menusubitem)

## Category
**Physical table:** `OSUSR_mnd_Category`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CAPTION | nvarchar | 50 | NO |  |

## Comparator
**Physical table:** `OSUSR_mnd_Comparator`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## MenuItem
**Physical table:** `OSUSR_mnd_MenuItem`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## MenuSubItem
**Physical table:** `OSUSR_mnd_MenuSubItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |
| MENUITEMID | int |  | YES | (NULL) |
