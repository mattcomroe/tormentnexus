# AutomatedEmail_CS

## Tables

- [AsyncEmailTemplateRequest](#asyncemailtemplaterequest)
- [AsyncRetryRequest](#asyncretryrequest)
- [EmailTemplate](#emailtemplate)
- [EmailTemplateCopyHistory](#emailtemplatecopyhistory)
- [EmailTemplateCustomRow](#emailtemplatecustomrow)
- [EmailTemplateLineage](#emailtemplatelineage)
- [EmailTemplateUser](#emailtemplateuser)
- [GlobalEmailTemplate](#globalemailtemplate)
- [GlobalEmailTemplateEmailTemplateCustomRow](#globalemailtemplateemailtemplatecustomrow)
- [GlobalEmailTemplatePublishResponse](#globalemailtemplatepublishresponse)
- [GlobalEmailTemplateType](#globalemailtemplatetype)
- [GlobalEmailTemplateUser](#globalemailtemplateuser)
- [GlobalTemplateProcessType](#globaltemplateprocesstype)

## AsyncEmailTemplateRequest
**Physical table:** `OSUSR_by8_AsyncResetEmailTemplateWorkBucket`  
**Description:** Processes for email and global email template requests  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| GLOBALEMAILTEMPLATEID | bigint |  | YES | ((0)) |
| ISCOMPLETE | bit |  | YES | ((0)) |
| HASERROR | bit |  | YES | ((0)) |
| TRYCOUNT | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| GLOBALTEMPLATEVERSION | int |  | YES | ((0)) |
| PROCESSTYPE | int |  | YES | (NULL) |
| ISRUNNINGSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISMANUALLYRETRIED | bit |  | YES | ((0)) |
| RETRIEDBY | int |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| EMAILTEMPLATECUSTOMROWID | bigint |  | YES | ((0)) |
| EMAILTEMPLATEID | bigint |  | YES | ((0)) |
| ISGLOBALTEMPLATE | bit |  | YES | ((0)) |
| ISPROMOTETOTEST | bit |  | YES | ((0)) |
| ISPROMOTETOSTAGE | bit |  | YES | ((0)) |
| ISPROMOTETOPRODUCTION | bit |  | YES | ((0)) |
| AUTOEMAILSUBEMAILTEMPLATEID | bigint |  | YES | ((0)) |

## AsyncRetryRequest
**Physical table:** `OSUSR_by8_AsyncRetryRequest`  
**Description:** Processes for retrying failed events  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ASYNCEMAILTEMPLATEREQUESTID | bigint |  | YES | (NULL) |

## EmailTemplate
**Physical table:** `OSUSR_by8_EmailTemplate`  
**Description:** Table to store email template references (initially implemented for the BeePlugin)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| NAME | nvarchar | 250 | YES | ('') |
| TEMPLATEFILESTORAGEID | int |  | YES | (NULL) |
| HTMLFILESTORAGEID | int |  | YES | (NULL) |
| ISPUBLISHED | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| ISWORKFLOWEMAIL | bit |  | YES | ((0)) |
| SUBJECT | nvarchar | 500 | YES | ('') |
| ATTACHMENTFILEID | nvarchar | 50 | YES | ('') |
| ISMEDIALIBRARYATTACHMENT | bit |  | YES | ((0)) |
| THUMBNAILFILESTORAGEID | int |  | YES | (NULL) |
| VERSION | int |  | YES | ((0)) |
| TEMPLATEJSONS3KEY | nvarchar | 1024 | YES | ('') |
| TEMPLATEHTMLS3KEY | nvarchar | 1024 | YES | ('') |
| THUMBNAILS3KEY | nvarchar | 1024 | YES | ('') |
| ISLATESTVERSION | bit |  | YES | ((0)) |
| SOURCETEMPLATEID | bigint |  | YES | ((0)) |
| ISUPDATEDBYCUSTOMER | bit |  | YES | ((0)) |
| SOURCETEMPLATEVERSION | int |  | YES | ((0)) |
| LOCATIONID | int |  | YES | (NULL) |
| SOURCEGLOBALEMAILTEMPLATEID | bigint |  | YES | ((0)) |
| SOURCEGLOBALEMAILTEMPLATEVER | int |  | YES | ((0)) |
| GLOBALTEMPLATELASTPUBVERSION | int |  | YES | ((0)) |
| GLOBALTEMPLATEPUBLISHRESPONS | int |  | YES | (NULL) |

## EmailTemplateCopyHistory
**Physical table:** `OSUSR_by8_EmailTemplateCopyHistory`  
**Description:** Stores history of templates copied from other templates  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EMAILTEMPLATEID | bigint |  | YES | (NULL) |
| COPIEDFROMEMAILTEMPLATEID | bigint |  | YES | (NULL) |

## EmailTemplateCustomRow
**Physical table:** `OSUSR_by8_EmailTemplateCustomRow`  
**Description:** Table to store email template custom saved row references (initially implemented for the BeePlugin)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| TEMPLATEFILESTORAGEID | int |  | YES | (NULL) |
| HTMLFILESTORAGEID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| NAME | nvarchar | 250 | YES | ('') |
| EDITPAGEFILESTORAGEID | int |  | YES | (NULL) |
| ISSYNCED | bit |  | YES | ((0)) |
| GUID | nvarchar | 50 | YES | ('') |

## EmailTemplateLineage
**Physical table:** `OSUSR_by8_EmailTemplateLineage`  
**Description:** Auxillary table to keep track of template version history  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EMAILTEMPLATEID | bigint |  | YES | (NULL) |
| COPIEDFROMEMAILTEMPLATEID | bigint |  | YES | (NULL) |
| ISVERSION | bit |  | YES | ((0)) |
| SOURCEEMAILTEMPLATEID | bigint |  | YES | (NULL) |

## EmailTemplateUser
**Physical table:** `OSUSR_by8_EmailTemplateUser`  
**Description:** relation between users and automated email templates  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| EMAILTEMPLATEID | bigint |  | YES | (NULL) |
| ISSTARRED | bit |  | YES | ((0)) |

## GlobalEmailTemplate
**Physical table:** `OSUSR_by8_GlobalEmailTemplate1`  
**Description:** Stores wodify global email templates to federate to Email templates across environments  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALEMAILTEMPLATEID | bigint |  | YES | ((0)) |
| VERSION | int |  | YES | ((0)) |
| NAME | nvarchar | 250 | YES | ('') |
| TEMPLATEJSONS3KEY | nvarchar | 1024 | YES | ('') |
| TEMPLATEHTMLS3KEY | nvarchar | 1024 | YES | ('') |
| THUMBNAILS3KEY | nvarchar | 1024 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| ISWORKFLOWEMAIL | bit |  | YES | ((0)) |
| SUBJECT | nvarchar | 500 | YES | ('') |
| ATTACHMENTFILEID | nvarchar | 50 | YES | ('') |
| ISMEDIALIBRARYATTACHMENT | bit |  | YES | ((0)) |
| ISLATESTVERSION | bit |  | YES | ((0)) |
| HTMLFILESTORAGEID | int |  | YES | (NULL) |
| TEMPLATEFILESTORAGEID | int |  | YES | (NULL) |
| THUMBNAILFILESTORAGEID | int |  | YES | (NULL) |
| ISPROMOTEDTOTEST | bit |  | YES | ((0)) |
| ISPROMOTEDTOSTAGE | bit |  | YES | ((0)) |
| ISPROMOTEDTOPRODUCTION | bit |  | YES | ((0)) |
| PROMOTEDTOTESTON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PROMOTEDTOSTAGEON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PROMOTEDTOPRODUCTIONON | datetime |  | YES | ('1900-01-01 00:00:00') |
| GLOBALEMAILTEMPLATETYPEID | int |  | YES | (NULL) |

## GlobalEmailTemplateEmailTemplateCustomRow
**Physical table:** `OSUSR_by8_GlobalEmailTemplateEmailTemplateCustomRow`  
**Description:** Auxillary table to keep track of custom synced rows being used in global email templates  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EMAILTEMPLATECUSTOMROWID | bigint |  | YES | (NULL) |
| GLOBALEMAILTEMPLATEID | bigint |  | YES | (NULL) |

## GlobalEmailTemplatePublishResponse
**Physical table:** `OSUSR_by8_GlobalEmailTemplatePublishResponse`  
**Description:** Global template Publish response options, to record state when a user receives, accepts, or rejects a new version of a GlobalEmailTemplate  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## GlobalEmailTemplateType
**Physical table:** `OSUSR_by8_GlobalEmailTemplateType`  
**Description:** Available types for global email templates  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## GlobalEmailTemplateUser
**Physical table:** `OSUSR_by8_GlobalEmailTemplateUser`  
**Description:** Stores relationship between a user and a global template, in order to allow a user to denote a global template as a favorite  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| GLOBALTEMPLATEEXTERNALID | bigint |  | YES | ((0)) |
| USERID | int |  | YES | (NULL) |
| ISSTARRED | bit |  | YES | ((0)) |

## GlobalTemplateProcessType
**Physical table:** `OSUSR_by8_ProcessType`  
**Description:** Static entity for global template async process types  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
