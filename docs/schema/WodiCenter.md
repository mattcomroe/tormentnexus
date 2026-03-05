# WodiCenter

## Tables

- [DeletedUser](#deleteduser)
- [DeploymentCard](#deploymentcard)
- [DeploymentRelease](#deploymentrelease)
- [DeploymentReleaseApplication](#deploymentreleaseapplication)
- [DeploymentReleaseInstance](#deploymentreleaseinstance)
- [DeploymentTask](#deploymenttask)
- [DeploymentTaskContent](#deploymenttaskcontent)
- [DeploymentTaskInstance](#deploymenttaskinstance)
- [DeploymentTaskType](#deploymenttasktype)
- [EntityScript](#entityscript)
- [Environment](#environment)
- [InvalidEmail](#invalidemail)
- [MenuItem](#menuitem)
- [MenuSubItem](#menusubitem)
- [Report_Log_Error](#report-log-error)
- [Report_Log_Error_Detail](#report-log-error-detail)
- [Report_Log_Error_GroupedMessages](#report-log-error-groupedmessages)
- [ScrubBinary](#scrubbinary)
- [ScrubControl](#scrubcontrol)
- [ScrubItemControl](#scrubitemcontrol)
- [ScrubItems](#scrubitems)
- [ScrubItemStatus](#scrubitemstatus)
- [TenantDelete_Control](#tenantdelete-control)
- [Zone](#zone)

## DeletedUser
**Physical table:** `OSUSR_82w_DeletedUser`  
**Description:** Contains Backed up OSSYS_USER data  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANT_ID | int |  | NO | ((0)) |
| NAME | nvarchar | 256 | YES | ('') |
| USERNAME | nvarchar | 250 | YES | ('') |
| PASSWORD | nvarchar | 256 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| MOBILEPHONE | nvarchar | 20 | YES | ('') |
| EXTERNAL_ID | nvarchar | 36 | YES | ('') |
| CREATION_DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| LAST_LOGIN | datetime |  | YES | ('1900-01-01 00:00:00') |
| OLDUSERID | bigint |  | YES | ((0)) |
| HASLOGGEDINBEFORE | bit |  | YES | ((0)) |
| LOCATIONID | int |  | YES | ((0)) |
| GYMPROGRAMID | int |  | YES | ((0)) |
| ISINITIALWELCOMEEMAILSENT | bit |  | YES | ((0)) |
| ISSUSPENDED | bit |  | YES | ((0)) |
| ATHLETESTATUSPICKLISTVALUEID | int |  | YES | ((0)) |
| LEADID | int |  | YES | ((0)) |
| LEADSOURCEPICKLISTVALUEID | int |  | YES | ((0)) |
| REFERRINGUSER | int |  | YES | ((0)) |
| CONVERTEDFROMLEAD | bit |  | YES | ((0)) |
| MEMBERDEACTIVATIONREASONID | int |  | YES | ((0)) |
| NUTRITIONCOACHID | int |  | YES | ((0)) |
| UOMWEIGHTID | int |  | YES | ((0)) |
| UOMDISTANCEID | int |  | YES | ((0)) |
| BALANCEDUE | decimal |  | YES | ((0)) |
| UNIQUEKEY | nvarchar | 25 | YES | ('') |
| YUBICOSECURITYKEY | nvarchar | 12 | YES | ('') |
| MASSEMAILSUBSCRIBED | bit |  | YES | ((0)) |
| MEMBERSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TAXIDENTIFICATIONNUMBER | nvarchar | 20 | YES | ('') |
| LASTATTENDANCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| SUBSCRIBETOSMSNOTIFICATIONS | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILCOMMYPERF | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILCOMOTHERPERF | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILLIKEMYPERF | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILLIKEMYCOM | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILLIKEOTHERPERF | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILJOURNALTOREVIE | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILJOURNALTOREAD | bit |  | YES | ((0)) |
| NOTIFYVIAEMAILFREQUENCY | int |  | YES | ((0)) |
| INAPP_MOBILECLASSSIGNIN | bit |  | YES | ((0)) |
| INAPP_LIKEMYPERFORMANCE | bit |  | YES | ((0)) |
| INAPP_LIKEMYCOMMENT | bit |  | YES | ((0)) |
| INAPP_COMMYPERFORMANCE | bit |  | YES | ((0)) |
| INAPP_COMOTHERPERFORMANCE | bit |  | YES | ((0)) |
| INAPP_JOURNALUNREADREVIEWS | bit |  | YES | ((0)) |
| INAPP_JOURNALAWAITINGREVIEW | bit |  | YES | ((0)) |
| INAPP_SIGNWAIVER | bit |  | YES | ((0)) |
| SMSSUBSCRIPTIONSTATUSID | int |  | YES | ((0)) |
| UNVIEWEDNOTIFICATIONSCOUNT | bigint |  | YES | ((0)) |
| ISDEFAULTCOMMENTPRIVATE | bit |  | YES | ((0)) |
| ISBIRTHDAYPRIVATE | bit |  | YES | ((0)) |
| ALLOWCOMMENTSONMYWHITEBOARD | bit |  | YES | ((0)) |
| SUBSCRIBEONCOMMENT | bit |  | YES | ((0)) |
| ALLOWEDTOCOMMENT | bit |  | YES | ((0)) |
| ISWODIFYWHITEBOARDPRIVATE | bit |  | YES | ((0)) |
| WODIFYPUBLICCOMMENTSVISIBLE | bit |  | YES | ((0)) |
| WODIFYPUBLICBIRTHDAYVISIBLE | bit |  | YES | ((0)) |
| WODIFYPUBLICPICTUREVISIBLE | bit |  | YES | ((0)) |
| GLOBALUSERID | int |  | YES | ((0)) |
| TENANTID | int |  | YES | ((0)) |
| ISDEFAULT | bit |  | YES | ((0)) |
| PRODUCTID | int |  | YES | ((0)) |

## DeploymentCard
**Physical table:** `OSUSR_82w_DeploymentCard`  
**Description:** Contains all Deployment card number for each Release  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DEPLOYMENTRELEASEID | bigint |  | YES | (NULL) |
| CARDNAME | nvarchar | 50 | YES | ('') |

## DeploymentRelease
**Physical table:** `OSUSR_82w_DeploymentRelease`  
**Description:** Contains a record for each release number / product  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| RELEASENUMBER | nvarchar | 50 | YES | ('') |
| ARCHIVEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| RELEASEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |

## DeploymentReleaseApplication
**Physical table:** `OSUSR_82w_DeploymentReleaseApplication`  
**Description:** Contains all the applications that are related with this product's release  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DEPLOYMENTRELEASEID | bigint |  | YES | (NULL) |
| APPLICATIONKEY | nvarchar | 150 | YES | ('') |
| APPLICATIONVERSIONKEY | nvarchar | 150 | YES | ('') |
| APPLICATIONNAME | nvarchar | 150 | YES | ('') |
| TAGVERSION | nvarchar | 50 | YES | ('') |
| TAGVERSIONINDEV | nvarchar | 50 | YES | ('') |
| TAGVERSIONINTST | nvarchar | 50 | YES | ('') |
| TAGVERSIONINSTG | nvarchar | 50 | YES | ('') |

## DeploymentReleaseInstance
**Physical table:** `OSUSR_82w_DeploymentReleaseInstance`  
**Description:** Contains Instances of running or runned Releases  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DEPLOYMENTRELEASEID | bigint |  | YES | (NULL) |
| ENVIRONMENTID | int |  | YES | (NULL) |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| ISPOSTDEPLOYMENT | bit |  | YES | ((0)) |
| STARTEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |

## DeploymentTask
**Physical table:** `OSUSR_82w_DeploymentTask`  
**Description:** Contains all Deployment tasks  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DEPLOYMENTRELEASEID | bigint |  | YES | (NULL) |
| DEPLOYMENTCARDID | bigint |  | YES | (NULL) |
| ISPOSTDEPLOYMENT | bit |  | YES | ((0)) |
| DEPLOYMENTTASKTYPEID | int |  | YES | (NULL) |
| ENVIRONMENTID | int |  | YES | (NULL) |
| FILENAME | nvarchar | 100 | YES | ('') |
| ESPACEID | int |  | YES | (NULL) |
| ESPACENAME | nvarchar | 50 | YES | ('') |
| ZONEID | int |  | YES | (NULL) |
| SITEPROPERTY | int |  | YES | (NULL) |
| SITEPROPERTYVALUE | nvarchar | 500 | YES | ('') |
| SOAPRESTNAME | nvarchar | 100 | YES | ('') |
| SOAPRESTEFFECTIVEURL | nvarchar | 500 | YES | ('') |
| SOAPRESTEFFECTIVEUSERNAME | nvarchar | 500 | YES | ('') |
| SOAPRESTEFFECTIVEPASSWORD | nvarchar | 500 | YES | ('') |
| TIMER | int |  | YES | (NULL) |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ZONENAME | nvarchar | 150 | YES | ('') |
| SITEPROPERTYNAME | nvarchar | 150 | YES | ('') |
| TIMERNAME | nvarchar | 150 | YES | ('') |

## DeploymentTaskContent
**Physical table:** `OSUSR_82w_DeploymentTaskContent`  
**Description:** When its a script or its an "other" task type that requires an attachment, the binary will stay here. It also has the "Other" Text  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| DEPLOYMENTTASKID | bigint |  | NO |  |
| BINARY | varbinary | -1 | YES | (NULL) |
| FILETYPE | nvarchar | 50 | YES | ('') |
| OTHERDESCRIPTION | nvarchar | -1 | YES | ('') |

## DeploymentTaskInstance
**Physical table:** `OSUSR_82w_DeploymentTaskInstance`  
**Description:** Contains Instances of running or runned tasks  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DEPLOYMENTRELEASEINSTANCEID | bigint |  | YES | (NULL) |
| DEPLOYMENTTASKID | bigint |  | YES | (NULL) |
| ISDONE | bit |  | YES | ((0)) |

## DeploymentTaskType
**Physical table:** `OSUSR_82w_DeploymentTaskType`  
**Description:** Contains all possible Task types to run as post or pre deployment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## EntityScript
**Physical table:** `OSUSR_82w_EntityScript`  
**Description:** Contains the script to run to remove tables  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ENTITYNAME | nvarchar | 500 | YES | ('') |
| SCRIPT | nvarchar | -1 | YES | ('') |

## Environment
**Physical table:** `OSUSR_82w_Environment`  
**Description:** Contains a record per needed environment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| URL | nvarchar | 50 | YES | ('') |
| NAMEINLIFETIME | nvarchar | 50 | YES | ('') |

## InvalidEmail
**Physical table:** `OSUSR_82w_InvalidEmail`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TYPE | nvarchar | 50 | YES | ('') |
| TYPEID | int |  | YES | ((0)) |
| TENANTID | int |  | YES | (NULL) |
| NAME | nvarchar | 50 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |

## MenuItem
**Physical table:** `OSUSR_48h_MenuItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CAPTION | nvarchar | 50 | YES | ('') |
| URL | nvarchar | 50 | YES | ('') |

## MenuSubItem
**Physical table:** `OSUSR_48h_MenuSubItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |
| MENUITEMID | int |  | YES | (NULL) |

## Report_Log_Error
**Physical table:** `OSUSR_82w_Report_Log_Error`  
**Description:** Contains the most common error logs reported  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| DAY | datetime |  | YES | ('1900-01-01 00:00:00') |
| TOTALOCCURRENCES | int |  | YES | ((0)) |
| TOTALINTEGRATIONOCCURRENCES | int |  | YES | ((0)) |
| TOTALMOBILEREQUESTSOCCURREN | int |  | YES | ((0)) |
| TOTALPLATFORMOCCURRENCES | int |  | YES | ((0)) |

## Report_Log_Error_Detail
**Physical table:** `OSUSR_82w_Report_Log_Error_Detail`  
**Description:** Contains the most common error logs reported  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| REPORTLOGERRORID | int |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 2000 | YES | ('') |
| NUMBEROFOCCURRENCES | int |  | YES | ((0)) |
| LOG_DETAILL_AGREGATORID | int |  | YES | (NULL) |
| ISAGREGATOR | bit |  | YES | ((0)) |
| ISNEW | bit |  | YES | ((0)) |
| ISINTEGRATIONERROR | bit |  | YES | ((0)) |
| ISMOBILEERROR | bit |  | YES | ((0)) |

## Report_Log_Error_GroupedMessages
**Physical table:** `OSUSR_82w_Report_Log_Error_GroupedMessages`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| MESSAGE | nvarchar | 500 | YES | ('') |
| ISPLATFORM | bit |  | YES | ((0)) |

## ScrubBinary
**Physical table:** `OSUSR_82w_ScrubBinary`  
**Description:** Contains the binary file to be used for scrub scripts  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| BINARYCONTENT | varbinary | -1 | YES | (NULL) |
| FILENAME | nvarchar | 500 | YES | ('') |
| MIMETYPE | nvarchar | 50 | YES | ('') |

## ScrubControl
**Physical table:** `OSUSR_82w_ScrubControl`  
**Description:** Information about the scrub execution (Pre Scrub or Scrub)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| IGNOREERRORS | bit |  | YES | ((0)) |

## ScrubItemControl
**Physical table:** `OSUSR_82w_ScrubItemControl`  
**Description:** Information about the scrub's item execution (Pre Scrub or Scrub)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SCRUBCONTROLID | bigint |  | YES | (NULL) |
| SCRUBITEMID | int |  | YES | (NULL) |
| SCRUBSTATUSID | int |  | YES | (NULL) |
| NUMBEROFRECORDS | int |  | YES | ((0)) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ERRORMSG | nvarchar | 1000 | YES | ('') |

## ScrubItems
**Physical table:** `OSUSR_82w_ScrubItems`  
**Description:** Actions that will be executed in scrubbing executions  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| DESCRIPTION | nvarchar | 200 | YES | ('') |
| ISPRESCRUB | bit |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| DOWNLOADFILE | bit |  | YES | ((0)) |

## ScrubItemStatus
**Physical table:** `OSUSR_82w_ScrubItemStatus`  
**Description:** Scrub Item's status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## TenantDelete_Control
**Physical table:** `OSUSR_82w_TenantDelete_Control`  
**Description:** list of Tenants to be deleted togheter with all tenant data  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANTID | int |  | YES | (NULL) |

## Zone
**Physical table:** `OSUSR_82w_Zone`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
