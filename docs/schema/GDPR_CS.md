# GDPR_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [DataExtractionType](#dataextractiontype)
- [DataScrubType](#datascrubtype)
- [Request](#request)
- [RequestFile](#requestfile)
- [RequestScrubInfo](#requestscrubinfo)
- [RequestType](#requesttype)

## AsyncProcess
**Physical table:** `OSUSR_XST_ASYNCPROCESS`  
**Description:** Auxiliar entity that contains all waivers asynchronous processes, which will run through the GDPR_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## DataExtractionType
**Physical table:** `OSUSR_4KT_DATAEXTRACTIONTYPE`  
**Description:** Entity to reprsent all the type of data (files) we'll generate to be extracted.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## DataScrubType
**Physical table:** `OSUSR_4KT_DATASCRUBTYPE`  
**Description:** Entity to represent all the type of scrub types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## Request
**Physical table:** `OSUSR_XST_REQUEST1`  
**Description:** Contains all consent requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |
| REQUESTTYPEID | int |  | YES | (NULL) |
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

## RequestFile
**Physical table:** `OSUSR_XST_REQUESTFILE`  
**Description:** Entity to store temporarily the generated files to be extracted.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUESTID | bigint |  | YES | (NULL) |
| DATAEXTRACTIONTYPEID | int |  | YES | (NULL) |
| BINARYDATA | varbinary | -1 | YES | (NULL) |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 1000 | YES | ('') |
| FILESIZE | int |  | YES | ((0)) |
| ISPROCESSED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| NRTRIES | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | -1 | YES | ('') |
| FILESTORAGEID | int |  | YES | (NULL) |
| NUMBEROFTRIES | int |  | YES | ((0)) |

## RequestScrubInfo
**Physical table:** `OSUSR_XST_REQUESTSCRUBINFO`  
**Description:** Entity to store temporarily the scrub information.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUESTID | bigint |  | YES | (NULL) |
| DATASCRUBTYPEID | int |  | YES | (NULL) |
| ISPROCESSED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| NRTRIES | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | -1 | YES | ('') |

## RequestType
**Physical table:** `OSUSR_XST_REQUESTTYPE1`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
