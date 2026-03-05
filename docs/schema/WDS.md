# WDS

## Tables

- [DateFormat](#dateformat)
- [DeviceResponsive](#deviceresponsive)
- [DeviceType](#devicetype)

## DateFormat
**Physical table:** `OSUSR_KH4_DATEFORMAT`  
**Description:** Holds all possible DateFormats that can be used  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| EXAMPLE | nvarchar | 50 | YES | ('') |
| SHORTDATEFORMAT | nvarchar | 50 | YES | ('') |
| SHORTDATENOYEARFORMAT | nvarchar | 50 | YES | ('') |
| LONGDATEFORMAT | nvarchar | 50 | YES | ('') |
| LONGDATENOYEARFORMAT | nvarchar | 50 | YES | ('') |
| RDSDATEPICKERFORMAT | nvarchar | 50 | YES | ('') |
| INPUTCALENDARFORMAT | nvarchar | 50 | YES | ('') |
| JQUERYGOODIESINPUTCALENDAR | nvarchar | 50 | YES | ('') |
| MOMENTINPUTCALENDAR | nvarchar | 50 | YES | ('') |
| MASSEMAILSFORMAT | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## DeviceResponsive
**Physical table:** `OSUSR_KH4_DEVICERESPONSIVE`  
**Description:** Defines the behavior response according to the device or group of devices types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## DeviceType
**Physical table:** `OSUSR_KH4_DEVICETYPE`  
**Description:** Type of devices which can access the application  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CLASS | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
