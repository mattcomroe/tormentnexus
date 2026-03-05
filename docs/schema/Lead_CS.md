# Lead_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [DropIn](#dropin)
- [Lead](#lead)
- [LeadConversionBoardCustomizedCardOption](#leadconversionboardcustomizedcardoption)
- [LeadConversionBoardSetting](#leadconversionboardsetting)
- [LeadConversionBoardSettingStatus](#leadconversionboardsettingstatus)
- [LeadConversionBoardSortBy](#leadconversionboardsortby)
- [LeadCreatedFromSource](#leadcreatedfromsource)
- [LeadFileStorage](#leadfilestorage)
- [LeadFormAttributes](#leadformattributes)
- [LeadGroup](#leadgroup)
- [LeadGroupParticipant](#leadgroupparticipant)
- [LeadGroupParticipantType](#leadgroupparticipanttype)
- [LeadStatus](#leadstatus)
- [LeadStatusActivityFeed](#leadstatusactivityfeed)
- [LeadStatusStatic](#leadstatusstatic)
- [Request](#request)
- [RequestType](#requesttype)

## AsyncProcess
**Physical table:** `OSUSR_1sp_AsyncProcess1`  
**Description:** Auxiliar entity that contains all asynchronous processes, which will run through the AP module in BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## DropIn
**Physical table:** `OSUSR_1sp_DropIn`  
**Description:** Unregistered drop-in identity (pre-Lead/Client) only. Do not insert for existing Leads/Clients.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DROPINGUID | nvarchar | 50 | YES | ('') |
| NAME | nvarchar | 101 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| NORMALIZEDEMAIL | nvarchar | 250 | YES | ('') |
| CONVERTEDTOLEAD | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| GENDERID | int |  | YES | (NULL) |
| PHONE | nvarchar | 20 | YES | ('') |
| INTERNATIONALPHONE | nvarchar | 20 | YES | ('') |
| STREETADDRESS1 | nvarchar | 200 | YES | ('') |
| STREETADDRESS2 | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| STATE | nvarchar | 50 | YES | ('') |
| PROVINCE | nvarchar | 50 | YES | ('') |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| DATEOFBIRTH | datetime |  | YES | ('1900-01-01 00:00:00') |
| AGE | int |  | YES | ((0)) |
| EMERGENCYCONTACTNAME | nvarchar | 100 | YES | ('') |
| EMERGENCYCONTACTPHONENUMBER | nvarchar | 20 | YES | ('') |
| COMMENTS | nvarchar | 2000 | YES | ('') |
| SMSTOLLFREESUBSCRIBED | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| PARENTGUARDIANFULLNAME | nvarchar | 101 | YES | ('') |
| ISDEPENDENT | bit |  | YES | ((0)) |
| LOCATIONID | int |  | YES | (NULL) |
| DROPINSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TOTALCLASSSIGNINS | int |  | YES | ((0)) |

## Lead
**Physical table:** `OSUSR_72o_Leads`  
**Description:** Contains Lead's data  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 101 | YES | ('') |
| TENANT | int |  | YES | (NULL) |
| CITY | nvarchar | 50 | YES | ('') |
| STATE | nvarchar | 50 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| PHONE | nvarchar | 20 | YES | ('') |
| COMMENTS | nvarchar | 2000 | YES | ('') |
| PICKLISTVALUEID | int |  | YES | (NULL) |
| STATEID | int |  | YES | (NULL) |
| PROVINCE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| OPENS | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| LASTCONTACT | datetime |  | YES | ('1900-01-01 00:00:00') |
| SOURCEPICKLISTVALUEID | int |  | YES | (NULL) |
| REFERRINGUSER | int |  | YES | (NULL) |
| LEADTYPEPICKLISTID | int |  | YES | (NULL) |
| LEADSOURCEPICKLISTID | int |  | YES | (NULL) |
| CONVERTEDTOUSER | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| REFERREDBYFROMWEB | nvarchar | 1000 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| GENDERID | int |  | YES | (NULL) |
| LEADSTATUSPICKLISTVALUEID | int |  | YES | (NULL) |
| LEADSOURCEPICKLISTVALUEID | int |  | YES | (NULL) |
| INTERNATIONALPHONE | nvarchar | 20 | YES | ('') |
| SMSSUBSCRIBED | bit |  | YES | ((0)) |
| CREATEDONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| STREETADDRESS1 | nvarchar | 200 | YES | ('') |
| STREETADDRESS2 | nvarchar | 50 | YES | ('') |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| DATEOFBIRTH | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMERGENCYCONTACTNAME | nvarchar | 100 | YES | ('') |
| EMERGENCYCONTACTPHONENUMBER | nvarchar | 20 | YES | ('') |
| LEADCREATEDFROMSOURCEID | int |  | YES | (NULL) |
| MASSEMAILSUBSCRIBED | bit |  | YES | ((0)) |
| UNIQUEKEY | nvarchar | 25 | YES | ('') |
| TRANSACTIONALEMAILSUBSCRIBED | bit |  | YES | ((0)) |
| AGE | int |  | YES | ((0)) |
| CLOUDINARYFILEID | int |  | YES | (NULL) |
| CAMEFROMFULLCONTACT | bit |  | YES | ((0)) |
| HASREMOVEDPICTURE | bit |  | YES | ((0)) |
| AFFINITYLASTRUNON | datetime |  | YES | ('1900-01-01 00:00:00') |
| AFFINITYRUNNINGSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| LOCATIONID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SMSTOLLFREESUBSCRIBED | bit |  | YES | ((0)) |
| GROUPPARTICIPANTTYPEID | int |  | YES | ((0)) |
| LEADSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| LEADOWNERID | int |  | YES | (NULL) |
| TOTALCLASSSIGNINS | int |  | YES | ((0)) |
| TOTALBOOKINGCHECKINS | int |  | YES | ((0)) |
| TOTALBOOKINGSIGNINS | int |  | YES | ((0)) |
| LASTCLASSSIGNIN | datetime |  | YES | ('1900-01-01 00:00:00') |
| LASTBOOKINGSIGNIN | datetime |  | YES | ('1900-01-01 00:00:00') |
| LEADGUID | nvarchar | 36 | YES | ('') |
| LEADSTATUSID | int |  | YES | (NULL) |

## LeadConversionBoardCustomizedCardOption
**Physical table:** `OSUSR_1sp_LeadBoardCustomizedCards`  
**Description:** Lead Conversion Board Customized Card options  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## LeadConversionBoardSetting
**Physical table:** `OSUSR_1sp_LeadCard`  
**Description:** Lead Conversion Board settings for a user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| LEADBOARDSORTBYID | int |  | YES | (NULL) |
| CUSTOMIZEDOPTION1 | int |  | YES | (NULL) |
| CUSTOMIZEDOPTION2 | int |  | YES | (NULL) |
| CUSTOMIZEDOPTION3 | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| LEADCONVERSIONBOARDSORTBYID | int |  | YES | (NULL) |
| ISSORTASCENDING | bit |  | YES | ((0)) |
| ISTOSHOWRESERVATIONSTATUS | bit |  | YES | ((0)) |
| USERID | int |  | YES | (NULL) |
| DISQUALIFIEDTIMEFRAMEID | int |  | YES | ((0)) |
| CONVERTEDTIMEFRAMEID | int |  | YES | ((0)) |

## LeadConversionBoardSettingStatus
**Physical table:** `OSUSR_1sp_LeadCardStatuses`  
**Description:** Extends LeadConversionBoardSettings to allow selection of multiple statuses  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LEADCARDID | bigint |  | YES | (NULL) |
| LEADBOARDSTATUSID | int |  | YES | (NULL) |
| LEADSTATUS | bigint |  | YES | ((0)) |
| LEADCONVERSIONBOARDSETTINGID | bigint |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| LEADSTATUSID | bigint |  | YES | ((0)) |
| LEADSTATUSID_NEW | int |  | YES | (NULL) |

## LeadConversionBoardSortBy
**Physical table:** `OSUSR_1sp_LeadBoardSortBy`  
**Description:** Lead Conversion Board sort by types  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## LeadCreatedFromSource
**Physical table:** `OSUSR_72o_LeadCreatedFromSource`  
**Description:** possible records for where was the lead created from  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| DESCRIPTION | nvarchar | 50 | YES | ('') |

## LeadFileStorage
**Physical table:** `OSUSR_ov4_LeadRackspaceFile`  
**Description:** Contains all the FileStorage associated with the Lead  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LEADID | int |  | YES | (NULL) |
| RACKSPACEID | int |  | YES | (NULL) |
| FILESTORAGEID | int |  | YES | (NULL) |

## LeadFormAttributes
**Physical table:** `OSUSR_72o_LeadFormAttributes`  
**Description:** For the dynamic lead form, contains the possible mandatory and optional attributes for that form  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_SELECTED | bit |  | YES | ((0)) |
| IS_MANDATORY | bit |  | YES | ((0)) |
| ISSELECTED | bit |  | YES | ((0)) |
| ISMANDATORY | bit |  | YES | ((0)) |
| FIELDNAME | nvarchar | 50 | YES | ('') |
| FIELDTYPE | nvarchar | 50 | YES | ('') |
| FIELDLENGTH | int |  | YES | ((0)) |
| USAONLY | bit |  | YES | ((0)) |

## LeadGroup
**Physical table:** `OSUSR_1sp_LeadGroup`  
**Description:** The group of leads  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## LeadGroupParticipant
**Physical table:** `OSUSR_1sp_LeadGroupParticipant`  
**Description:** Contains a group of leads with types within a group  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LEADGROUPID | bigint |  | YES | (NULL) |
| LEADGROUPPARTICIPANTTYPEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |

## LeadGroupParticipantType
**Physical table:** `OSUSR_1sp_LeadGroupParticipantType`  
**Description:** Lead Group participant type (for instance guardians, members, dependents)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## LeadStatus
**Physical table:** `OSUSR_1sp_LeadStatus`  
**Description:** Defines the possible Values for Lead status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LEADSTATUSSTATICID | int |  | YES | (NULL) |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| ISSYSTEMVALUE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## LeadStatusActivityFeed
**Physical table:** `OSUSR_1sp_LeadStatusActivityFeed`  
**Description:** Connects Status History with the Lead  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LEADID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| FROMLEADSTATUSID | int |  | YES | (NULL) |
| TOLEADSTATUSID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## LeadStatusStatic
**Physical table:** `OSUSR_1sp_LeadStatusStatic`  
**Description:** List of bootstrapped lead status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| ISUSERSELECTABLE | bit |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_1sp_Request`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |
| ISACTIVATE | bit |  | YES | ((0)) |
| ACCOUNTID | nvarchar | 50 | YES | ('') |
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

## RequestType
**Physical table:** `OSUSR_1sp_RequestType`  
**Description:** Type of request record  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
