# EventPublisher_CS

## Tables

- [ActivityFeed](#activityfeed)
- [ActivityFeedEventPublisherActionMapping](#activityfeedeventpublisheractionmapping)
- [ActivityFeedParticipantType](#activityfeedparticipanttype)
- [CUDAction](#cudaction)
- [EntityAssociatedObjectMapping](#entityassociatedobjectmapping)
- [EntityListItemDetailsLabelMapping](#entitylistitemdetailslabelmapping)
- [EventPublisherAction](#eventpublisheraction)
- [EventPublisherApplicationSource](#eventpublisherapplicationsource)
- [EventPublisherBusinessEntity](#eventpublisherbusinessentity)
- [EventPublisherEntity](#eventpublisherentity)
- [FirestoreActivityFeedEntityMapping](#firestoreactivityfeedentitymapping)
- [FirestoreEntityAssociatedObjectMapping](#firestoreentityassociatedobjectmapping)
- [FirestoreEventPublisherEntity](#firestoreeventpublisherentity)
- [ForByEntityMapping](#forbyentitymapping)
- [ProcessStatus](#processstatus)
- [PublishEventBuffer](#publisheventbuffer)
- [QueuedHandlerLog](#queuedhandlerlog)
- [SEB_BPTWatchTable](#seb-bptwatchtable)
- [SEB_EventError](#seb-eventerror)
- [SEB_EventToSend](#seb-eventtosend)
- [Subscriber](#subscriber)

## ActivityFeed
**Physical table:** `OSUSR_57f_ActivityFeed1`  
**Description:** Feeds to hydrate in Firestore  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityFeedEventPublisherActionMapping
**Physical table:** `OSUSR_57f_ActivityFeedEventPublisherAction`  
**Description:** Cotains the mapping of Event Publish Actions to Activity Feeds to hydrate in Firestore  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ActivityFeedParticipantType
**Physical table:** `OSUSR_57f_ActivityFeedParticipantType`  
**Description:** [POC]  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## CUDAction
**Physical table:** `OSUSR_57f_CUDAction`  
**Description:** Create, Update, or Delete labels to be used when building Event JSON.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## EntityAssociatedObjectMapping
**Physical table:** `OSUSR_57f_EntityAssociatedObjectMapping`  
**Description:** (see entity diagram for details) Used to determine which additional object(s) should be parsed and included in the associated feeds for an event if a given entity related to an event. Ex: Event is published where a clients group ID is updated, we want to include the other group members in the associated feeds  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## EntityListItemDetailsLabelMapping
**Physical table:** `OSUSR_57f_EntityListItemDetailsLabelNameMapping`  
**Description:** Associates an EventPublisherEntity with the name of its label field name as used in the Updated  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## EventPublisherAction
**Physical table:** `OSUSR_57f_EventPublisherAction`  
**Description:** List of applications actions to report to Event Publisher  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## EventPublisherApplicationSource
**Physical table:** `OSUSR_57f_EventPublisherSource`  
**Description:** List of applications and systems to show where events are originating  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## EventPublisherBusinessEntity
**Physical table:** `OSUSR_57f_EventPublisherBusinessActions`  
**Description:** List of business entities (caetgories) to be referenced in EventPublisherActions entity  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## EventPublisherEntity
**Physical table:** `OSUSR_57f_EventPublisherEntity`  
**Description:** Outsystems entities in EventPublisher payloads.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## FirestoreActivityFeedEntityMapping
**Physical table:** `OSUSR_57f_FirestoreActivityFeedEntityMapping`  
**Description:** maps an FirestoreEventPublisherEntity to an ActivityFeed  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## FirestoreEntityAssociatedObjectMapping
**Physical table:** `OSUSR_57f_FirestoreEntityAssociatedObjectMapping`  
**Description:** (see entity diagram for details) Used to determine which additional object(s) should be parsed and included in the associated feeds for an event if a given entity related to an event. Ex: Event is published where task followers are added/updated, we want to include all followers in the associated feeds.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## FirestoreEventPublisherEntity
**Physical table:** `OSUSR_57f_FirestoreEventPublisherEntity`  
**Description:** Firestore counterpart of EventPublisherEntity  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ForByEntityMapping
**Physical table:** `OSUSR_57f_ForByEntityMapping`  
**Description:** [POC]maps ObjectType to EventPublisher Entity, only for "for" and "by"  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## ProcessStatus
**Physical table:** `OSUSR_57f_ProcessStatus`  
**Description:** Available statuses for an event being published.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PublishEventBuffer
**Physical table:** `OSUSR_57f_PublishEventBuffer`  
**Description:** For storing events as they are being processed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EVENTDETAIL | nvarchar | -1 | YES | ('') |
| RETRIES | int |  | YES | ((0)) |
| SUBSCRIBER | int |  | YES | (NULL) |
| RESPONSEMESSAGE | nvarchar | -1 | YES | ('') |
| RESPONSESTATUS | nvarchar | -1 | YES | ('') |
| PROCESSSTATUS | int |  | YES | (NULL) |
| NEXTRETRYAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| BATCHID | int |  | YES | ((0)) |
| HANDLERID | int |  | YES | ((0)) |

## QueuedHandlerLog
**Physical table:** `OSUSR_57f_QueuedHandlerLog`  
**Description:** Status log for queued events.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ERRORMESSAGE | nvarchar | 50 | YES | ('') |
| SUBSCRIBERID | bigint |  | YES | ((0)) |
| FROMSTATUSID | int |  | YES | (NULL) |
| TOSTATUSID | int |  | YES | (NULL) |

## SEB_BPTWatchTable
**Physical table:** `OSUSR_57f_SEB_BPTWatchTable`  
**Description:** Data about the processing of an Event via BPT.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## SEB_EventError
**Physical table:** `OSUSR_57f_SEB_EventError`  
**Description:** Error associated with an Event  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## SEB_EventToSend
**Physical table:** `OSUSR_57f_SEB_EventToSend`  
**Description:** Data associated with an Event to be processed for EventBridge.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## Subscriber
**Physical table:** `OSUSR_57f_Subscriber3`  
**Description:** Available subscribers to the event publisher system.  

_Table not present in the dev environment — schema unavailable. May exist in production only._
