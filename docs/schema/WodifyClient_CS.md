# WodifyClient_CS

## Tables

- [AvatarRing](#avatarring)
- [ClassFilter](#classfilter)
- [ClassReservationStatusIds](#classreservationstatusids)
- [ClassWithReservationCounts](#classwithreservationcounts)
- [ConfigSetting](#configsetting)
- [ConfigurationRecord](#configurationrecord)
- [DataType](#datatype)
- [Local_EmailConversations](#local-emailconversations)
- [Local_EmailMessages](#local-emailmessages)
- [Local_EmailPersonCacheContent](#local-emailpersoncachecontent)
- [Local_FirebaseCacheContent](#local-firebasecachecontent)
- [Local_FireBaseCollectionQuery](#local-firebasecollectionquery)
- [Local_InAppChatConversation](#local-inappchatconversation)
- [Local_SenderEmailAddressByCustomerId](#local-senderemailaddressbycustomerid)
- [Local_TwilioConversation](#local-twilioconversation)
- [Local_TwilioMessages](#local-twiliomessages)
- [LocalBirthdays](#localbirthdays)
- [LocalBlobCache](#localblobcache)
- [LocalCustomNavFeatures](#localcustomnavfeatures)
- [LocalCustomNavMenu](#localcustomnavmenu)
- [LocalCustomNavMenuType](#localcustomnavmenutype)
- [LocalInAppChatMessageCacheContent](#localinappchatmessagecachecontent)
- [LocalLocations](#locallocations)
- [LocalMediaCache](#localmediacache)
- [LocalProgramsWorkout](#localprogramsworkout)
- [LocalStaticTermV2](#localstatictermv2)
- [MemberSettings](#membersettings)
- [ObjectType](#objecttype)
- [ReportType](#reporttype)
- [ReserveItAgainClass](#reserveitagainclass)
- [ServiceFilter](#servicefilter)
- [Settings](#settings)
- [TwilioBlacklistWords](#twilioblacklistwords)

## AvatarRing
**Physical table:** `OSUSR_i35_AvatarRing`  
**Description:** Local storage containing static AvatarRing data  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClassFilter
**Physical table:** `OSUSR_i35_ClassFilter`  
**Description:** Saved class filters (program, coach) for filtering on schedule tab  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClassReservationStatusIds
**Physical table:** `OSUSR_i35_ClassReservationStatusIds`  
**Description:** Syncronized from Schedule to Returns list of static status ids for class reservation state  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ClassWithReservationCounts
**Physical table:** `OSUSR_i35_ClassWithReservationCounts`  
**Description:** Classes with Reservation Counts  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ConfigSetting
**Physical table:** `OSUSR_i35_ConfigSetting1`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ConfigurationRecord
**Physical table:** `OSUSR_i35_ConfigurationRecord2`  
**Description:** Holds the configuration record for the given ID.  This record could be any data type listed in the DataType Static Entity  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## DataType
**Physical table:** `OSUSR_i35_DataType2`  
**Description:** Enumerates the supported data types used to classify values (e.g., for typed configuration/settings).  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_EmailConversations
**Physical table:** `OSUSR_i35_Local_EmailConversations`  
**Description:** JSON of the Firebase Cache  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_EmailMessages
**Physical table:** `OSUSR_i35_Local_EmailMessages`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_EmailPersonCacheContent
**Physical table:** `OSUSR_i35_Local_EmailPersonCacheContent`  
**Description:** JSON of the email person object  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_FirebaseCacheContent
**Physical table:** `OSUSR_i35_Local_FirebaseCacheContent`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_FireBaseCollectionQuery
**Physical table:** `OSUSR_i35_Local_FireBaseCollectionQuery`  
**Description:** JSON of the Firebase Cache  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_InAppChatConversation
**Physical table:** `OSUSR_i35_Local_InAppChatConversation`  
**Description:** JSON of the Firebase Cache  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_SenderEmailAddressByCustomerId
**Physical table:** `OSUSR_i35_Local_SenderEmailAddressByCustomerId`  
**Description:** JSON of the list of EmailServiceSenderEmailAddress by customer id  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_TwilioConversation
**Physical table:** `OSUSR_i35_Local_TwilioConversation`  
**Description:** JSON of the Firebase Cache  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Local_TwilioMessages
**Physical table:** `OSUSR_i35_Local_TwilioCacheMessages`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalBirthdays
**Physical table:** `OSUSR_i35_LocalBirthdays`  
**Description:** This Local Storage has the next 6 days of birthdays on the app, filtered by Customer Id  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalBlobCache
**Physical table:** `OSUSR_i35_LocalBlobCache`  
**Description:** Once an image has a blob cache, we can just pull the blob instead of recreating it.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalCustomNavFeatures
**Physical table:** `OSUSR_i35_LocalCustomNavFeatures`  
**Description:** WodifyFeature, Media Library, External link etc. These are PK from the static entity, since we dont want static entities in mobile from the CS, we will use booleans to identify the PK  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalCustomNavMenu
**Physical table:** `OSUSR_i35_LocalCustomNavMenu`  
**Description:** Represents a customized menu item configured by a customer for use within the Wodify mobile application.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalCustomNavMenuType
**Physical table:** `OSUSR_i35_LocalCustomNavMenuType`  
**Description:** The static entity ID from {MenuType}, used as the primary key for lookup and filtering.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalInAppChatMessageCacheContent
**Physical table:** `OSUSR_i35_LocalInAppChatMessageCacheContent`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalLocations
**Physical table:** `OSUSR_i35_LocalLocations`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalMediaCache
**Physical table:** `OSUSR_i35_LocalMediaCache`  
**Description:** Stores metadata and content references for media files (images) that are cached locally on the device for offline access or performance optimization.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalProgramsWorkout
**Physical table:** `OSUSR_i35_LocalPrograms`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LocalStaticTermV2
**Physical table:** `OSUSR_i35_LocalStaticTermV2`  
**Description:** Entity that holds the Terms that are Customizable per Users and per Language (Locale)  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## MemberSettings
**Physical table:** `OSUSR_i35_MemberSettings`  
**Description:** Contains all Settings for a specific Member (Client)  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ObjectType
**Physical table:** `OSUSR_i35_ObjectType`  
**Description:** Static entity with Object Types  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ReportType
**Physical table:** `OSUSR_i35_ReportType`  
**Description:** Static entity with types of content that can be reported  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ReserveItAgainClass
**Physical table:** `OSUSR_i35_ReserveItAgainClass`  
**Description:** Classes for Reserve It Again  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ServiceFilter
**Physical table:** `OSUSR_i35_ServiceFilter`  
**Description:** Saved Service Filter on schedule tab by service id  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Settings
**Physical table:** `OSUSR_i35_Settings`  
**Description:** contains default application settings.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## TwilioBlacklistWords
**Physical table:** `OSUSR_i35_TwilioBlacklistWords`  
**Description:** list of TwilioBlacklistWords  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._
