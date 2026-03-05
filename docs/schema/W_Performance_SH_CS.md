# W_Performance_SH_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [PerformanceResultSource](#performanceresultsource)
- [PerformanceSettings](#performancesettings)
- [PRType](#prtype)
- [Request](#request)
- [RequestType](#requesttype)
- [ResultsSharingOption](#resultssharingoption)
- [UserClassLogin](#userclasslogin)
- [UserComponent](#usercomponent)
- [WorkoutTrackingLocationSettings](#workouttrackinglocationsettings)

## AsyncProcess
**Physical table:** `OSUSR_lgw_AsyncProcess`  
**Description:** Auxiliar entity that contains all asynchronous processes, which will run through the AP module in BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PerformanceResultSource
**Physical table:** `OSUSR_lgw_PerformanceResultSource`  
**Description:** Entity to hold the PerformanceResultSource. For Performance Results, this replaces the LoginSource entity (WCS-15700). The first 3 records (Web Mobile NewMobile) are brought over here as inactive to not break the FK relationship for existing records  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PerformanceSettings
**Physical table:** `OSUSR_lgw_PerformanceSettings`  
**Description:** Contains all the settings of a Customer regarding Performance. One record per Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANTID | int |  | YES | ((0)) |
| DEFAULTLEADERBOARDID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| RESULTSSHARING | int |  | YES | (NULL) |
| RESULTSSHARINGSETTING | int |  | YES | (NULL) |
| RESULTSSHARINGOPTION | int |  | YES | (NULL) |
| PROGRESSIONSENABLED | bit |  | YES | ((0)) |
| SHOWLEADERBOARDHOMEPAGE | bit |  | YES | ((0)) |
| SHOWHIGHLIGHTSHOMEPAGE | bit |  | YES | ((1)) |
| CUSTOMERID | bigint |  | NO | ((0)) |

## PRType
**Physical table:** `OSUSR_72o_PRType`  
**Description:** types of PRs  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_lgw_PRRecalculationRequest`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| USERID | int |  | YES | (NULL) |
| COMPONENTID | int |  | YES | (NULL) |
| NUMBEROFTRIES | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| HASFINISHED | bit |  | YES | ((0)) |
| ISRUNNINGSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |
| REQUESTTYPEID | int |  | YES | (NULL) |
| ISMANUALLYRETRIED | bit |  | YES | ((0)) |
| RETRIEDBY | int |  | YES | (NULL) |

## RequestType
**Physical table:** `OSUSR_lgw_RequestType`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## ResultsSharingOption
**Physical table:** `OSUSR_lgw_ResultsSharingOption`  
**Description:** Whether result sharing is on or off; if on, how results are ordered.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## UserClassLogin
**Physical table:** `OSUSR_72o_UserClassLogin`  
**Description:** Contains information for when a user, a lead or dropin has signed into a class  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| ATHLETENAME | nvarchar | 101 | YES | ('') |
| CLASSID | int |  | YES | (NULL) |
| LOGINSOURCEID | int |  | YES | (NULL) |
| MEMBERPLANID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| GENDERID | int |  | YES | (NULL) |
| ISDROPIN | bit |  | YES | ((0)) |
| COUNTTOWARDSATTENDANCELIMITS | bit |  | YES | ((0)) |
| RESULTSSOURCEID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| ISLEAD | bit |  | YES | ((0)) |
| EMAIL | nvarchar | 250 | YES | ('') |
| SENTWAIVEREMAIL | bit |  | YES | ((0)) |
| ENFORCEMEMBERSHIPLIMITS | bit |  | YES | ((0)) |
| CONTRACTENFORCEMENTTYPEID | int |  | YES | (NULL) |
| SESSIONENFORCEMENTTYPEID | int |  | YES | (NULL) |
| ISAUTOSIGNIN | bit |  | YES | ((0)) |
| ONLINEMEMBERSHIPSALEID | int |  | YES | (NULL) |
| WASSENTATTENDEDEMAIL | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DROPINID | bigint |  | YES | (NULL) |

## UserComponent
**Physical table:** `OSUSR_72o_UserComponent`  
**Description:** An exercise that was added by a client, outside a WOD.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| COMPONENTRESULTID | int |  | YES | (NULL) |
| USERCLASSLOGINID | int |  | YES | (NULL) |
| COMPONENTTYPEID | int |  | YES | (NULL) |
| COMPONENTID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| PERFORMANCERESULTID | bigint |  | YES | ((0)) |
| MEASUREREPSCHEME | nvarchar | 50 | YES | ('') |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ORIGINALCOMPONENTID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PERFORMANCERESULTGUID | nvarchar | 36 | YES | ('') |
| UOMWEIGHTID | int |  | YES | (NULL) |
| UOMDISTANCEID | int |  | YES | (NULL) |
| SETS | int |  | YES | ((0)) |
| REPS | int |  | YES | ((0)) |
| WODCOMPONENTID | int |  | YES | (NULL) |

## WorkoutTrackingLocationSettings
**Physical table:** `OSUSR_lgw_WorkoutTrackingLocationSettings`  
**Description:** Contains the Workout Tracking feature settings for a given location.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| LOCATIONID | int |  | NO |  |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
