# Waiver_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [BulkFile](#bulkfile)
- [Request](#request)
- [RequestType](#requesttype)
- [SendByEmailBulkRequest](#sendbyemailbulkrequest)
- [SignedWaiverToSend](#signedwaivertosend)
- [UserMissingWaiver](#usermissingwaiver)
- [UserSignedWaiver](#usersignedwaiver)
- [UserSignedWaiverAnswer](#usersignedwaiveranswer)
- [UserSignedWaiverSource](#usersignedwaiversource)
- [Waiver](#waiver)
- [WaiverBasicDetail](#waiverbasicdetail)
- [WaiverBasicDetailType](#waiverbasicdetailtype)
- [WaiverLink](#waiverlink)
- [WaiverMultipleChoiceAnswer](#waivermultiplechoiceanswer)
- [WaiverPersonalInfo](#waiverpersonalinfo)
- [WaiverProgram](#waiverprogram)
- [WaiverQuestion](#waiverquestion)
- [WaiverQuestionType](#waiverquestiontype)
- [WaiverStatus](#waiverstatus)
- [WhoSignsWaiver](#whosignswaiver)

## AsyncProcess
**Physical table:** `OSUSR_G9L_ASYNCPROCESS`  
**Description:** Auxiliar entity that contains all waivers asynchronous processes, which will run through the Waivers_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## BulkFile
**Physical table:** `OSUSR_G9L_BULKFILE`  
**Description:** Zip file containing several files to be sent to the user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SENDBYEMAILBULKID | bigint |  | YES | (NULL) |
| FILEKEY | nvarchar | 100 | YES | ('') |
| FILENAME | nvarchar | 100 | YES | ('') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Request
**Physical table:** `OSUSR_6AO_REQUEST`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| REQUESTTYPEID | int |  | YES | (NULL) |
| USERSIGNEDWAIVERID | int |  | YES | (NULL) |
| WAIVERID | int |  | YES | (NULL) |
| WASWAIVERUPDATED | bit |  | YES | ((0)) |
| ISRUNNINGSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISMANUALLYRETRIED | bit |  | YES | ((0)) |
| RETRIEDBY | int |  | YES | (NULL) |
| NUMBEROFRETRIES | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| NUMBEROFTRIES | int |  | YES | ((0)) |
| HASFINISHED | bit |  | YES | ((0)) |
| USERID | int |  | YES | (NULL) |
| LEADID | bigint |  | YES | ((0)) |
| LOCATIONID | bigint |  | YES | ((0)) |
| REGENERATEWAIVERS | bit |  | YES | ((0)) |
| REGENERATECONTRACTS | bit |  | YES | ((0)) |
| LASTFINISHEDSIGNEDCONTRACTID | bigint |  | YES | ((0)) |
| LASTFINISHEDSIGNEDWAIVERID | bigint |  | YES | ((0)) |
| CONTRACTSSIGNEDAFTER | datetime |  | YES | ('1900-01-01 00:00:00') |
| ATTRIBUTES | nvarchar | 2000 | YES | ('') |

## RequestType
**Physical table:** `OSUSR_6AO_REQUESTTYPE`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## SendByEmailBulkRequest
**Physical table:** `OSUSR_G9L_SENDBYEMAILBULKREQUEST`  
**Description:** Stores the exports to be sent to the user as a zip file  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISFINISHED | bit |  | YES | ((0)) |

## SignedWaiverToSend
**Physical table:** `OSUSR_G9L_SIGNEDWAIVERTOSEND`  
**Description:** Signed Waiver to send  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SENDBYEMAILBULKID | bigint |  | YES | (NULL) |
| USERSIGNEDWAIVERID | int |  | YES | (NULL) |
| ISPROCESSED | bit |  | YES | ((0)) |
| ISERROR | bit |  | YES | ((0)) |

## UserMissingWaiver
**Physical table:** `OSUSR_72O_USERMISSINGWAIVER`  
**Description:** Contain user or lead that misses any waivers that they need to sign  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| EMAIL | nvarchar | 250 | YES | ('') |
| GENDERID | int |  | YES | (NULL) |
| DOB | datetime |  | YES | ('1900-01-01 00:00:00') |
| WAIVERID | int |  | YES | (NULL) |
| WAIVERNUMBER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| ISDELETED | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DROPINID | bigint |  | YES | (NULL) |

## UserSignedWaiver
**Physical table:** `OSUSR_72O_USERSIGNEDWAIVER`  
**Description:** Signed Waivers  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| WAIVERID | int |  | YES | (NULL) |
| SIGNEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| NAME | nvarchar | 256 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| USERSIGNATURE | varbinary | -1 | YES | (NULL) |
| WAIVERATTACHMENTID | int |  | YES | (NULL) |
| ATHLETESTATUSID | int |  | YES | (NULL) |
| IS_DROPIN | bit |  | YES | ((0)) |
| USERSIGNATURETEXT | nvarchar | -1 | YES | ('') |
| USERSIGNATUREFILENAME | nvarchar | 150 | YES | ('') |
| INITIALS | nvarchar | 5 | YES | ('') |
| PARENTGUARDIANFULLNAME | nvarchar | 101 | YES | ('') |
| WAIVERPERSONALINFOID | int |  | YES | (NULL) |
| CLOUDINARYFILEID | int |  | YES | (NULL) |
| UNIQUEID | nvarchar | 50 | YES | ('') |
| DROPINUSERID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| WAIVERNUMBER | int |  | YES | ((0)) |
| ISCURRENT | bit |  | YES | ((0)) |
| ATHLETESTATUSPICKLISTVALUEID | int |  | YES | (NULL) |
| LEADSTATUSPICKLISTVALUEID | int |  | YES | (NULL) |
| CONVERTEDFROMLEADID | int |  | YES | (NULL) |
| USERSIGNEDWAIVERSOURCEID | int |  | YES | (NULL) |
| ISMOBILE | bit |  | YES | ((0)) |
| ISDROPIN | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| RACKSPACEFILEID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| RACKSPACEID | int |  | YES | (NULL) |
| FILESTORAGEID | int |  | YES | (NULL) |
| HASAGREEDTOELECTRONICRECORDS | bit |  | YES | ((0)) |
| EXTERNALIMAGEID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LEADSTATUSID | int |  | YES | (NULL) |
| DROPINGUID | nvarchar | 36 | YES | ('') |
| DROPINID | bigint |  | YES | (NULL) |

## UserSignedWaiverAnswer
**Physical table:** `OSUSR_72O_USERSIGNEDWAIVERANSWER`  
**Description:** Answers  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| WAIVERQUESTIONID | int |  | YES | (NULL) |
| WAIVERMULTCHOICEANSWERID | int |  | YES | (NULL) |
| YESNO | bit |  | YES | ((0)) |
| FREEFORMANSWER | nvarchar | 1500 | YES | ('') |
| USERSIGNEDWAIVERID | int |  | YES | (NULL) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| FOLLOWUPANSWER | nvarchar | 1500 | YES | ('') |
| LEADID | int |  | YES | (NULL) |
| YESNOINTVAL | int |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## UserSignedWaiverSource
**Physical table:** `OSUSR_72O_USERSIGNEDWAIVERSOURCE`  
**Description:** Where the waiver was signed  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Waiver
**Physical table:** `OSUSR_72O_WAIVER`  
**Description:** Contains information of a waiver  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 50 | YES | ('') |
| WAIVERTERMS | nvarchar | -1 | YES | ('') |
| WAIVEREMAILTEMPLATE | nvarchar | -1 | YES | ('') |
| WAIVERCOPIEDFROMID | int |  | YES | (NULL) |
| WAIVERCOPIEDTOID | int |  | YES | (NULL) |
| WAIVERSTATUSID | int |  | YES | (NULL) |
| VERSION | decimal |  | YES | ((0)) |
| IS_CURRENT | bit |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| WAIVERNUMBER | int |  | YES | ((0)) |
| RESIGNWAIVER | bit |  | YES | ((0)) |
| HISTORY | nvarchar | -1 | YES | ('') |
| ISCURRENT | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| SUBJECT | nvarchar | 500 | YES | ('') |
| SUPPRESSEMAILS | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| WHOSIGNSWAIVERID | int |  | YES | (NULL) |
| DROPINSUPPORT | bit |  | YES | ((0)) |
| DROPINSUPPORTQUESTIONS | bit |  | YES | ((1)) |

## WaiverBasicDetail
**Physical table:** `OSUSR_72O_WAIVERBASICDETAIL`  
**Description:** Waiver Basic Detail  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| WAIVERID | int |  | YES | (NULL) |
| WAIVERBASICDETAILTYPEID | int |  | YES | (NULL) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | nvarchar | 50 | YES | ('') |

## WaiverBasicDetailType
**Physical table:** `OSUSR_72O_WAIVERBASICDETAILTYPE`  
**Description:** The basic detail type of a waiver  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| IS_REQUIRED | bit |  | YES | ((0)) |

## WaiverLink
**Physical table:** `OSUSR_72O_WAIVERLINK`  
**Description:** WaiverLink  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| LINKTOKEN | nvarchar | 100 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| WAIVERID | int |  | YES | (NULL) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CONVERTTOLEAD | bit |  | YES | ((0)) |
| LOCATIONID | int |  | YES | (NULL) |
| CREATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| EMAIL | nvarchar | 250 | YES | ('') |
| DROPINID | bigint |  | YES | (NULL) |

## WaiverMultipleChoiceAnswer
**Physical table:** `OSUSR_72O_WAIVERMULTIPLECHOICEANSWER`  
**Description:** Answers to a multiple choice question  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| WAIVERID | int |  | YES | (NULL) |
| WAIVERQUESTIONID | int |  | YES | (NULL) |
| ANSWER | nvarchar | 100 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## WaiverPersonalInfo
**Physical table:** `OSUSR_72O_WAIVERPERSONALINFO`  
**Description:** Personal information for a user or lead  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| WAIVERID | int |  | YES | (NULL) |
| USERSIGNEDWAIVERID | int |  | YES | (NULL) |
| FULLNAME | nvarchar | 256 | NO | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| GENDERID | int |  | YES | (NULL) |
| STREETADDRESS | nvarchar | 200 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| DATEOFBIRTH | datetime |  | YES | ('1900-01-01 00:00:00') |
| PHONE | nvarchar | 20 | YES | ('') |
| EMERGENCYCONTACT | nvarchar | 100 | YES | ('') |
| EMERGENCYCONTACTPHONE | nvarchar | 20 | YES | ('') |
| LEADID | int |  | YES | (NULL) |
| PROVINCE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| ISONLINESALESPORTAL | bit |  | YES | ((0)) |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| LEADSOURCEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SMSTOLLFREESUBSCRIBED | bit |  | YES | ((0)) |
| STREETADDRESS2 | nvarchar | 200 | YES | ('') |
| DROPINID | bigint |  | YES | (NULL) |

## WaiverProgram
**Physical table:** `OSUSR_72O_WAIVERPROGRAM`  
**Description:** Contains reference between waivers and gym program by customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| WAIVERID | int |  | YES | (NULL) |
| PROGRAMID | int |  | YES | (NULL) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| WAIVERNUMBER | int |  | YES | ((0)) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## WaiverQuestion
**Physical table:** `OSUSR_72O_WAIVERQUESTION`  
**Description:** Waiver question and answers  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| WAIVERID | int |  | YES | (NULL) |
| WAIVERQUESTIONTYPEID | int |  | YES | (NULL) |
| QUESTION | nvarchar | 150 | YES | ('') |
| ANSWERS | nvarchar | 1500 | YES | ('') |
| ALLOWMULTIPLEANSWERS | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| IS_REQUIRED | bit |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| FOLLOWUPQUESTION | nvarchar | 150 | YES | ('') |
| PARENTQUESTIONID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| IS_YES_FOLLOWUP_REQUIRED | bit |  | YES | ((0)) |
| IS_NO_FOLLOWUP_REQUIRED | bit |  | YES | ((0)) |
| NORESPONSEFOLLOWUPQUESTION | nvarchar | 150 | YES | ('') |

## WaiverQuestionType
**Physical table:** `OSUSR_72O_WAIVERQUESTIONTYPE`  
**Description:** The type of question  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## WaiverStatus
**Physical table:** `OSUSR_72O_WAIVERSTATUS`  
**Description:** The status type of the waiver  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## WhoSignsWaiver
**Physical table:** `OSUSR_6AO_WHOSIGNSWAIVER`  
**Description:** Contains all the needed records to select who needs to sign a specific waiver  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 60 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
