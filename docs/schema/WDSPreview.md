# WDSPreview

## Tables

- [Alert2](#alert2)
- [AvatarNotifications](#avatarnotifications)
- [AvatarSize](#avatarsize)
- [AvatarSizes](#avatarsizes)
- [ChipNotifications](#chipnotifications)
- [DateFormat](#dateformat)
- [DOC_Position](#doc-position)
- [DummyDropdown](#dummydropdown)
- [DummyList](#dummylist)
- [GutterSize2](#guttersize2)
- [MenuSubCategory](#menusubcategory)
- [RankSize2](#ranksize2)
- [Sample_Invoices](#sample-invoices)
- [Sample_Membership](#sample-membership)
- [Sample_Payment](#sample-payment)
- [Theme](#theme)
- [Timer](#timer)
- [TimerIntervals](#timerintervals)
- [WodifyIconSet](#wodifyiconset)

## Alert2
**Physical table:** `OSUSR_CUH_ALERT2`  
**Description:** Different types of alert messages  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ALERT | nvarchar | 50 | NO |  |

## AvatarNotifications
**Physical table:** `OSUSR_CUH_AVATARNOTIFICATIONS1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## AvatarSize
**Physical table:** `OSUSR_CUH_AVATARSIZE`  
**Description:** Contains different type of sizes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SIZE | nvarchar | 50 | NO |  |

## AvatarSizes
**Physical table:** `OSUSR_MTI_AVATARSIZES`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ChipNotifications
**Physical table:** `OSUSR_MTI_CHIPNOTIFICATIONS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## DateFormat
**Physical table:** `OSUSR_CUH_DATEFORMAT`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## DOC_Position
**Physical table:** `OSUSR_MTI_DOC_POSITION`  
**Description:** Used only for documentation, because can't fetch data from Library Modules  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| POSITION | nvarchar | 50 | NO |  |

## DummyDropdown
**Physical table:** `OSUSR_CUH_DUMMYDROPDOWN`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## DummyList
**Physical table:** `OSUSR_CUH_DUMMYLIST`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TITLE | nvarchar | 50 | YES | ('') |
| SUBTITLE | nvarchar | 50 | YES | ('') |

## GutterSize2
**Physical table:** `OSUSR_CUH_GUTTERSIZE2`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| GUTTERSIZE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| LABEL | nvarchar | 50 | YES | ('') |

## MenuSubCategory
**Physical table:** `OSUSR_MTI_MENUSUBCATEGORY`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| MENUCATEGORYID | int |  | YES | ((0)) |
| IMAGEPATH | nvarchar | 500 | YES | ('') |

## RankSize2
**Physical table:** `OSUSR_CUH_RANKSIZE2`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Sample_Invoices
**Physical table:** `OSUSR_CUH_SAMPLE_INVOICES`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INVOICE | nvarchar | 255 | YES | ('') |
| PRODUCTNAME | nvarchar | 255 | YES | ('') |
| STATUS | nvarchar | 255 | YES | ('') |
| AUTOBILL | bit |  | YES | ((0)) |
| FINALCHARGE | decimal |  | YES | ((0)) |
| PAYMENTDUE | datetime |  | YES | ('1900-01-01 00:00:00') |

## Sample_Membership
**Physical table:** `OSUSR_CUH_SAMPLE_MEMBERSHIP`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| MEMBERSHIP | nvarchar | 255 | YES | ('') |
| LOCATIONSALE | nvarchar | 255 | YES | ('') |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXPIRES | datetime |  | YES | ('1900-01-01 00:00:00') |
| TYPE | nvarchar | 255 | YES | ('') |
| ATTENDANCELIMITATION | nvarchar | 255 | YES | ('') |
| AUTORENEW | bit |  | YES | ((0)) |

## Sample_Payment
**Physical table:** `OSUSR_CUH_SAMPLE_PAYMENT`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 255 | YES | ('') |
| EXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| VERIFICATION | bit |  | YES | ((0)) |
| ISDEFAULT | bit |  | YES | ((0)) |
| SHARED | nvarchar | 255 | YES | ('') |

## Theme
**Physical table:** `OSUSR_MTI_THEME`  
**Description:** Application Themes  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| THEME | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISDARK | bit |  | YES | ((0)) |

## Timer
**Physical table:** `OSUSR_CUH_WORKOUTEXERCICE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| NUMBEROFSETS | int |  | YES | ((1)) |
| WARMUPSECONDS | int |  | YES | ((0)) |
| WARMUPCOLOR | nvarchar | 50 | YES | ('') |
| COOLDOWNSECONDS | int |  | YES | ((0)) |
| COOLDOWNCOLOR | nvarchar | 50 | YES | ('') |
| RESTBETWEENSETSSECONDS | int |  | YES | ((0)) |
| RESTBETWEENSETSCOLOR | nvarchar | 50 | YES | ('green') |
| RESTBETWEENINTERVALSSECONDS | int |  | YES | ((0)) |
| RESTBETWEENINTERVALSCOLOR | nvarchar | 50 | YES | ('yellow') |

## TimerIntervals
**Physical table:** `OSUSR_CUH_WORKOUTEXERCISETIMER`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| TIMESECONDS | int |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| WORKOUTEXERCICEID | bigint |  | YES | (NULL) |
| TIMERID | bigint |  | YES | (NULL) |

## WodifyIconSet
**Physical table:** `OSUSR_CUH_WODIFYICONSET`  
**Description:** Wodify Icon Set  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CLASSNAME | nvarchar | 50 | YES | ('') |
