# W_Utils_CS

## Tables

- [GeneralListenerRequestType](#generallistenerrequesttype)
- [LoginSource](#loginsource)
- [Picklist](#picklist)
- [PicklistType](#picklisttype)
- [PicklistValue](#picklistvalue)
- [PicklistValueType](#picklistvaluetype)
- [TimeFormat](#timeformat)

## GeneralListenerRequestType
**Physical table:** `OSUSR_SZ1_GENERALLISTENERREQUESTTYPE1`  
**Description:** Type of Request that triggers the General Listener  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| DESCRIPTION | nvarchar | 300 | YES | ('') |

## LoginSource
**Physical table:** `OSUSR_72O_LOGINSOURCE`  
**Description:** Contains the possible sources of login  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## Picklist
**Physical table:** `OSUSR_72O_PICKLIST`  
**Description:** Defines the Picklists to be used for drop downs  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PICKLISTTYPEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |

## PicklistType
**Physical table:** `OSUSR_72O_PICKLISTTYPE`  
**Description:** Contains all possible Types of Picklists  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| ISSYSTEMLIST | bit |  | YES | ((0)) |

## PicklistValue
**Physical table:** `OSUSR_72O_PICKLISTVALUE`  
**Description:** Defines the possible Values for a Picklist to be used in dropdowns  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PICKLISTID | int |  | YES | (NULL) |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISSYSTEMVALUE | bit |  | YES | ((0)) |
| PICKLISTVALUETYPEID | int |  | YES | (NULL) |
| ACCOUNTINGCHARTACCOUNT | nvarchar | 150 | YES | ('') |
| CUSTOMERID | bigint |  | YES | ((0)) |
| DESCRIPTION | nvarchar | 500 | YES | ('') |

## PicklistValueType
**Physical table:** `OSUSR_72O_PICKLISTVALUETYPE`  
**Description:** Contains the Types for PicklistValues  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| PICKLISTTYPEID | int |  | YES | (NULL) |
| ISUSERSELECTABLE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## TimeFormat
**Physical table:** `OSUSR_72O_TIMEFORMAT`  
**Description:** Contains all possible time formats  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| LABELPLURAL | nvarchar | 50 | YES | ('') |
| LABELSINGULAR | nvarchar | 50 | YES | ('') |
