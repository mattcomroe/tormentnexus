# Sample_Customer_CS

## Tables

- [Company](#company)
- [CompanyContact](#companycontact)
- [CompanyContactThumbnail](#companycontactthumbnail)
- [CompanyPosition](#companyposition)
- [Customer](#customer)
- [CustomerIdentificationDocument](#customeridentificationdocument)
- [CustomerIdentificationSelfie](#customeridentificationselfie)
- [CustomerThumbnail](#customerthumbnail)
- [Gender](#gender)
- [Title](#title)

## Company
**Physical table:** `OSUSR_AZO_COMPANY`  
**Description:** Entity that holds the records of Companies.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CODE | nvarchar | 50 | YES | ('') |
| COMPANYNAME | nvarchar | 100 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| LOCATIONID | int |  | YES | (NULL) |
| JOINDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISINTERNALORG | bit |  | YES | ((0)) |
| NUMBEROFEMPLOYEES | int |  | YES | ((0)) |

## CompanyContact
**Physical table:** `OSUSR_AZO_COMPANYCONTACT`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| USERNAME | nvarchar | 50 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| PHONENUMBER | nvarchar | 20 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| COMPANY | bigint |  | YES | (NULL) |
| ISADMIN | bit |  | YES | ((0)) |
| DEPARTMENT | bigint |  | YES | (NULL) |
| JOBPOSITION | nvarchar | 50 | YES | ('') |
| ISINTERNALUSER | bit |  | YES | ((0)) |
| ISSUPPORTMANAGER | bit |  | YES | ((0)) |
| HIRINGDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CompanyContactThumbnail
**Physical table:** `OSUSR_AZO_COMPANYCONTACTTHUMBNAIL`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FILENAME | nvarchar | 50 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CompanyPosition
**Physical table:** `OSUSR_AZO_COMPANYPOSITION`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| POSITION | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |

## Customer
**Physical table:** `OSUSR_AZO_CUSTOMER`  
**Description:** Entity that holds the records of Customers.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TITLEID | int |  | YES | (NULL) |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| BIRTHDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAIL | nvarchar | 250 | YES | ('') |
| PHONE | nvarchar | 20 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| GENDERID | int |  | YES | (NULL) |
| ADDRESS | nvarchar | 250 | YES | ('') |
| CORRESPONDENCEADDRESS | nvarchar | 250 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| COUNTRYSTATEID | int |  | YES | (NULL) |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| LAT | decimal |  | YES | ((0)) |
| LNG | decimal |  | YES | ((0)) |
| MOBILE | nvarchar | 20 | YES | ('') |
| LANGUAGE | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## CustomerIdentificationDocument
**Physical table:** `OSUSR_AZO_CUSTOMERIDENTIFICATIONDOCUMENT`  
**Description:** Entity that holds the records of customers identification document.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| FILENAME | nvarchar | 50 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| ISBACKSIDE | bit |  | YES | ((0)) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerIdentificationSelfie
**Physical table:** `OSUSR_AZO_CUSTOMERIDENTIFICATIONSELFIE`  
**Description:** Entity that holds the records of customers identification selfie.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FILENAME | nvarchar | 50 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerThumbnail
**Physical table:** `OSUSR_AZO_CUSTOMERTHUMBNAIL`  
**Description:** Entity that holds the records of Customers thumbnails.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FILENAME | nvarchar | 50 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Gender
**Physical table:** `OSUSR_AZO_GENDER`  
**Description:** Entity that holds the options for a customer's gender  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Title
**Physical table:** `OSUSR_AZO_TITLE`  
**Description:** Entity that holds the options for a customer's title.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
