# EPA_Taskbox

## Tables

- [Activity_Extension](#activity-extension)
- [MenuItem](#menuitem)
- [Seen_Activity](#seen-activity)

## Activity_Extension
**Physical table:** `OSUSR_lc9_Activity_Extension`  
**Description:** Extends the Activity entity with custom properties used only for Taskbox visualization  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ACTIVITYID | int |  | NO |  |
| HIDEDONE | bit |  | YES | ((0)) |
| HIDERELEASE | bit |  | YES | ((0)) |
| CUSTOMINSTRUCTIONS | nvarchar | 500 | YES | ('') |

## MenuItem
**Physical table:** `OSUSR_lc9_MenuItem`  
**Description:** Menu item to be used in menu web block parameters.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## Seen_Activity
**Physical table:** `OSUSR_lc9_Seen_Activity`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| USER_ID | int |  | YES | (NULL) |
| LAST_SEEN_ACTIVITY_ID | int |  | YES | (NULL) |
