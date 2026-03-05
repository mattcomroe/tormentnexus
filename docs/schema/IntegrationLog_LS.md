# IntegrationLog_LS

## Tables

- [IntegrationAction](#integrationaction)
- [IntegrationActionPartner](#integrationactionpartner)
- [IntegrationIndexStatus](#integrationindexstatus)
- [IntegrationLogIntKey](#integrationlogintkey)
- [IntegrationPartner](#integrationpartner)
- [IntegrationStatus](#integrationstatus)
- [IntegrationStatusRecordIntKey](#integrationstatusrecordintkey)
- [IntegrationUserType](#integrationusertype)
- [LogRetention](#logretention)
- [ParentReferenceEntity](#parentreferenceentity)
- [ReferenceEntity](#referenceentity)

## IntegrationAction
**Physical table:** `OSUSR_vg7_IntegrationAction1`  
**Description:** Used to filter logs by Integration Action.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 250 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| INTEGRATIONPARTNERID | int |  | YES | (NULL) |

## IntegrationActionPartner
**Physical table:** `OSUSR_dl3_IntegrationActionPartner1`  
**Description:** Indicates which integration partners use integration actions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INTEGRATIONACTIONID | int |  | YES | (NULL) |
| INTEGRATIONPARTNERID | int |  | YES | (NULL) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## IntegrationIndexStatus
**Physical table:** `OSUSR_vg7_IntegrationIndexStatus1`  
**Description:** Status to show wether or not this records has been send to a provider to be indexed for fast full text searching.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |

## IntegrationLogIntKey
**Physical table:** `OSUSR_vg7_IntegrationLogIntKey`  
**Description:** Entity that support inserts via the CreateAsynchLog Action.  Records are placed in message queue and inserted in batch.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| TENANTID | int |  | YES | (NULL) |
| INTEGRATIONACTIONID | int |  | YES | (NULL) |
| INTEGRATIONPARTNERID | int |  | YES | (NULL) |
| PARENTREFERENCEENTITYID | int |  | YES | (NULL) |
| PARENTREFERENCERECORDID | int |  | YES | ((0)) |
| REFERENCEENTITYID | int |  | YES | (NULL) |
| REFERENCERECORDID | int |  | YES | ((0)) |
| REQUEST | nvarchar | -1 | YES | ('') |
| REQUESTON | datetime |  | YES | ('1900-01-01 00:00:00') |
| REQUESTBY | int |  | YES | (NULL) |
| RESPONSE | nvarchar | -1 | YES | ('') |
| RESPONSEON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HASEXCEPTION | bit |  | YES | ((0)) |
| EXCEPTION | nvarchar | -1 | YES | ('') |
| EXCEPTIONON | datetime |  | YES | ('1900-01-01 00:00:00') |
| INTEGRATIONINDEXSTATUSID | int |  | YES | (NULL) |
| INDEXEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| INDEXTRIES | int |  | YES | ((0)) |
| INDEXTRIEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| INDEXEXCEPTION | nvarchar | 500 | YES | ('') |
| DELETETRIES | int |  | YES | ((0)) |
| DELETETRIEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| DELETEEXCEPTION | nvarchar | 500 | YES | ('') |
| INTEGRATIONUSERTYPEID | int |  | YES | (NULL) |
| INTEGRATIONUSERID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |

## IntegrationPartner
**Physical table:** `OSUSR_vg7_IntegrationPartner1`  
**Description:** Used to filter Logs by Partner  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## IntegrationStatus
**Physical table:** `OSUSR_vg7_IntegrationStatus1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## IntegrationStatusRecordIntKey
**Physical table:** `OSUSR_vg7_IntegrationStatusRecordIntKey`  
**Description:** Many to Many table to get Integration Status of Record.  WARNING: RecordId is set as an Integer to support tracking many entitites inside of one table. When building a query, it is critically important to create a join that uses the function EntityRefIntegerToInteger().   It is also important to filter on the RequestReferenceEntityId. Failure to do so could result in reading records from another entity.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| REQUESTPARTNERID | int |  | YES | (NULL) |
| REQUESTREFERENCEENTITYID | int |  | YES | (NULL) |
| REFERENCERECORDID | int |  | YES | ((0)) |
| INTEGRATIONSTATUSID | int |  | YES | (NULL) |
| TRIES | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## IntegrationUserType
**Physical table:** `OSUSR_dl3_IntegrationUserType`  
**Description:** Type of user associated to the integration lol record.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## LogRetention
**Physical table:** `OSUSR_vg7_RefernceEntityLogRetention1`  
**Description:** Number of days integration logs are kept. The default number is set in a site property. Inserting records here will override that default value.  If you override the default value for a specific action or entity, be sure to specify values for every possible entity or integration action for that integratyion partner, otherwise those will be retained forever.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| REQUESTPARTNERID | int |  | YES | (NULL) |
| REFERENCEENTITYID | int |  | YES | (NULL) |
| PARTNERRETENTIONDAYS | int |  | YES | ((0)) |
| INDEXRETENTIONDAYS | int |  | YES | ((0)) |
| INTEGRATIONACTIONID | int |  | YES | (NULL) |

## ParentReferenceEntity
**Physical table:** `OSUSR_vg7_ParentReferenceEntity1`  
**Description:** Optional Parent Entity Input to model parent child relationships like (Invoice and Transcation).  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| URI | nvarchar | 500 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ReferenceEntity
**Physical table:** `OSUSR_vg7_ReferenceEntity1`  
**Description:** Used to fitler Logs by Entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| URI | nvarchar | 500 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
