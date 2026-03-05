# CustomAutomations_CS

## Tables

- [Button](#button)
- [ButtonInput](#buttoninput)
- [ButtonInputOption](#buttoninputoption)
- [DeviceEvent](#deviceevent)
- [DeviceEventSource](#deviceeventsource)
- [DeviceEventType](#deviceeventtype)
- [InputType](#inputtype)
- [PageButton](#pagebutton)
- [PersonAccessCode](#personaccesscode)
- [SmartButtonPage](#smartbuttonpage)
- [SmartButtonRequestStatus](#smartbuttonrequeststatus)

## Button
**Physical table:** `OSUSR_qdm_CustomAction`  
**Description:** Smart button data.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMMENUITEMID | bigint |  | YES | (NULL) |
| LABEL | nvarchar | 50 | YES | ('') |
| ICON | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## ButtonInput
**Physical table:** `OSUSR_qdm_ActionInput`  
**Description:** Button input data.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMACTIONID | bigint |  | YES | (NULL) |
| INPUTTYPEID | int |  | YES | (NULL) |
| LABEL | nvarchar | 50 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| DROPDOWNTYPEID | int |  | YES | (NULL) |

## ButtonInputOption
**Physical table:** `OSUSR_qdm_ActionInputMultiOption`  
**Description:** Options for an Button input if type is Multiple Choice or Multi-select.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ACTIONINPUTID | bigint |  | YES | (NULL) |
| OPTION | nvarchar | 50 | YES | ('') |
| CUSTOMACTIONINPUTID | bigint |  | YES | (NULL) |

## DeviceEvent
**Physical table:** `OSUSR_qdm_DeviceLog`  
**Description:** Logs Smart Device events from Seam and Workflows  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## DeviceEventSource
**Physical table:** `OSUSR_qdm_DeviceEventSource`  
**Description:** Source of Device event, Seam or Workflows  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## DeviceEventType
**Physical table:** `OSUSR_qdm_DeviceEventType`  
**Description:** Type of Device event  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## InputType
**Physical table:** `OSUSR_qdm_InputType`  
**Description:** Input types for ButtonInputs.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PageButton
**Physical table:** `OSUSR_qdm_PageButton`  
**Description:** Entity to associate a Workflow Button Page with Workflow Buttons, i.e. shows which Buttons is on a Page.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## PersonAccessCode
**Physical table:** `OSUSR_qdm_PersonAccessCode`  
**Description:** joining table that maps Access Code to a person and/or Reservation  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## SmartButtonPage
**Physical table:** `OSUSR_qdm_CustomMenuItem`  
**Description:** Smart button page data.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LOCATIONID | bigint |  | YES | ((0)) |
| LABEL | nvarchar | 50 | YES | ('') |
| ICON | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## SmartButtonRequestStatus
**Physical table:** `OSUSR_qdm_CustomAutomationRequestStatus`  
**Description:** Statuses for smart button requests.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
