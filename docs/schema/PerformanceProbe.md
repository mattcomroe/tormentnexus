# PerformanceProbe

## Tables

- [Purpose](#purpose)
- [RequestData](#requestdata)

## Purpose
**Physical table:** `OSUSR_qiv_Purpose`  
**Description:** Contains all the environment purposes defined in licenses.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
| DISPLAYLABEL | nvarchar | 50 | YES | ('') |

## RequestData
**Physical table:** `OSUSR_qiv_RequestData`  
**Description:** RawData collected from the end-user experience, such as web screen load time and end-user IP.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| INSTANTSTART | datetime |  | YES | ('1900-01-01 00:00:00') |
| LOADTIME | int |  | YES | ((0)) |
| BROWSERTIME | int |  | YES | ((0)) |
| USERAGENT | nvarchar | 1000 | YES | ('') |
| USERIP | nvarchar | 45 | YES | ('') |
| SCREENRESOLUTION | nvarchar | 20 | YES | ('') |
| REQUESTKEY | nvarchar | 40 | YES | ('') |
| VISITORKEY | nvarchar | 40 | YES | ('') |
| VISITKEY | nvarchar | 40 | YES | ('') |
| SESSIONKEY | nvarchar | 40 | YES | ('') |
| USERKEY | nvarchar | 40 | YES | ('') |
| APPLICATIONKEY | nvarchar | 40 | YES | ('') |
| ESPACEKEY | nvarchar | 40 | YES | ('') |
| WEBSCREENKEY | nvarchar | 40 | YES | ('') |
| WEBSCREENNAME | nvarchar | 50 | YES | ('') |
| TENANTKEY | nvarchar | 40 | YES | ('') |
| ENVIRONMENTKEY | nvarchar | 40 | YES | ('') |
| FRONTENDNAME | nvarchar | 100 | YES | ('') |
| AJAXREQUESTCOUNT | int |  | YES | ((0)) |
| FRONTENDKEY | nvarchar | 100 | YES | ('') |
