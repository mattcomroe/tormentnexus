# Reporting_CS

## Tables

- [CustomerDashboardFilter](#customerdashboardfilter)
- [DateWeekMap](#dateweekmap)
- [Report](#report)
- [ReportMetabaseId](#reportmetabaseid)
- [ReportType](#reporttype)
- [ReportUserStar](#reportuserstar)

## CustomerDashboardFilter
**Physical table:** `OSUSR_VTI_CUSTOMERDASHBOARDFILTER`  
**Description:** Holds a set of filters for a dashboard specific to a customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DASHBOARDID | bigint |  | YES | ((0)) |
| FILTER | nvarchar | 500 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## DateWeekMap
**Physical table:** `OSUSR_VTI_DATEWEEKMAP`  
**Description:** Maps dates to what week they would be in the year  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| YEAR | int |  | YES | ((0)) |
| WEEK | int |  | YES | ((0)) |
| DAY | int |  | YES | ((0)) |
| YEARWEEK | nvarchar | 15 | YES | ('') |
| TOTALWEEK | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| FOLLOWINGDATE | datetime |  | YES | ('1900-01-01 00:00:00') |

## Report
**Physical table:** `OSUSR_72O_REPORT`  
**Description:** Our pre-configured reports to be viewed/ran.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| TITLE | nvarchar | 255 | YES | ('') |
| DESCRIPTION | nvarchar | 255 | YES | ('') |
| VIEWABLEBYCOACH | bit |  | YES | ((0)) |
| REPORTTYPEID | int |  | YES | (NULL) |
| ISADMINVIEWABLE | bit |  | YES | ((0)) |
| ISMANAGERVIEWABLE | bit |  | YES | ((0)) |
| ISCOACHVIEWABLE | bit |  | YES | ((0)) |
| METABASEDASHBOARDID | bigint |  | YES | ((0)) |
| REPORTHELPURL | nvarchar | 255 | YES | ('') |
| IS_REALTIME | bit |  | YES | ((0)) |
| IS_UNLISTED | bit |  | YES | ((0)) |
| IS_EMBEDDABLE | bit |  | YES | ((0)) |
| SITEPROPERTYNAME | nvarchar | 50 | YES | ('') |

## ReportMetabaseId
**Physical table:** `OSUSR_VTI_REPORTMETABASEID`  
**Description:** Metabase ID of the dashboard corresponding to a report. These are decoupled from the static entity to allow us to have different values in each environment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| REPORTID | int |  | NO |  |
| METABASEDASHBOARDID | bigint |  | YES | ((0)) |

## ReportType
**Physical table:** `OSUSR_72O_REPORTTYPE`  
**Description:** The categories for our canned reports  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ReportUserStar
**Physical table:** `OSUSR_VTI_REPORTUSERSTAR`  
**Description:** Table to hold records of reports which users have favorited.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| REPORTID | int |  | YES | (NULL) |
| ISSTARRED | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
