# LTAutomationJenkins

## Tables

- [MenuItem](#menuitem)
- [MenuSubItem](#menusubitem)
- [ScheduleMaintenance](#schedulemaintenance)

## MenuItem
**Physical table:** `OSUSR_fbw_MenuItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## MenuSubItem
**Physical table:** `OSUSR_fbw_MenuSubItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |
| MENUITEMID | int |  | YES | (NULL) |

## ScheduleMaintenance
**Physical table:** `OSUSR_fbw_ScheduleMaintenance`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| SCHEDULEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| OWNER | nvarchar | 50 | YES | ('') |
| LOGDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| STATUS | nvarchar | 50 | YES | ('') |
