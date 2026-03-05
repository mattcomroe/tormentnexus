# LogEvents_CS

## Tables

- [EventProcessingStatus](#eventprocessingstatus)
- [EventType](#eventtype)
- [MAndBTimerLog](#mandbtimerlog)
- [MAndBUserQueueS3SNS](#mandbuserqueues3sns)
- [UnorderedEvent](#unorderedevent)

## EventProcessingStatus
**Physical table:** `OSUSR_CH5_EVENTPROCESSINGSTATUS`  
**Description:** Keeps track of the last event order number that was processed, for each event type.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| EVENTTYPEID | int |  | NO |  |
| LASTPROCESSEDORDER | bigint |  | YES | ((0)) |

## EventType
**Physical table:** `OSUSR_CH5_EVENTTYPE`  
**Description:** This will contain all the Event types available to use for Amazon SNS Events  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| DBSEQUENCENAME | nvarchar | 50 | YES | ('') |
| CODE | nvarchar | 50 | YES | ('') |

## MAndBTimerLog
**Physical table:** `OSUSR_CH5_MANDBTIMERLOG`  
**Description:** Temporary table that contains all needed information regarding Membership and Billing Timer to log: - When the Timer started and ended - How many Triggers per timer were going to be launched - How many Triggers per timer were actually launched - How many CloudSearch API calls we got -  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TIMERSTARTEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| TIMERENDEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| NUMBEROFS3SNSCALLS | int |  | YES | ((0)) |
| NUMBEROFUNIQUES3SNSCALLS | int |  | YES | ((0)) |
| NUMBEROFCLOUDSEARCHAPICALLS | int |  | YES | ((0)) |
| ISTIMERBUSINESSPROCESSRUNNIN | bit |  | YES | ((0)) |
| TIMERBUSINESSPROCESSENDEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| S3SNSTRIGGERSTARTEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| S3SNSTRIGGERENDEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| CSSYNCSTARTEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| CSSYNCENDEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | ((0)) |

## MAndBUserQueueS3SNS
**Physical table:** `OSUSR_CH5_MANDBUSERQUEUES3SNS`  
**Description:** Contains all users that will be triggered to S3/SNS  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| USERID | int |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | ((0)) |

## UnorderedEvent
**Physical table:** `OSUSR_CH5_UNORDEREDEVENT`  
**Description:** Events that were received out of order.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EVENTORDER | bigint |  | YES | ((0)) |
| EVENTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| EVENTTYPEID | int |  | YES | (NULL) |
| EVENTJSON | nvarchar | -1 | YES | ('') |
