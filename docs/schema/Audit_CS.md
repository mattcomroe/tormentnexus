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

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ActivityHistory_Archive
**Physical table:** `OSUSR_2w6_ActivityHistory_Archive`  
**Description:** Contains ActivityHistory data older than X days  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ActivityHistoryContent
**Physical table:** `OSUSR_2w6_ActivityHistoryContent`  
**Description:** If the activity is an email, its content is saved here  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ActivityHistoryContent_Archive
**Physical table:** `OSUSR_2w6_ActivityHistoryContent_Archive`  
**Description:** Contains ActivityHistoryContent data older than X days  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ActivityHistoryFileStorage
**Physical table:** `OSUSR_2w6_ActivityHistoryFileStorage`  
**Description:** Contains all the files for each activity history  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ActivityHistoryFileStorage_Archive
**Physical table:** `OSUSR_2w6_ActivityHistoryFileStorage_Archive`  
**Description:** Contains all the files for each activity history  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ActivityType
**Physical table:** `OSUSR_2w6_ActivityType`  
**Description:** Possible Activity Types for the ActivityHistory  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ActivityTypeCategory
**Physical table:** `OSUSR_2w6_ActivityTypeCategory`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## EventToActivityTypeMapping
**Physical table:** `OSUSR_2w6_EventToActivityTypeMapping`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LeadActivityHistory
**Physical table:** `OSUSR_2w6_LeadActivityHistory`  
**Description:** Connects Activity History with the Lead  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LeadActivityHistory_Archive
**Physical table:** `OSUSR_2w6_LeadActivityHistory_Archive`  
**Description:** Connects Activity History with the Lead  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ReserveItAgainActivityHistory
**Physical table:** `OSUSR_2w6_ReserveItAgainAction`  
**Description:** History of activity for Reserve It Again section; logged on click "reserve" or "cancel" button  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ReserveItAgainActivityType
**Physical table:** `OSUSR_2w6_ReserveItAgainActionType`  
**Description:** Tyoes of actions for Reserve It Again; for SignIn, site property must be enabled in Schedule_BL  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ReserveItAgainViewHistory
**Physical table:** `OSUSR_2w6_ReserveItAgainView`  
**Description:** History of views for Reserve It Again section; logged on status check of locally stored classes (i.e., on CA homepage load/pull to refresh)  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._
