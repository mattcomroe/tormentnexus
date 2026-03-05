# StatusHistory_CS

## Tables

- [StatusHistory](#statushistory)

## StatusHistory
**Physical table:** `OSUSR_72O_LEADHISTORY`  
**Description:** User's status history  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| LEADID | int |  | YES | (NULL) |
| FROMSTATUS | int |  | YES | (NULL) |
| TOSTATUS | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| USERID | int |  | YES | (NULL) |
| CURRENTLOCATIONID | int |  | YES | (NULL) |
| CURRENTPROGRAMID | int |  | YES | (NULL) |
| CREATEDONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| FROMLOCATIONID | int |  | YES | (NULL) |
| CURRENTGYMPROGRAMID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
