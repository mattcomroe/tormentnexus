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
**Physical table:** `OSUSR_QDM_CUSTOMACTION`  
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
**Physical table:** `OSUSR_QDM_ACTIONINPUT`  
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
**Physical table:** `OSUSR_QDM_ACTIONINPUTMULTIOPTION`  
**Description:** Options for an Button input if type is Multiple Choice or Multi-select.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ACTIONINPUTID | bigint |  | YES | (NULL) |
| OPTION | nvarchar | 50 | YES | ('') |
| CUSTOMACTIONINPUTID | bigint |  | YES | (NULL) |

## DeviceEvent
**Physical table:** `OSUSR_QDM_DEVICELOG`  
**Description:** Logs Smart Device events from Seam and Workflows  

_Column definitions not found in schema export._

## DeviceEventSource
**Physical table:** `OSUSR_QDM_DEVICEEVENTSOURCE`  
**Description:** Source of Device event, Seam or Workflows  

_Column definitions not found in schema export._

## DeviceEventType
**Physical table:** `OSUSR_QDM_DEVICEEVENTTYPE`  
**Description:** Type of Device event  

_Column definitions not found in schema export._

## InputType
**Physical table:** `OSUSR_QDM_INPUTTYPE`  
**Description:** Input types for ButtonInputs.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PageButton
**Physical table:** `OSUSR_QDM_PAGEBUTTON`  
**Description:** Entity to associate a Workflow Button Page with Workflow Buttons, i.e. shows which Buttons is on a Page.  

_Column definitions not found in schema export._

## PersonAccessCode
**Physical table:** `OSUSR_QDM_PERSONACCESSCODE`  
**Description:** joining table that maps Access Code to a person and/or Reservation  

_Column definitions not found in schema export._

## SmartButtonPage
**Physical table:** `OSUSR_QDM_CUSTOMMENUITEM`  
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
**Physical table:** `OSUSR_QDM_CUSTOMAUTOMATIONREQUESTSTATUS`  
**Description:** Statuses for smart button requests.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
