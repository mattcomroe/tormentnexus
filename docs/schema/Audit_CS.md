# Audit_CS

## Tables

- [ActivityHistory](#activityhistory)
- [ActivityHistory_Archive](#activityhistory-archive)
- [ActivityHistoryContent](#activityhistorycontent)
- [ActivityHistoryContent_Archive](#activityhistorycontent-archive)
- [ActivityHistoryFileStorage](#activityhistoryfilestorage)
- [ActivityHistoryFileStorage_Archive](#activityhistoryfilestorage-archive)
- [ActivityType](#activitytype)
- [ActivityTypeCategory](#activitytypecategory)
- [EventToActivityTypeMapping](#eventtoactivitytypemapping)
- [LeadActivityHistory](#leadactivityhistory)
- [LeadActivityHistory_Archive](#leadactivityhistory-archive)
- [ReserveItAgainActivityHistory](#reserveitagainactivityhistory)
- [ReserveItAgainActivityType](#reserveitagainactivitytype)
- [ReserveItAgainViewHistory](#reserveitagainviewhistory)

## ActivityHistory
**Physical table:** `OSUSR_2w6_ActivityHistory`  
**Description:** Contains activities (user friendly logs) related to user or lead  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityHistory_Archive
**Physical table:** `OSUSR_2w6_ActivityHistory_Archive`  
**Description:** Contains ActivityHistory data older than X days  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityHistoryContent
**Physical table:** `OSUSR_2w6_ActivityHistoryContent`  
**Description:** If the activity is an email, its content is saved here  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityHistoryContent_Archive
**Physical table:** `OSUSR_2w6_ActivityHistoryContent_Archive`  
**Description:** Contains ActivityHistoryContent data older than X days  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityHistoryFileStorage
**Physical table:** `OSUSR_2w6_ActivityHistoryFileStorage`  
**Description:** Contains all the files for each activity history  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityHistoryFileStorage_Archive
**Physical table:** `OSUSR_2w6_ActivityHistoryFileStorage_Archive`  
**Description:** Contains all the files for each activity history  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityType
**Physical table:** `OSUSR_2w6_ActivityType`  
**Description:** Possible Activity Types for the ActivityHistory  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityTypeCategory
**Physical table:** `OSUSR_2w6_ActivityTypeCategory`  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## EventToActivityTypeMapping
**Physical table:** `OSUSR_2w6_EventToActivityTypeMapping`  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## LeadActivityHistory
**Physical table:** `OSUSR_2w6_LeadActivityHistory`  
**Description:** Connects Activity History with the Lead  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## LeadActivityHistory_Archive
**Physical table:** `OSUSR_2w6_LeadActivityHistory_Archive`  
**Description:** Connects Activity History with the Lead  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ReserveItAgainActivityHistory
**Physical table:** `OSUSR_2w6_ReserveItAgainAction`  
**Description:** History of activity for Reserve It Again section; logged on click "reserve" or "cancel" button  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ReserveItAgainActivityType
**Physical table:** `OSUSR_2w6_ReserveItAgainActionType`  
**Description:** Tyoes of actions for Reserve It Again; for SignIn, site property must be enabled in Schedule_BL  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ReserveItAgainViewHistory
**Physical table:** `OSUSR_2w6_ReserveItAgainView`  
**Description:** History of views for Reserve It Again section; logged on status check of locally stored classes (i.e., on CA homepage load/pull to refresh)  

_Table not present in the dev environment — schema unavailable. May exist in production only._
