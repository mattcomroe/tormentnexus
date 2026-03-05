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
**Physical table:** `OSUSR_I35_AVATARRING`  
**Description:** Local storage containing static AvatarRing data  

_Column definitions not found in schema export._

## ClassFilter
**Physical table:** `OSUSR_I35_CLASSFILTER`  
**Description:** Saved class filters (program, coach) for filtering on schedule tab  

_Column definitions not found in schema export._

## ClassReservationStatusIds
**Physical table:** `OSUSR_I35_CLASSRESERVATIONSTATUSIDS`  
**Description:** Syncronized from Schedule to Returns list of static status ids for class reservation state  

_Column definitions not found in schema export._

## ClassWithReservationCounts
**Physical table:** `OSUSR_I35_CLASSWITHRESERVATIONCOUNTS`  
**Description:** Classes with Reservation Counts  

_Column definitions not found in schema export._

## ConfigSetting
**Physical table:** `OSUSR_I35_CONFIGSETTING1`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions not found in schema export._

## ConfigurationRecord
**Physical table:** `OSUSR_I35_CONFIGURATIONRECORD2`  
**Description:** Holds the configuration record for the given ID.  This record could be any data type listed in the DataType Static Entity  

_Column definitions not found in schema export._

## DataType
**Physical table:** `OSUSR_I35_DATATYPE2`  
**Description:** Enumerates the supported data types used to classify values (e.g., for typed configuration/settings).  

_Column definitions not found in schema export._

## Local_EmailConversations
**Physical table:** `OSUSR_I35_LOCAL_EMAILCONVERSATIONS`  
**Description:** JSON of the Firebase Cache  

_Column definitions not found in schema export._

## Local_EmailMessages
**Physical table:** `OSUSR_I35_LOCAL_EMAILMESSAGES`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions not found in schema export._

## Local_EmailPersonCacheContent
**Physical table:** `OSUSR_I35_LOCAL_EMAILPERSONCACHECONTENT`  
**Description:** JSON of the email person object  

_Column definitions not found in schema export._

## Local_FirebaseCacheContent
**Physical table:** `OSUSR_I35_LOCAL_FIREBASECACHECONTENT`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions not found in schema export._

## Local_FireBaseCollectionQuery
**Physical table:** `OSUSR_I35_LOCAL_FIREBASECOLLECTIONQUERY`  
**Description:** JSON of the Firebase Cache  

_Column definitions not found in schema export._

## Local_InAppChatConversation
**Physical table:** `OSUSR_I35_LOCAL_INAPPCHATCONVERSATION`  
**Description:** JSON of the Firebase Cache  

_Column definitions not found in schema export._

## Local_SenderEmailAddressByCustomerId
**Physical table:** `OSUSR_I35_LOCAL_SENDEREMAILADDRESSBYCUSTOMERID`  
**Description:** JSON of the list of EmailServiceSenderEmailAddress by customer id  

_Column definitions not found in schema export._

## Local_TwilioConversation
**Physical table:** `OSUSR_I35_LOCAL_TWILIOCONVERSATION`  
**Description:** JSON of the Firebase Cache  

_Column definitions not found in schema export._

## Local_TwilioMessages
**Physical table:** `OSUSR_I35_LOCAL_TWILIOCACHEMESSAGES`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions not found in schema export._

## LocalBirthdays
**Physical table:** `OSUSR_I35_LOCALBIRTHDAYS`  
**Description:** This Local Storage has the next 6 days of birthdays on the app, filtered by Customer Id  

_Column definitions not found in schema export._

## LocalBlobCache
**Physical table:** `OSUSR_I35_LOCALBLOBCACHE`  
**Description:** Once an image has a blob cache, we can just pull the blob instead of recreating it.  

_Column definitions not found in schema export._

## LocalCustomNavFeatures
**Physical table:** `OSUSR_I35_LOCALCUSTOMNAVFEATURES`  
**Description:** WodifyFeature, Media Library, External link etc. These are PK from the static entity, since we dont want static entities in mobile from the CS, we will use booleans to identify the PK  

_Column definitions not found in schema export._

## LocalCustomNavMenu
**Physical table:** `OSUSR_I35_LOCALCUSTOMNAVMENU`  
**Description:** Represents a customized menu item configured by a customer for use within the Wodify mobile application.  

_Column definitions not found in schema export._

## LocalCustomNavMenuType
**Physical table:** `OSUSR_I35_LOCALCUSTOMNAVMENUTYPE`  
**Description:** The static entity ID from {MenuType}, used as the primary key for lookup and filtering.  

_Column definitions not found in schema export._

## LocalInAppChatMessageCacheContent
**Physical table:** `OSUSR_I35_LOCALINAPPCHATMESSAGECACHECONTENT`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions not found in schema export._

## LocalLocations
**Physical table:** `OSUSR_I35_LOCALLOCATIONS`  

_Column definitions not found in schema export._

## LocalMediaCache
**Physical table:** `OSUSR_I35_LOCALMEDIACACHE`  
**Description:** Stores metadata and content references for media files (images) that are cached locally on the device for offline access or performance optimization.  

_Column definitions not found in schema export._

## LocalProgramsWorkout
**Physical table:** `OSUSR_I35_LOCALPROGRAMS`  

_Column definitions not found in schema export._

## LocalStaticTermV2
**Physical table:** `OSUSR_I35_LOCALSTATICTERMV2`  
**Description:** Entity that holds the Terms that are Customizable per Users and per Language (Locale)  

_Column definitions not found in schema export._

## MemberSettings
**Physical table:** `OSUSR_I35_MEMBERSETTINGS`  
**Description:** Contains all Settings for a specific Member (Client)  

_Column definitions not found in schema export._

## ObjectType
**Physical table:** `OSUSR_I35_OBJECTTYPE`  
**Description:** Static entity with Object Types  

_Column definitions not found in schema export._

## ReportType
**Physical table:** `OSUSR_I35_REPORTTYPE`  
**Description:** Static entity with types of content that can be reported  

_Column definitions not found in schema export._

## ReserveItAgainClass
**Physical table:** `OSUSR_I35_RESERVEITAGAINCLASS`  
**Description:** Classes for Reserve It Again  

_Column definitions not found in schema export._

## ServiceFilter
**Physical table:** `OSUSR_I35_SERVICEFILTER`  
**Description:** Saved Service Filter on schedule tab by service id  

_Column definitions not found in schema export._

## Settings
**Physical table:** `OSUSR_I35_SETTINGS`  
**Description:** contains default application settings.  

_Column definitions not found in schema export._

## TwilioBlacklistWords
**Physical table:** `OSUSR_I35_TWILIOBLACKLISTWORDS`  
**Description:** list of TwilioBlacklistWords  

_Column definitions not found in schema export._
