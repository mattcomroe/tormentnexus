# ScraperServices_CS

## Tables

- [Certification](#certification)
- [Coach](#coach)
- [CoachCertifications](#coachcertifications)
- [CoachUsers](#coachusers)
- [NewCoachForHubspot](#newcoachforhubspot)
- [RecordQueue](#recordqueue)
- [RecordQueueStatus](#recordqueuestatus)
- [Scrape](#scrape)
- [ScrapeState](#scrapestate)
- [ScrapeStateStatus](#scrapestatestatus)

## Certification
**Physical table:** `OSUSR_B94_CERTIFICATIONS`  
**Description:** List of Certifications that can be filtered on in the CrossFit Trainer Directory  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| SOURCEORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CODE | nvarchar | 50 | YES | ('') |
| DISPLAYORDER | int |  | YES | ((0)) |
| ISSELECTED | bit |  | YES | ((0)) |
| SOURCENAME | nvarchar | 50 | YES | ('') |

## Coach
**Physical table:** `OSUSR_B94_COACHES`  
**Description:** List of Coaches retrieved from the CrossFit Trainer Directory  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| STATE | nvarchar | 50 | YES | ('') |
| COUNTRY | nvarchar | 50 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| LASTMATCHEDTOUSER | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDSCRAPEID | bigint |  | YES | (NULL) |
| UPDATEDSCRAPEID | bigint |  | YES | (NULL) |

## CoachCertifications
**Physical table:** `OSUSR_B94_COACHESCERTIFICATIONS`  
**Description:** Which certifications does each coach have  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COACHID | bigint |  | YES | (NULL) |
| CERTIFICATIONID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDSCRAPEID | bigint |  | YES | (NULL) |
| UPDATEDSCRAPEID | bigint |  | YES | (NULL) |

## CoachUsers
**Physical table:** `OSUSR_B94_COACHESUSERS`  
**Description:** Mapping between a Coach and a Wodify User  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COACHID | bigint |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| MATCHTYPE | nvarchar | 50 | YES | ('') |
| CUSTOMERACTIVE | bit |  | YES | ((0)) |
| CLIENTACTIVE | bit |  | YES | ((0)) |
| LASTLOGIN | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLIENTROLES | nvarchar | 50 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| MATCHORDER | int |  | YES | ((0)) |
| CREATEDSCRAPEID | bigint |  | YES | (NULL) |
| UPDATEDSCRAPEID | bigint |  | YES | (NULL) |

## NewCoachForHubspot
**Physical table:** `OSUSR_B94_NEWCOACHFORHUBSPOT4`  
**Description:** Holds Coach records that will be passed over to Hubspot  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COACHUSERID | bigint |  | YES | ((0)) |
| SCRAPEID | bigint |  | YES | (NULL) |
| INHUBSPOT | bit |  | YES | ((0)) |

## RecordQueue
**Physical table:** `OSUSR_B94_RECORDQUEUE`  
**Description:** Contains unprocessed HTML table row for the Trainer Directory Record  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ROWCONTENTS | nvarchar | -1 | YES | ('') |
| RECORDQUEUESTATUSID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SCRAPEID | bigint |  | YES | (NULL) |

## RecordQueueStatus
**Physical table:** `OSUSR_B94_RECORDQUEUESTATUS`  
**Description:** Status of the record queue record  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Scrape
**Physical table:** `OSUSR_B94_SCRAPE`  
**Description:** Record of Scrapes  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ScrapeState
**Physical table:** `OSUSR_B94_SCRAPESTATE`  
**Description:** Contains the states we want to scrape over along with the current status. Default status is Done, gets set to Waiting when a scrape starts.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STATEID | int |  | YES | (NULL) |
| SCRAPESTATESSTATUSID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SCRAPESTATESTATUSID | int |  | YES | (NULL) |
| SCRAPEID | bigint |  | YES | (NULL) |

## ScrapeStateStatus
**Physical table:** `OSUSR_B94_SCRAPESTATESTATUS`  
**Description:** Contains the status of the scrape state  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
