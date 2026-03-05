# Zendesk_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [AsyncProcessType](#asyncprocesstype)
- [CustomerOrganization](#customerorganization)
- [GlobalUsersToSync](#globaluserstosync)
- [MergeUsers](#mergeusers)

## AsyncProcess
**Physical table:** `OSUSR_dm2_AsyncProcess`  
**Description:** Auxiliar entity that contains all waivers asynchronous processes, which will run through the Waivers_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ASYNCPROCESSTYPEID | int |  | YES | (NULL) |

## AsyncProcessType
**Physical table:** `OSUSR_dm2_AsyncProcessType`  
**Description:** contains all timers and BPTs that can run asynchronously through the Membership_AP  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CustomerOrganization
**Physical table:** `OSUSR_lab_TenantOrganization`  
**Description:** This holds the Customer id from Wodify and organization id from Zendesk. This is kept so we don't have to search for a Customer's organization id whenever we make an update to a Customer/user. The IsBootstrapped flag is updated after the bootstrap timer has been ran for a given Customer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORGANIZATIONID | nvarchar | 50 | YES | ('') |
| ISBOOTSTRAPPED | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |

## GlobalUsersToSync
**Physical table:** `OSUSR_dm2_GlobalUsersToSync`  
**Description:** Temporary table to store the users that are not in Zendesk  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| LASTPROCESSEDUSERID | int |  | YES | (NULL) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| REACTIVATE | bit |  | YES | ((0)) |

## MergeUsers
**Physical table:** `OSUSR_dm2_MergeUsers`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERIDTOBEMERGED | int |  | YES | (NULL) |
| USEREMAILTOBEMERGED | nvarchar | 250 | YES | ('') |
| PRIMARYUSERID | int |  | YES | (NULL) |
| PRIMARYUSEREMAIL | nvarchar | 250 | YES | ('') |
| PROCESSEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
