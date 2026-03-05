# Notification_CS

## Tables

- [ClientNotificationSettings](#clientnotificationsettings)

## ClientNotificationSettings
**Physical table:** `OSUSR_x9o_ClientNotificationSettings`  
**Description:** Contains all notification settings for the specified client  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PUSHNOTSOCIALCOMREPTAGS | bit |  | YES | ((0)) |
| PUSHNOTSOCIALLIKES | bit |  | YES | ((0)) |
| PUSHNOTCLASSFIRSTREPLYWL | bit |  | YES | ((0)) |
| PUSHNOTCLASSORDEREDWL | bit |  | YES | ((0)) |
| PUSHNOTCLASSCANCEL | bit |  | YES | ((0)) |
| PUSHNOTCLASSRESCHEDULE | bit |  | YES | ((0)) |
| PUSHNOTAPPTUPCOMINGREMIND | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PUSHNOTTASKASSIGNMENT | bit |  | YES | ((1)) |
| PUSHNOTTASKMENTION | bit |  | YES | ((1)) |
| PUSHNOTTASKCOMPLETED | bit |  | YES | ((1)) |
| PUSHNOTCHATRECIEVED | bit |  | YES | ((1)) |
| PUSHNOTSMS | bit |  | YES | ((1)) |
| PUSHNOTLOCATIONCHATRECIEVED | bit |  | YES | ((1)) |
| PUSHNOTCUSTOMERCHATRECIEVED | bit |  | YES | ((1)) |
