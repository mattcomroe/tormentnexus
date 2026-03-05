# zSandboxDon_SpeedRotationPOC

## Tables

- [DailyPerformanceMetric](#dailyperformancemetric)
- [DailyPerformanceReport](#dailyperformancereport)
- [GeneralLogModule_Name](#generallogmodule-name)
- [LogStatistics](#logstatistics)
- [PerformanceActionName](#performanceactionname)
- [PerformanceEspace](#performanceespace)
- [PerformanceWebPage](#performancewebpage)
- [ReportLogName](#reportlogname)

## DailyPerformanceMetric
**Physical table:** `OSUSR_U76_DAILYPERFORMANCEMETRIC`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| DAILYPERFORMANCEREPORTID | int |  | YES | (NULL) |
| GUID | nvarchar | 50 | YES | ('') |
| ESPACENAME | int |  | YES | (NULL) |
| ACTIONNAME | int |  | YES | (NULL) |
| WEBPAGENAME | int |  | YES | (NULL) |
| APDEX_SCORE | decimal |  | YES | ((0)) |
| APDEX_SATISFACTORYCOUNT | bigint |  | YES | ((0)) |
| APDEX_TOLERABLECOUNT | bigint |  | YES | ((0)) |
| APDEX_TOTALCOUNT | bigint |  | YES | ((0)) |
| APDEX_APDEXTHRESHOLD | bigint |  | YES | ((0)) |
| TOTALDURATION | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## DailyPerformanceReport
**Physical table:** `OSUSR_U76_PERFORMANCEREPORT`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| REPORTNAME | nvarchar | 200 | YES | ('') |
| REPORTLOGNAMEID | int |  | YES | (NULL) |
| REPORTSTARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| REPORTENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| REPORTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| APDEX_SCORE | decimal |  | YES | ((0)) |
| APDEX_SATISFACTORYCOUNT | bigint |  | YES | ((0)) |
| APDEX_TOLERABLECOUNT | bigint |  | YES | ((0)) |
| APDEX_TOTALCOUNT | bigint |  | YES | ((0)) |
| APDEX_APDEXTHRESHOLD | bigint |  | YES | ((0)) |
| TOTALDURATION | int |  | YES | ((0)) |
| ESPACENAME | nvarchar | 200 | YES | ('') |
| ACTIONNAME | nvarchar | 50 | YES | ('') |
| WEBPAGENAME | nvarchar | 50 | YES | ('') |

## GeneralLogModule_Name
**Physical table:** `OSUSR_U76_GENERALLOGMODULE_NAME`  
**Description:** Type Of data requested from general logs: slowSQL, slowExtension  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| SQLFILTER | nvarchar | 50 | YES | ('') |

## LogStatistics
**Physical table:** `OSUSR_U76_LOGSTATISTICS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| INSTANT | datetime |  | YES | ('1900-01-01 00:00:00') |
| LINEGROUPINGCOMPARISON | nvarchar | 1200 | YES | ('') |
| DURATION | bigint |  | YES | ((0)) |
| GUID | nvarchar | 50 | YES | ('') |

## PerformanceActionName
**Physical table:** `OSUSR_U76_PERFORMANCEACTIONNAME`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| ACTIONNAME | nvarchar | 200 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## PerformanceEspace
**Physical table:** `OSUSR_U76_PERFORMANCEESPACE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| ESPACENAME | nvarchar | 100 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## PerformanceWebPage
**Physical table:** `OSUSR_U76_PERFORMANCEWEBPAGE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| WEBPAGENAME | nvarchar | 200 | YES | ('') |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## ReportLogName
**Physical table:** `OSUSR_U76_REPORTLOGNAME`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| APDEXTHERSHHOLD | bigint |  | YES | ((1000)) |
