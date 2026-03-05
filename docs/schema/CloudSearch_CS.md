# CloudSearch_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [AsyncProcessType](#asyncprocesstype)
- [CloudSearchAuditResult](#cloudsearchauditresult)
- [CloudSearchFilterUsage](#cloudsearchfilterusage)
- [CloudSearchLogicOperator](#cloudsearchlogicoperator)
- [CloudSearchReturnData](#cloudsearchreturndata)
- [CloudSearchSync](#cloudsearchsync)
- [CloudSearchSyncClient](#cloudsearchsyncclient)
- [EndPointDomain](#endpointdomain)
- [GlobalSearchActionType](#globalsearchactiontype)
- [GlobalSearchType](#globalsearchtype)
- [Request](#request)
- [RequestType](#requesttype)

## AsyncProcess
**Physical table:** `OSUSR_43w_AsyncProcess`  
**Description:** Auxiliar entity that contains all membership asynchronous processes, which will run through the Membership_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ASYNCPROCESSTYPEID | int |  | YES | (NULL) |

## AsyncProcessType
**Physical table:** `OSUSR_43w_AsyncProcessType`  
**Description:** contains all timers and BPTs that can run asynchronously through the Membership_AP  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CloudSearchAuditResult
**Physical table:** `OSUSR_43w_CloudSearchAuditResult`  
**Description:** Tracks audit results for Email_CloudSearchAudit timer in CloudSearchSyncAudit_AP  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ATTRIBUTENAME | nvarchar | 60 | YES | ('') |
| NUMCONFLICTING | int |  | YES | ((0)) |

## CloudSearchFilterUsage
**Physical table:** `OSUSR_43w_CloudSearchFilterUsage`  
**Description:** Indicates the usage of the filter  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| USAGE | nvarchar | 50 | YES | ('') |

## CloudSearchLogicOperator
**Physical table:** `OSUSR_43w_CloudSearchLogicOperator`  
**Description:** Cloud Search logic operator  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| OPERATOR | nvarchar | 50 | YES | ('') |

## CloudSearchReturnData
**Physical table:** `OSUSR_43w_CloudSearchReturnData`  
**Description:** Indicates what fields CloudSearch should return  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ATTRIBUTE | nvarchar | 200 | YES | ('') |

## CloudSearchSync
**Physical table:** `OSUSR_43w_CloudSearchSync`  
**Description:** Contains only one record with that manages when it is syncing with CloudSearch via cloudsearch_API  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LASTSYNCAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISSYNCING | bit |  | YES | ((0)) |
| SYNCID | nvarchar | 50 | YES | ('') |

## CloudSearchSyncClient
**Physical table:** `OSUSR_43w_CloudSearchSyncClient`  
**Description:** Contains all the clients that will be synced in CloudSearch in a specified SyncId from Cloudsearch_API  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| SYNCID | nvarchar | 50 | YES | ('') |

## EndPointDomain
**Physical table:** `OSUSR_43w_EndPointDomain`  
**Description:** Holds information about a domain's identifier needed to build the base URL  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |
| INITIALURLPATHOPERATION | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 1000 | YES | ('') |

## GlobalSearchActionType
**Physical table:** `OSUSR_43w_GlobalSearchActionType`  
**Description:** Global Search Action Type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## GlobalSearchType
**Physical table:** `OSUSR_43w_GlobalSearchType`  
**Description:** Global Search Type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_43w_Request`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| REQUESTTYPEID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| LEADID | bigint |  | YES | ((0)) |
| ISRUNNINGSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISMANUALLYRETRIED | bit |  | YES | ((0)) |
| RETRIEDBY | int |  | YES | (NULL) |
| NUMBEROFTRIES | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| HASFINISHED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| FILE | varbinary | -1 | YES | (NULL) |

## RequestType
**Physical table:** `OSUSR_43w_RequestType`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
