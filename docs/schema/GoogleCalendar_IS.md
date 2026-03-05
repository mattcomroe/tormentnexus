# GoogleCalendar_IS

## Tables

- [GoogleCalendar](#googlecalendar)
- [GoogleCalendarEvent](#googlecalendarevent)
- [GoogleCalendarEventExclusion](#googlecalendareventexclusion)

## GoogleCalendar
**Physical table:** `OSUSR_c69_GoogleCalendar`  
**Description:** A Google Calendar  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GOOGLEACCOUNTID | bigint |  | YES | (NULL) |
| EXTERNALID | nvarchar | 1000 | YES | ('') |
| NAME | nvarchar | 500 | YES | ('') |
| ISREADONLY | bit |  | YES | ((0)) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| NEXTSYNCTOKEN | nvarchar | 50 | YES | ('') |
| WATCHCHANNELID | nvarchar | 1000 | YES | ('') |
| WATCHRESOURCEID | nvarchar | 1000 | YES | ('') |
| WATCHEXPIRATIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISPRIMARY | bit |  | YES | ((0)) |

## GoogleCalendarEvent
**Physical table:** `OSUSR_c69_GoogleCalendarEvent`  
**Description:** A Google Calendar event  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GOOGLECALENDARID | bigint |  | YES | (NULL) |
| EXTERNALID | nvarchar | 1000 | YES | ('') |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| SUMMARY | nvarchar | 1000 | YES | ('') |
| TIMEZONEID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISBUSY | bit |  | YES | ((0)) |

## GoogleCalendarEventExclusion
**Physical table:** `OSUSR_c69_GoogleCalendarEventExclusion`  
**Description:** IDs of Google Calendar events that should be excluded from the import process. These are usually events that were exported from the app, so we don't want to import them  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| EXTERNALD | nvarchar | 1000 | NO |  |
