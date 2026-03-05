# ECT_Provider

## Tables

- [AppConfig](#appconfig)
- [Background](#background)
- [CallbackRule](#callbackrule)
- [DeviceColor](#devicecolor)
- [Feedback](#feedback)
- [FeedbackCookie](#feedbackcookie)
- [FeedbackExt](#feedbackext)
- [FeedbackExt_Mobile](#feedbackext-mobile)
- [FeedbackFrame](#feedbackframe)
- [FeedbackLocalInfo](#feedbacklocalinfo)
- [FeedbackMigrationQueue](#feedbackmigrationqueue)
- [FeedbackScreenshot](#feedbackscreenshot)
- [FeedbackSoundMessage](#feedbacksoundmessage)
- [FeedbackStatus](#feedbackstatus)
- [FeedbackWebpageContent](#feedbackwebpagecontent)
- [HttpStatusCode](#httpstatuscode)
- [LastFeedback](#lastfeedback)
- [MenuItem](#menuitem)
- [MenuSubItem](#menusubitem)
- [RequestBucket](#requestbucket)
- [Resource](#resource)
- [Rule](#rule)
- [Rule_eSpace](#rule-espace)
- [Rule_Group](#rule-group)
- [Rule_User](#rule-user)
- [Theme](#theme)
- [Theme_Espace](#theme-espace)
- [UserUsedECT](#userusedect)
- [WebpageContent](#webpagecontent)

## AppConfig
**Physical table:** `OSUSR_s41_AppConfig`  
**Description:** ECT configuration for an application. Each application can have ECT enabled or disabled. If the application has ECT enabled, it can be for all users, if GroupId is null, or for a group of users, if the GroupId is filled in.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| APPLICATIONID | int |  | NO |  |
| ECTENABLED | bit |  | YES | ((0)) |
| GROUPID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## Background
**Physical table:** `OSUSR_s41_Background`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## CallbackRule
**Physical table:** `OSUSR_s41_CallbackRule`  
**Description:** deprecated entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CALLBACK_URL_ID | int |  | YES | (NULL) |
| RULE_ID | int |  | YES | (NULL) |

## DeviceColor
**Physical table:** `OSUSR_s41_DeviceColor`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## Feedback
**Physical table:** `OSUSR_s41_Feedback`  
**Description:** Feedback sent by users  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| MOUSEX | nvarchar | 50 | YES | ('') |
| MOUSEY | nvarchar | 50 | YES | ('') |
| GEOMX | nvarchar | 50 | YES | ('') |
| GEOMY | nvarchar | 50 | YES | ('') |
| NODETYPE | nvarchar | 50 | YES | ('') |
| NODEXPATH | nvarchar | 2000 | YES | ('') |
| NODEOFFSETX | nvarchar | 50 | YES | ('') |
| NODEOFFSETY | nvarchar | 50 | YES | ('') |
| BROWSERTYPE | nvarchar | 300 | YES | ('') |
| BROWSERVERSION | nvarchar | 300 | YES | ('') |
| COMPATMODE | nvarchar | 50 | YES | ('') |
| HTML_GUID | nvarchar | 50 | YES | ('') |
| MESSAGE | nvarchar | 500 | YES | ('') |
| ESPACENAME | nvarchar | 50 | YES | ('') |
| ESPACEURL | nvarchar | 2000 | YES | ('') |
| DATETIMESUBMITTED | datetime |  | YES | ('1900-01-01 00:00:00') |
| USER_NAME | nvarchar | 100 | YES | ('') |
| USER_USERNAME | nvarchar | 100 | YES | ('') |
| USER_EMAIL | nvarchar | 100 | YES | ('') |
| GUID | nvarchar | 50 | YES | ('') |
| ORIGINALHTML | ntext | 1073741823 | YES | ('') |
| SCREENNAME | nvarchar | 2000 | YES | ('') |
| SCREENUID | nvarchar | 50 | YES | ('') |
| ESPACEUID | nvarchar | 50 | YES | ('') |

## FeedbackCookie
**Physical table:** `OSUSR_s41_FeedbackCookie`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FEEDBACK_ID | int |  | YES | (NULL) |
| COOKIEHEADER | ntext | 1073741823 | YES | ('') |

## FeedbackExt
**Physical table:** `OSUSR_s41_FeedbackExt`  
**Description:** Extension to the Feedback entity. Feedback is a public entity in a system component so we don't want to change it.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FEEDBACKID | int |  | YES | (NULL) |
| ENVIRONMENTUID | nvarchar | 40 | YES | ('') |
| REQUESTURL | nvarchar | -1 | YES | ('') |
| USERAGENTHEADER | nvarchar | 500 | YES | ('') |
| OPERATINGSYSTEMNAME | nvarchar | 150 | YES | ('') |
| DEVICEID | int |  | YES | (NULL) |
| FEEDBACKSTATUSID | int |  | YES | (NULL) |
| FEEDBACKSTATUSDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| STATUSCHANGEBY | int |  | YES | (NULL) |
| APPLICATIONID | int |  | YES | (NULL) |

## FeedbackExt_Mobile
**Physical table:** `OSUSR_s41_FeedbackExt_Mobile`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FEEDBACKID | int |  | YES | (NULL) |
| DEVICEMODEL | nvarchar | 50 | YES | ('') |

## FeedbackFrame
**Physical table:** `OSUSR_s41_FeedbackFrame`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FEEDBACKID | int |  | YES | (NULL) |
| ORIGINALHTML | ntext | 1073741823 | YES | ('') |
| URL | nvarchar | 2000 | YES | ('') |

## FeedbackLocalInfo
**Physical table:** `OSUSR_s41_FeedbackLocalInfo`  
**Description:** Entity to hold the status of the synch with other systems  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| USER_ID | int |  | YES | ((0)) |
| ESPACE_ID | int |  | YES | ((0)) |
| ISSYNCHED | bit |  | YES | ((0)) |
| FEEDBACK_ID | int |  | YES | (NULL) |
| HIDE | bit |  | YES | ((0)) |
| RETRYCONTENTFETCHMAXCOUNT | int |  | YES | ((0)) |
| READYTOSYNC | bit |  | YES | ((0)) |
| RETRYSYNCCOUNT | int |  | YES | ((0)) |
| SYNCDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| SYNCERRORMESSAGE | nvarchar | 500 | YES | ('') |
| SYNCERRORCODE | nvarchar | 50 | YES | ('') |
| ESPACE_UID | nvarchar | 50 | YES | ('') |

## FeedbackMigrationQueue
**Physical table:** `OSUSR_s41_FeedbackMigrationQueue`  
**Description:** Contains the IDs of all the Feedback records that need to be migrated to the latest version. Filled in at the start of a migration process.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FEEDBACKID | int |  | YES | (NULL) |
| ISMIGRATED | bit |  | YES | ((0)) |
| MIGRATIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |

## FeedbackScreenshot
**Physical table:** `OSUSR_s41_FeedbackScreenshot`  
**Description:** A screenshot of the users's screen when the feedback was provided. Screenshots are received through the JavaScript API  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FEEDBACKID | int |  | YES | (NULL) |
| IMAGEBINARY | varbinary | -1 | YES | (NULL) |
| IMAGEMIMEFORMAT | nvarchar | 150 | YES | ('') |

## FeedbackSoundMessage
**Physical table:** `OSUSR_s41_FeedbackSoundMessage`  
**Description:** Sound recorded when the feedback was provided. Sounds are received through the JavaScript API  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FEEDBACKID | int |  | YES | (NULL) |
| SOUNDBINARY | varbinary | -1 | YES | (NULL) |
| SOUNDMIMEFORMAT | nvarchar | 150 | YES | ('') |

## FeedbackStatus
**Physical table:** `OSUSR_s41_FeedbackStatus`  
**Description:** Each feedback can be either opened or closed  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## FeedbackWebpageContent
**Physical table:** `OSUSR_s41_FeedbackWebpageContent`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FEEDBACK_ID | int |  | YES | (NULL) |
| WEBPAGE_CONTENT_ID | int |  | YES | (NULL) |

## HttpStatusCode
**Physical table:** `OSUSR_s41_HttpStatusCode`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CODE | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## LastFeedback
**Physical table:** `OSUSR_s41_LastFeedback`  
**Description:** Save the last feedback seen by application and user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FEEDBACKID | int |  | YES | (NULL) |
| APPLICATIONID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |

## MenuItem
**Physical table:** `OSUSR_s41_MenuItem`  
**Description:** Menu item to be used in menu web block parameters.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## MenuSubItem
**Physical table:** `OSUSR_s41_MenuSubItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |
| MENUITEMID | int |  | YES | (NULL) |

## RequestBucket
**Physical table:** `OSUSR_s41_RequestBucket`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| IPADDRESS | nvarchar | 50 | YES | ('') |
| BUCKETCAPACITY | int |  | YES | ((0)) |
| EXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| FIRSTTIMESTAMP | datetime |  | YES | ('1900-01-01 00:00:00') |
| LASTTIMESTAMP | datetime |  | YES | ('1900-01-01 00:00:00') |
| USERID | int |  | YES | (NULL) |

## Resource
**Physical table:** `OSUSR_s41_Resource`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| MIMETYPE | nvarchar | 50 | YES | ('') |
| CONTENT | image | 2147483647 | YES | (NULL) |
| THEME_ID | int |  | YES | (NULL) |

## Rule
**Physical table:** `OSUSR_s41_Rule`  
**Description:** deprecated entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 200 | YES | ('') |
| FINISHED | bit |  | YES | ((0)) |
| ENABLED | bit |  | YES | ((0)) |
| ALL_ESPACES | bit |  | YES | ((0)) |
| ALL_GROUPS | bit |  | YES | ((0)) |
| ALLOW_NO_USER_GROUP | bit |  | YES | ((0)) |
| ALL_USERS | bit |  | YES | ((0)) |
| ALLOW_ANONYMOUS_USER | bit |  | YES | ((0)) |

## Rule_eSpace
**Physical table:** `OSUSR_s41_Rule_eSpace`  
**Description:** deprecated entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ESPACE_ID | int |  | YES | (NULL) |
| RULE_ID | int |  | YES | (NULL) |

## Rule_Group
**Physical table:** `OSUSR_s41_Rule_Group`  
**Description:** deprecated entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GROUP_ID | int |  | YES | (NULL) |
| RULE_ID | int |  | YES | (NULL) |

## Rule_User
**Physical table:** `OSUSR_s41_Rule_User`  
**Description:** deprecated entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| USER_ID | int |  | YES | (NULL) |
| RULE_ID | int |  | YES | (NULL) |

## Theme
**Physical table:** `OSUSR_s41_Theme`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| MAINCSSRESOURCE | int |  | YES | (NULL) |

## Theme_Espace
**Physical table:** `OSUSR_s41_Theme_Espace`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| THEMEID | int |  | YES | (NULL) |
| ESPACEID | int |  | YES | (NULL) |

## UserUsedECT
**Physical table:** `OSUSR_s41_UserUsedECT`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| USER | int |  | YES | ((0)) |
| ESPACE | int |  | YES | ((0)) |

## WebpageContent
**Physical table:** `OSUSR_s41_WebpageContent`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| CONTENTHASH | nvarchar | 256 | YES | ('') |
| MIME_TYPE | nvarchar | 50 | YES | ('') |
| CONTENT | image | 2147483647 | YES | (NULL) |
| URL | nvarchar | 2000 | YES | ('') |
