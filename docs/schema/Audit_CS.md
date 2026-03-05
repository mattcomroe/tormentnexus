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
**Physical table:** `OSUSR_2W6_ACTIVITYHISTORY`  
**Description:** Contains activities (user friendly logs) related to user or lead  

_Column definitions not found in schema export._

## ActivityHistory_Archive
**Physical table:** `OSUSR_2W6_ACTIVITYHISTORY_ARCHIVE`  
**Description:** Contains ActivityHistory data older than X days  

_Column definitions not found in schema export._

## ActivityHistoryContent
**Physical table:** `OSUSR_2W6_ACTIVITYHISTORYCONTENT`  
**Description:** If the activity is an email, its content is saved here  

_Column definitions not found in schema export._

## ActivityHistoryContent_Archive
**Physical table:** `OSUSR_2W6_ACTIVITYHISTORYCONTENT_ARCHIVE`  
**Description:** Contains ActivityHistoryContent data older than X days  

_Column definitions not found in schema export._

## ActivityHistoryFileStorage
**Physical table:** `OSUSR_2W6_ACTIVITYHISTORYFILESTORAGE`  
**Description:** Contains all the files for each activity history  

_Column definitions not found in schema export._

## ActivityHistoryFileStorage_Archive
**Physical table:** `OSUSR_2W6_ACTIVITYHISTORYFILESTORAGE_ARCHIVE`  
**Description:** Contains all the files for each activity history  

_Column definitions not found in schema export._

## ActivityType
**Physical table:** `OSUSR_2W6_ACTIVITYTYPE`  
**Description:** Possible Activity Types for the ActivityHistory  

_Column definitions not found in schema export._

## ActivityTypeCategory
**Physical table:** `OSUSR_2W6_ACTIVITYTYPECATEGORY`  

_Column definitions not found in schema export._

## EventToActivityTypeMapping
**Physical table:** `OSUSR_2W6_EVENTTOACTIVITYTYPEMAPPING`  

_Column definitions not found in schema export._

## LeadActivityHistory
**Physical table:** `OSUSR_2W6_LEADACTIVITYHISTORY`  
**Description:** Connects Activity History with the Lead  

_Column definitions not found in schema export._

## LeadActivityHistory_Archive
**Physical table:** `OSUSR_2W6_LEADACTIVITYHISTORY_ARCHIVE`  
**Description:** Connects Activity History with the Lead  

_Column definitions not found in schema export._

## ReserveItAgainActivityHistory
**Physical table:** `OSUSR_2W6_RESERVEITAGAINACTION`  
**Description:** History of activity for Reserve It Again section; logged on click "reserve" or "cancel" button  

_Column definitions not found in schema export._

## ReserveItAgainActivityType
**Physical table:** `OSUSR_2W6_RESERVEITAGAINACTIONTYPE`  
**Description:** Tyoes of actions for Reserve It Again; for SignIn, site property must be enabled in Schedule_BL  

_Column definitions not found in schema export._

## ReserveItAgainViewHistory
**Physical table:** `OSUSR_2W6_RESERVEITAGAINVIEW`  
**Description:** History of views for Reserve It Again section; logged on status check of locally stored classes (i.e., on CA homepage load/pull to refresh)  

_Column definitions not found in schema export._
