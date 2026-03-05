# TabFilters_CS

## Tables

- [Domain](#domain)
- [FilterType](#filtertype)
- [Operator](#operator)
- [Page](#page)
- [PageFilter](#pagefilter)
- [PageFilterOperators](#pagefilteroperators)
- [PageTab](#pagetab)
- [PageTabFilter](#pagetabfilter)
- [PageTabUserOrder](#pagetabuserorder)
- [SubPage](#subpage)
- [Tab](#tab)

## Domain
**Physical table:** `OSUSR_zt8_Domain`  
**Description:** Each record represents an entity that contains a list of values.  The record does not actually identify that entity, but rather that entity must be known by the developer to be used in GetDomainValuesByPageFilterId.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| IS_ACTIVE | bit |  | YES | ((0)) |

## FilterType
**Physical table:** `OSUSR_zt8_FilterType`  
**Description:** There are 7 different types of filters:  Text: Will act as a search on a particular attribute of an entity. Will open a text box.  Integer: Same as Text, but searching for Integers only.  Boolean: Will filter on whether a particular attribute is true or not. Will show a check box.  DateTime: Will filter on a date range, that will be specified on a calendar input selector.   Datetime range: Will filter on a datetime range, that will be specified on a calendar input selector.  Domain: When there is a defined list of values that can be filtered on. Will show a dropdown.  Decimal: Same as Text, but searching for Decimals only.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Operator
**Physical table:** `OSUSR_zt8_Operator`  
**Description:** An operator picked from this list will be specified in each PageFilterOperators record. Each Operator record includes a small piece of SQL that will be used in the dynamic clause.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| SQL | nvarchar | 50 | YES | ('') |

## Page
**Physical table:** `OSUSR_zt8_Page`  
**Description:** The Page Label will be referenced (via API) from the End User Layer.  Must enter this correctly.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PAGENAME | nvarchar | 50 | YES | ('') |
| DATATYPE | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| OBJECTTYPEID | int |  | YES | (NULL) |

## PageFilter
**Physical table:** `OSUSR_zt8_PageFilter`  
**Description:** WARNING - these records are referenced by API and will not show up via F12 search. Don't be deleteing shit unless you know you can ;-)  Define the PageFilters that will appear on a specified page and will appear in the 'select a filter' dropdown.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| PAGEID | int |  | YES | (NULL) |
| FILTERTYPEID | int |  | YES | (NULL) |
| DOMAINID | int |  | YES | (NULL) |
| ENTITYATTRIBUTENAME | nvarchar | 255 | YES | ('') |
| ISCUSTOMSQLCLAUSE | bit |  | YES | ((0)) |

## PageFilterOperators
**Physical table:** `OSUSR_zt8_PageFilterOperators`  
**Description:** WARNING - these records are referenced by API and will not show up via F12 search. Don't be deleteing shit unless you know you can ;-)   Create records here for each PageFilter with type Domain, specifying both the PageFilter itself and the type of Operator used on it.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FILTERID | int |  | YES | (NULL) |
| OPERATORID | int |  | YES | (NULL) |

## PageTab
**Physical table:** `OSUSR_zt8_PageTab`  
**Description:** Contains all the customized Filter tabs for each user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAGEID | int |  | YES | (NULL) |
| NAME | nvarchar | 50 | YES | ('') |
| OWNERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLAUSEISALL | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| CANNOTBEDELETED | bit |  | YES | ((0)) |
| ISTABWITHNOFILTERS | bit |  | YES | ((0)) |
| BETAFEATUREID | int |  | YES | (NULL) |
| TABID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SUBPAGEID | bigint |  | YES | (NULL) |

## PageTabFilter
**Physical table:** `OSUSR_zt8_PageTabFilter`  
**Description:** Contains all the customized PageFilters for each tab created on PageTab Entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAGETABID | int |  | YES | (NULL) |
| FILTERID | int |  | YES | (NULL) |
| FILTERNAME | nvarchar | 150 | YES | ('') |
| FILTERVALUE | nvarchar | 100 | YES | ('') |
| OPERATORID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PageTabUserOrder
**Physical table:** `OSUSR_r0r_PageTabUserOrder`  
**Description:** Contains the customized order of page tabs for each user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PAGETABID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| PAGEID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |

## SubPage
**Physical table:** `OSUSR_r0r_SubPage`  
**Description:** Connects the PageTab entity to specific ObjectIds  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| PAGEID | int |  | YES | (NULL) |
| OBJECTID | bigint |  | YES | ((0)) |

## Tab
**Physical table:** `OSUSR_r0r_Tab`  
**Description:** Contains all tabs that cannot be deleted and are used to run a specific query, which will avoid having "expand inline" and "execution plan recreation"  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| PAGEID | int |  | YES | (NULL) |
| ISDEFAULT | bit |  | YES | ((0)) |
