# EPA_Taskbox

## Tables

- [Activity_Extension](#activity-extension)
- [MenuItem](#menuitem)
- [Seen_Activity](#seen-activity)

## Activity_Extension
**Physical table:** `OSUSR_LC9_ACTIVITY_EXTENSION`  
**Description:** Extends the Activity entity with custom properties used only for Taskbox visualization  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ACTIVITYID | int |  | NO |  |
| HIDEDONE | bit |  | YES | ((0)) |
| HIDERELEASE | bit |  | YES | ((0)) |
| CUSTOMINSTRUCTIONS | nvarchar | 500 | YES | ('') |

## MenuItem
**Physical table:** `OSUSR_LC9_MENUITEM`  
**Description:** Menu item to be used in menu web block parameters.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## Seen_Activity
**Physical table:** `OSUSR_LC9_SEEN_ACTIVITY`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| USER_ID | int |  | YES | (NULL) |
| LAST_SEEN_ACTIVITY_ID | int |  | YES | (NULL) |
