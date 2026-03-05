# Calendar_CS

## Tables

- [ButtonIcon](#buttonicon)
- [Calendar](#calendar)
- [CalendarAction](#calendaraction)
- [CalendarBusinessHoursDOW](#calendarbusinesshoursdow)
- [CalendarDefaultFilter](#calendardefaultfilter)
- [CalendarDisplayHeader](#calendardisplayheader)
- [CalendarEvent](#calendarevent)
- [CalendarFilter](#calendarfilter)
- [CalendarHiddenDay](#calendarhiddenday)
- [CalendarModule](#calendarmodule)
- [CalendarTextCustom](#calendartextcustom)
- [CalendarTimezone](#calendartimezone)
- [CustomerSettingCalendar](#customersettingcalendar)
- [ElementType](#elementtype)
- [EventLimitClick](#eventlimitclick)
- [HeaderElement](#headerelement)
- [HeaderPosition](#headerposition)

## ButtonIcon
**Physical table:** `OSUSR_BO7_BUTTONICON`  
**Description:** Contains the icons used to navigate in the calendar.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## Calendar
**Physical table:** `OSUSR_BO7_CALENDAR`  
**Description:** Contains all the main configurations for the creation of a calendar  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 500 | YES | ('') |
| CALENDARMODULEID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| FIRSTDAY | int |  | YES | (NULL) |
| ISRTL | bit |  | YES | ((0)) |
| INCLUDEWEEKENDS | bit |  | YES | ((0)) |
| FIXEDWEEKCOUNT | bit |  | YES | ((0)) |
| WEEKNUMBERS | bit |  | YES | ((0)) |
| WEEKNUMBERCALCULATION | nvarchar | 5 | YES | ('') |
| USEBUSINESSHOURS | bit |  | YES | ((0)) |
| BUSINESSHOURSSTART | datetime |  | YES | ('1900-01-01 00:00:00') |
| BUSINESSHOURSEND | datetime |  | YES | ('1900-01-01 00:00:00') |
| HEIGHT | int |  | YES | ((0)) |
| CONTENTHEIGHT | int |  | YES | ((0)) |
| ASPECTRATIO | decimal |  | YES | ((0)) |
| HANDLEWINDOWRESIZE | bit |  | YES | ((0)) |
| EVENTLIMIT | int |  | YES | ((0)) |
| EVENTLIMITCLICKID | int |  | YES | (NULL) |
| EVENTLIMITCLICKVIEW | int |  | YES | (NULL) |
| DEFAULTVIEW | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| SELECTABLE | bit |  | YES | ((0)) |
| SELECTHELPER | bit |  | YES | ((0)) |

## CalendarAction
**Physical table:** `OSUSR_BO7_CALENDARACTION`  
**Description:** It contains all the possible actions that a user can have while selecting days and events  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ACTION | nvarchar | 50 | NO |  |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CalendarBusinessHoursDOW
**Physical table:** `OSUSR_BO7_CALENDARBUSINESSHOURSDOW`  
**Description:** Emphasizes certain time slots on the calendar. By default, Monday-Friday  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CALENDARID | int |  | YES | (NULL) |
| DAYOFWEEKID | int |  | YES | (NULL) |

## CalendarDefaultFilter
**Physical table:** `OSUSR_BO7_CALENDARDEFAULTFILTER`  
**Description:** It contains the default filters for each calendar for each Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| CALENDARMODULEID | int |  | YES | (NULL) |
| CALENDARFILTERID | int |  | YES | (NULL) |
| VALUES | nvarchar | 500 | YES | ('') |
| CUSTOMERID | bigint |  | YES | ((0)) |

## CalendarDisplayHeader
**Physical table:** `OSUSR_BO7_CALENDARDISPLAYHEADER`  
**Description:** All the Elements that will be displayed in the header  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CALENDARID | int |  | YES | (NULL) |
| HEADERPOSITIONID | int |  | YES | (NULL) |
| HEADERELEMENTID | int |  | YES | (NULL) |
| ISSEPARATED | bit |  | YES | ((0)) |
| ICONID | int |  | YES | (NULL) |
| TEXT | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## CalendarEvent
**Physical table:** `OSUSR_BO7_CALENDAREVENT`  
**Description:** Settings to Drag or Resizing events in a global way  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| EDITABLE | bit |  | YES | ((0)) |
| EVENTSTARTEDITABLE | bit |  | YES | ((0)) |
| EVENTDURATIONEDITABLE | bit |  | YES | ((0)) |
| DRAGREVERTDURATION | int |  | YES | ((0)) |
| DRAGOPACITY | decimal |  | YES | ((0)) |
| DRAGSCROLL | bit |  | YES | ((0)) |
| EVENTOVERLAP | bit |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| BACKGROUNDCOLOR | nvarchar | 50 | YES | ('') |
| BORDERCOLOR | nvarchar | 50 | YES | ('') |
| TEXTCOLOR | nvarchar | 50 | YES | ('') |

## CalendarFilter
**Physical table:** `OSUSR_BO7_CALENDARFILTER`  
**Description:** It contains all possible filters for all calendars. Is used to get the default filters for each calendar  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## CalendarHiddenDay
**Physical table:** `OSUSR_BO7_CALENDARHIDDENDAYS`  
**Description:** Exclude certain days-of-the-week from being displayed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CALENDARID | int |  | YES | (NULL) |
| DAYOFWEEKID | int |  | YES | (NULL) |

## CalendarModule
**Physical table:** `OSUSR_BO7_CALENDARMODULE`  
**Description:** It contains all the Calendars that will be displayed in the application  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## CalendarTextCustom
**Physical table:** `OSUSR_BO7_CALENDARTEXTCUSTOM`  
**Description:** It contains Text Customization for text that is dinamic.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| VALUE | nvarchar | 50 | YES | ('') |

## CalendarTimezone
**Physical table:** `OSUSR_BO7_CALENDARTIMEZONE`  
**Description:** Contains the timezone in which dates throughout the API are parsed and rendered.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TIMEZONE | nvarchar | 50 | YES | ('') |

## CustomerSettingCalendar
**Physical table:** `OSUSR_BO7_CALENDARSETTING`  
**Description:** Contains all the general settings for the calendars for each Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| WODDEFAULTVIEW | int |  | YES | (NULL) |
| FIRSTDAYOFWEEKID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| WODGYMNASTICSCOLOR | nvarchar | 50 | YES | ('') |
| WODWEIGHTLIFTINGCOLOR | nvarchar | 50 | YES | ('') |
| WODWEIGHTLIFTINGTOTALCOLOR | nvarchar | 50 | YES | ('') |
| WODMETCONSCOLOR | nvarchar | 50 | YES | ('') |
| CUSTOMERID | bigint |  | NO |  |

## ElementType
**Physical table:** `OSUSR_BO7_ELEMENTTYPE`  
**Description:** Contains all the possible types of buttons that can appear on the header  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## EventLimitClick
**Physical table:** `OSUSR_BO7_EVENTLIMITCLICK`  
**Description:** Determines the action taken when the user clicks on a "more" link created by the eventLimit option.  "popover", "week", "day", view name "popover" (the default) Displays a rectangular panel over the cell with a full list of events for that day. "week" Goes to a week view, as determined by the views in the header. "day" Goes to a day view, as determined by the views in the header. view name A literal string name of any of the Available Views.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## HeaderElement
**Physical table:** `OSUSR_BO7_HEADERELEMENT`  
**Description:** Contains all the possible buttons that can appear on the header  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ELEMENTTYPEID | int |  | YES | (NULL) |
| VALUE | nvarchar | 50 | YES | ('') |
| CAPTION | nvarchar | 50 | YES | ('') |

## HeaderPosition
**Physical table:** `OSUSR_BO7_HEADERPOSITION`  
**Description:** Contains all the positions that the Element will stay (left, right or center)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
