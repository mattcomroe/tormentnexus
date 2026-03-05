# W_Social_SH_CS

## Tables

- [UserSettingNotification](#usersettingnotification)
- [UserSettingSocial](#usersettingsocial)

## UserSettingNotification
**Physical table:** `OSUSR_72O_USERSETTINGNOTIFICATION`  
**Description:** Data about a users notification settings and preferences  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| SUBSCRIBETOSMSNOTIFICATIONS | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILCOMMYPERF | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILCOMOTHERPERF | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILLIKEMYPERF | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILLIKEMYCOM | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILLIKEOTHERPERF | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILJOURNALTOREVIE | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILJOURNALTOREAD | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILFREQUENCY | int |  | YES | (NULL) |
| MOBILENOTIFYCLASSSIGNIN | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| SMSSUBSCRIPTIONSTATUSID | int |  | YES | (NULL) |
| INAPP_MOBILECLASSSIGNIN | bit |  | YES | ((0)) |
| INAPP_LIKEMYPERFORMANCE | bit |  | YES | ((0)) |
| INAPP_LIKEMYCOMMENT | bit |  | YES | ((0)) |
| INAPP_COMMYPERFORMANCE | bit |  | YES | ((0)) |
| INAPP_COMOTHERPERFORMANCE | bit |  | YES | ((0)) |
| INAPP_JOURNALUNREADREVIEWS | bit |  | YES | ((0)) |
| INAPP_JOURNALAWAITINGREVIEW | bit |  | YES | ((0)) |
| INAPP_SIGNWAIVER | bit |  | YES | ((0)) |
| UNVIEWEDNOTIFICATIONSCOUNT | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SMSSUBSCRIBEDTOLLFREE | bit |  | YES | ((0)) |

## UserSettingSocial
**Physical table:** `OSUSR_72O_USERSETTINGSOCIAL`  
**Description:** Contains end user social settings and preferences  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| ISDEFAULTCOMMENTPRIVATE | bit |  | YES | ((0)) |
| ISBIRTHDAYPRIVATE | bit |  | YES | ((0)) |
| ISWODIFYWHITEBOARDPRIVATE | bit |  | YES | ((0)) |
| ALLOWCOMMENTSONMYWHITEBOARD | bit |  | YES | ((0)) |
| SUBSCRIBEONCOMMENT | bit |  | YES | ((0)) |
| ALLOWEDTOCOMMENT | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| WODIFYPUBLICCOMMENTSVISIBLE | bit |  | YES | ((0)) |
| WODIFYPUBLICBIRTHDAYVISIBLE | bit |  | YES | ((0)) |
| WODIFYPUBLICPICTUREVISIBLE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
