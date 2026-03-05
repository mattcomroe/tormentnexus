# Utils_LS

## Tables

- [AcceptedFiletype](#acceptedfiletype)
- [ActionRole](#actionrole)
- [ActionType](#actiontype)
- [AvatarRing](#avatarring)
- [Color](#color)
- [ColorObjectType](#colorobjecttype)
- [ColorObjectTypeMapping](#colorobjecttypemapping)
- [DateFormat](#dateformat)
- [DateRange](#daterange)
- [DayOfWeek](#dayofweek)
- [DaysOfTheMonth](#daysofthemonth)
- [Languages](#languages)
- [ObjectType](#objecttype)
- [ObjectTypeActionType](#objecttypeactiontype)
- [PaymentAccountSource](#paymentaccountsource)
- [PaymentAccountType](#paymentaccounttype)
- [SystemOfMeasure](#systemofmeasure)
- [TimePointType](#timepointtype)
- [TimeRelationType](#timerelationtype)
- [TransactionResultStatus](#transactionresultstatus)
- [UnitsOfTime](#unitsoftime)
- [UOMDistance](#uomdistance)
- [UOMTemperature](#uomtemperature)
- [UOMWeight](#uomweight)

## AcceptedFiletype
**Physical table:** `OSUSR_b3s_AcceptedFileType`  
**Description:** Filetype extensions for validation. The FileExtension field value should be in lower case.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| FILEEXTENSION | nvarchar | 50 | YES | ('') |
| FILEMIMETYPE | nvarchar | 255 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISDOCUMENTUPLOAD | bit |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ActionRole
**Physical table:** `OSUSR_b3s_ActionRole`  
**Description:** option, role, role definition,  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ActionType
**Physical table:** `OSUSR_b3s_ActionType`  
**Description:** service/resource type - task, email, sms, in app chat, etc.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## AvatarRing
**Physical table:** `OSUSR_b3s_AvatarRing`  
**Description:** Defines avatar ring types  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| COLORID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Color
**Physical table:** `OSUSR_b3s_Color`  
**Description:** Static colors to use for database representation when storing discrete color options  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| HEXCODE | nvarchar | 10 | YES | ('') |

## ColorObjectType
**Physical table:** `OSUSR_b3s_ColorObjectType`  
**Description:** Represents an entity or business concept that can have Colors.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ColorObjectTypeMapping
**Physical table:** `OSUSR_b3s_ColorObjectTypeMapping`  
**Description:** Associates a Color with an individual ColorObjectType so a Color can be used by multiple ColorObjectTypes  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| COLORID | int |  | YES | (NULL) |
| COLOROBJECTTYPEID | int |  | YES | (NULL) |

## DateFormat
**Physical table:** `OSUSR_b3s_DateFormat`  
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
| LONGDATEABVMONTHFORMAT | nvarchar | 50 | YES | ('') |
| LONGDATENOYEARABVMONTHFORMAT | nvarchar | 50 | YES | ('') |
| LONGDATENOMONTHFORMAT | nvarchar | 50 | YES | ('') |
| ISYMD | bit |  | YES | ((0)) |
| ISMDY | bit |  | YES | ((0)) |
| ISDMY | bit |  | YES | ((0)) |
| SHORTDATEABBREVMONTHNOYEARFO | nvarchar | 50 | YES | ('') |

## DateRange
**Physical table:** `OSUSR_kvs_DateRange`  
**Description:** Week starts on Monday  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## DayOfWeek
**Physical table:** `OSUSR_b3s_DayOfWeek`  
**Description:** Contains all possible days of the week  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| DAYOFWEEKVALUE | int |  | YES | ((0)) |

## DaysOfTheMonth
**Physical table:** `OSUSR_b3s_DaysOfTheMonth`  
**Description:** Day's of the month 1st - 31st  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Languages
**Physical table:** `OSUSR_b3s_Languages`  
**Description:** Contains supported Languanges  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| RFC1766 | nvarchar | 5 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ObjectType
**Physical table:** `OSUSR_b3s_ObjectType`  
**Description:** Represents an entity or business concept that can have tags.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INTERNALDESCRIPTION | nvarchar | 255 | YES | ('') |
| LABEL | nvarchar | 150 | YES | ('') |
| ENTITYIDATTRIBUTE | nvarchar | 255 | YES | ('') |
| EXTERNALNAME | nvarchar | 50 | YES | ('') |

## ObjectTypeActionType
**Physical table:** `OSUSR_b3s_ObjectTypeActionType`  
**Description:** joining table for an object type and the services it's accessible to  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| OBJECTTYPEID | int |  | YES | (NULL) |
| ACTIONTYPEID | int |  | YES | (NULL) |
| ACTIONROLEID | int |  | YES | (NULL) |

## PaymentAccountSource
**Physical table:** `OSUSR_kvs_PaymentAccountSource`  
**Description:** Types of payment methods that the system can accept (if configured).  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| REPORTORDER | int |  | YES | ((0)) |
| PAYMENTACCOUNTTYPE | int |  | YES | (NULL) |
| ISANONYMOUS | bit |  | YES | ((0)) |

## PaymentAccountType
**Physical table:** `OSUSR_kvs_PaymentAccountType`  
**Description:** Represents the possible payment account types. These are further sub-categorized by the PaymentAccountSource static entity.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| PLURALLABEL | nvarchar | 50 | YES | ('') |
| DEFAULTISENABLEDMEMBERSHIPS | bit |  | YES | ((0)) |
| DEFAULTISENABLEDRETAIL | bit |  | YES | ((0)) |
| DEFAULTISENABLEDDROPIN | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |

## SystemOfMeasure
**Physical table:** `OSUSR_kvs_SystemOfMeasure`  
**Description:** System of measurement.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| APPLIESTODISTANCE | bit |  | YES | ((0)) |
| APPLIESTOWEIGHT | bit |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TimePointType
**Physical table:** `OSUSR_b3s_TimePointType`  
**Description:** contains possible types of point in time  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TimeRelationType
**Physical table:** `OSUSR_b3s_TimeRelationType`  
**Description:** Suggests a type of relationship to a point in time — perfect for before/after/during  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TransactionResultStatus
**Physical table:** `OSUSR_kvs_TransactionResultStatus`  
**Description:** Possible transaction results.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## UnitsOfTime
**Physical table:** `OSUSR_b3s_UnitsOfTime`  
**Description:** Contains all possible time units  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PLURALLABEL | nvarchar | 50 | YES | ('') |
| SINGULARLABEL | nvarchar | 50 | YES | ('') |
| SINGULARPLURALLABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISTIMEUNIT | bit |  | YES | ((0)) |
| NUMBEROFDAYS | int |  | YES | ((0)) |

## UOMDistance
**Physical table:** `OSUSR_b3s_UOMDistance`  
**Description:** Units of measure for distance.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| SYSTEMOFMEASURE | int |  | YES | (NULL) |

## UOMTemperature
**Physical table:** `OSUSR_b3s_UOMTemperature`  
**Description:** Unit of Measure for Temperature  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| CODE | nvarchar | 5 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## UOMWeight
**Physical table:** `OSUSR_b3s_UOMWeight`  
**Description:** Units of measure for weight,  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| SYSTEMOFMEASURE | int |  | YES | (NULL) |
