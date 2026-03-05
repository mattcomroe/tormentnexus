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
**Physical table:** `OSUSR_57F_ACTIVITYFEED1`  
**Description:** Feeds to hydrate in Firestore  

_Column definitions not found in schema export._

## ActivityFeedEventPublisherActionMapping
**Physical table:** `OSUSR_57F_ACTIVITYFEEDEVENTPUBLISHERACTION`  
**Description:** Cotains the mapping of Event Publish Actions to Activity Feeds to hydrate in Firestore  

_Column definitions not found in schema export._

## ActivityFeedParticipantType
**Physical table:** `OSUSR_57F_ACTIVITYFEEDPARTICIPANTTYPE`  
**Description:** [POC]  

_Column definitions not found in schema export._

## CUDAction
**Physical table:** `OSUSR_57F_CUDACTION`  
**Description:** Create, Update, or Delete labels to be used when building Event JSON.  

_Column definitions not found in schema export._

## EntityAssociatedObjectMapping
**Physical table:** `OSUSR_57F_ENTITYASSOCIATEDOBJECTMAPPING`  
**Description:** (see entity diagram for details) Used to determine which additional object(s) should be parsed and included in the associated feeds for an event if a given entity related to an event. Ex: Event is published where a clients group ID is updated, we want to include the other group members in the associated feeds  

_Column definitions not found in schema export._

## EntityListItemDetailsLabelMapping
**Physical table:** `OSUSR_57F_ENTITYLISTITEMDETAILSLABELNAMEMAPPING`  
**Description:** Associates an EventPublisherEntity with the name of its label field name as used in the Updated  

_Column definitions not found in schema export._

## EventPublisherAction
**Physical table:** `OSUSR_57F_EVENTPUBLISHERACTION`  
**Description:** List of applications actions to report to Event Publisher  

_Column definitions not found in schema export._

## EventPublisherApplicationSource
**Physical table:** `OSUSR_57F_EVENTPUBLISHERSOURCE`  
**Description:** List of applications and systems to show where events are originating  

_Column definitions not found in schema export._

## EventPublisherBusinessEntity
**Physical table:** `OSUSR_57F_EVENTPUBLISHERBUSINESSACTIONS`  
**Description:** List of business entities (caetgories) to be referenced in EventPublisherActions entity  

_Column definitions not found in schema export._

## EventPublisherEntity
**Physical table:** `OSUSR_57F_EVENTPUBLISHERENTITY`  
**Description:** Outsystems entities in EventPublisher payloads.  

_Column definitions not found in schema export._

## FirestoreActivityFeedEntityMapping
**Physical table:** `OSUSR_57F_FIRESTOREACTIVITYFEEDENTITYMAPPING`  
**Description:** maps an FirestoreEventPublisherEntity to an ActivityFeed  

_Column definitions not found in schema export._

## FirestoreEntityAssociatedObjectMapping
**Physical table:** `OSUSR_57F_FIRESTOREENTITYASSOCIATEDOBJECTMAPPING`  
**Description:** (see entity diagram for details) Used to determine which additional object(s) should be parsed and included in the associated feeds for an event if a given entity related to an event. Ex: Event is published where task followers are added/updated, we want to include all followers in the associated feeds.  

_Column definitions not found in schema export._

## FirestoreEventPublisherEntity
**Physical table:** `OSUSR_57F_FIRESTOREEVENTPUBLISHERENTITY`  
**Description:** Firestore counterpart of EventPublisherEntity  

_Column definitions not found in schema export._

## ForByEntityMapping
**Physical table:** `OSUSR_57F_FORBYENTITYMAPPING`  
**Description:** [POC]maps ObjectType to EventPublisher Entity, only for "for" and "by"  

_Column definitions not found in schema export._

## ProcessStatus
**Physical table:** `OSUSR_57F_PROCESSSTATUS`  
**Description:** Available statuses for an event being published.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PublishEventBuffer
**Physical table:** `OSUSR_57F_PUBLISHEVENTBUFFER`  
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
**Physical table:** `OSUSR_57F_QUEUEDHANDLERLOG`  
**Description:** Status log for queued events.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ERRORMESSAGE | nvarchar | 50 | YES | ('') |
| SUBSCRIBERID | bigint |  | YES | ((0)) |
| FROMSTATUSID | int |  | YES | (NULL) |
| TOSTATUSID | int |  | YES | (NULL) |

## SEB_BPTWatchTable
**Physical table:** `OSUSR_57F_SEB_BPTWATCHTABLE`  
**Description:** Data about the processing of an Event via BPT.  

_Column definitions not found in schema export._

## SEB_EventError
**Physical table:** `OSUSR_57F_SEB_EVENTERROR`  
**Description:** Error associated with an Event  

_Column definitions not found in schema export._

## SEB_EventToSend
**Physical table:** `OSUSR_57F_SEB_EVENTTOSEND`  
**Description:** Data associated with an Event to be processed for EventBridge.  

_Column definitions not found in schema export._

## Subscriber
**Physical table:** `OSUSR_57F_SUBSCRIBER3`  
**Description:** Available subscribers to the event publisher system.  

_Column definitions not found in schema export._
