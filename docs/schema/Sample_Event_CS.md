# Sample_Event_CS

## Tables

- [Event](#event)
- [EventAttendee](#eventattendee)
- [EventColor](#eventcolor)
- [EventSession](#eventsession)
- [EventSessionSpeaker](#eventsessionspeaker)
- [Hours](#hours)
- [Image](#image)
- [Minutes](#minutes)
- [Rating](#rating)
- [SessionCategory](#sessioncategory)
- [Speaker](#speaker)

## Event
**Physical table:** `OSUSR_wu5_Event`  
**Description:** Entity to hold all information regarding the Events  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 200 | YES | ('') |
| CITY | nvarchar | 100 | YES | ('') |
| ADDRESS | nvarchar | 255 | YES | ('') |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| IMAGEID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## EventAttendee
**Physical table:** `OSUSR_wu5_EventAttendee`  
**Description:** Table to hold a relation of an attendee for a certain Session  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EVENTID | bigint |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## EventColor
**Physical table:** `OSUSR_wu5_Color`  
**Description:** Collection of curated colors which match with the respective CSS classes  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| COLOR | nvarchar | 50 | NO |  |

## EventSession
**Physical table:** `OSUSR_wu5_EventSession`  
**Description:** Table to hold a definition of an Session.Note: Must use name as "EventSession" to avoid troubleshooting related with Session systems variable.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EVENTID | bigint |  | YES | (NULL) |
| TITLE | nvarchar | 200 | YES | ('') |
| SUBTITLE | nvarchar | 200 | YES | ('') |
| SUMMARY | nvarchar | 2000 | YES | ('') |
| SESSIONCATEGORYID | int |  | YES | (NULL) |
| EVENTSESSIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| EVENTSESSIONTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| DURATIONHOUR | nvarchar | 50 | YES | (NULL) |
| DURATIONMINUTES | nvarchar | 50 | YES | (NULL) |
| ISBREAK | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ISHIGHLIGHT | bit |  | YES | ((0)) |
| REMOTESESSIONURL | nvarchar | 250 | YES | ('') |

## EventSessionSpeaker
**Physical table:** `OSUSR_wu5_EventSessionSpeaker`  
**Description:** Table to hold a relation of an speakers for a certain Session  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EVENTSESSIONID | bigint |  | YES | (NULL) |
| SPEAKERID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## Hours
**Physical table:** `OSUSR_wu5_Hours`  
**Description:** Collection of Hours  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| VALUE | int |  | YES | ((0)) |

## Image
**Physical table:** `OSUSR_wu5_Image`  
**Description:** Entity to store images on the database  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FILENAME | nvarchar | 250 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| FILETYPE | nvarchar | 250 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Minutes
**Physical table:** `OSUSR_wu5_Minutes`  
**Description:** Collection of Minutes  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| VALUE | int |  | YES | ((0)) |

## Rating
**Physical table:** `OSUSR_wu5_Rating`  
**Description:** Entity to hold all information regarding ratings by a user for a certain session  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EVENTSESSIONID | bigint |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| RATING | int |  | YES | ((0)) |
| FEEDBACK | nvarchar | 2000 | YES | ('') |
| DATESUBMITTED | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## SessionCategory
**Physical table:** `OSUSR_wu5_SessionCategory`  
**Description:** Collection of Session Category  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| COLORID | nvarchar | 50 | YES | (NULL) |

## Speaker
**Physical table:** `OSUSR_wu5_Speaker`  
**Description:** Entity to hold all information regarding the Speaker  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| DESCRIPTION | nvarchar | 1000 | YES | ('') |
| IMAGEID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
