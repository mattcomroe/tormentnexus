# CustomDictionary_CS

## Tables

- [CustomerCustomDictionary](#customercustomdictionary)
- [StaticTerm](#staticterm)
- [StaticTermCategory](#statictermcategory)
- [StaticTermV2](#statictermv2)
- [StaticTermV2Attribute](#statictermv2attribute)

## CustomerCustomDictionary
**Physical table:** `OSUSR_ef1_CustomerCustomDictionary`  
**Description:** Entity that holds Customer's Custom Dictionary settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| STATICTERMID | int |  | YES | (NULL) |
| LOCALE | nvarchar | 50 | YES | ('') |
| CUSTOMIZEDTERM | nvarchar | 60 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## StaticTerm
**Physical table:** `OSUSR_ef1_StaticTerm`  
**Description:** Entity that holds the Terms that are Customizable per Users and per Language (Locale)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CODE | nvarchar | 50 | YES | ('') |
| DEFAULTTERM | nvarchar | 50 | YES | ('') |
| CHARLIMIT | int |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## StaticTermCategory
**Physical table:** `OSUSR_ef1_StaticTermCategory`  
**Description:** Entity that holds the Categories for static terms that are Customizable per Users and per Language (Locale)  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## StaticTermV2
**Physical table:** `OSUSR_ef1_StaticTermV2`  
**Description:** Mobile version of Static Term that holds the Terms that are Customizable per Users and per Language (Locale)  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## StaticTermV2Attribute
**Physical table:** `OSUSR_ef1_StaticTermV2Attribute`  
**Description:** Static Entity that relates to the attribute available in terms  

_Table not present in the dev environment — schema unavailable. May exist in production only._
