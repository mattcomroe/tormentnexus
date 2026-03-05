# Segment_CS

## Tables

- [BootstrappedSegmentError](#bootstrappedsegmenterror)
- [Segment](#segment)
- [SegmentCloudSearchQuery](#segmentcloudsearchquery)
- [SegmentLogicOperator](#segmentlogicoperator)
- [SegmentPeople](#segmentpeople)
- [SegmentPeopleType](#segmentpeopletype)
- [SegmentRule](#segmentrule)
- [SegmentRule_Definition](#segmentrule-definition)
- [SegmentRule_Scope](#segmentrule-scope)
- [SegmentRule_Type](#segmentrule-type)
- [SegmentRuleTimeType](#segmentruletimetype)

## BootstrappedSegmentError
**Physical table:** `OSUSR_2wp_BootstrappedSegmentError`  
**Description:** Table to track customers who failed to create bootstrapped segment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| BOOTSTRAPACTIONNAME | nvarchar | 50 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Segment
**Physical table:** `OSUSR_2wp_Segment`  
**Description:** Segment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| DESCRIPTION | nvarchar | 250 | YES | ('') |
| ISLOCKED | bit |  | YES | ((0)) |
| PEOPLECOUNT | int |  | YES | ((0)) |
| ISFAVORITE | bit |  | YES | ((0)) |
| PEOPLETYPEID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISBOOTSTRAP | bit |  | YES | ((0)) |
| ISCUSTOM | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## SegmentCloudSearchQuery
**Physical table:** `OSUSR_2wp_SegmentCloudSearchQuery`  
**Description:** Segment CloudSearch Query  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| SEGMENTID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISLOCKED | bit |  | YES | ((0)) |
| QUERY | nvarchar | 2000 | YES | ('') |

## SegmentLogicOperator
**Physical table:** `OSUSR_2wp_SegmentLogicOperator`  
**Description:** Contains the logic operator to be used in the segment rule values table  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| CLOUDSEARCHLOGICOPERATORID | int |  | YES | (NULL) |
| USEONVALUECHOICE | bit |  | YES | ((0)) |
| USEONTERMMATCH | bit |  | YES | ((0)) |
| USEONMULTIPLECHOICE | bit |  | YES | ((0)) |
| USEONTIMEDCONDITION | bit |  | YES | ((0)) |
| USEONTIMEFRAME | bit |  | YES | ((0)) |
| USEONVALUECHOICEINTERVAL | bit |  | YES | ((0)) |
| USEONPEOPLERELATION | bit |  | YES | ((0)) |
| USEONMULTICHOICEWITHSUBCAT | bit |  | YES | ((0)) |

## SegmentPeople
**Physical table:** `OSUSR_2wp_SegmentPeople`  
**Description:** Segment People  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SEGMENTID | bigint |  | YES | (NULL) |
| ATHLETEID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| ISEXCLUDED | bit |  | YES | ((0)) |
| ISMANUALYINCLUDED | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## SegmentPeopleType
**Physical table:** `OSUSR_2wp_SegmentPeopleType`  
**Description:** SegmentPeople Type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 42 | YES | ('') |
| NAMESUMMARY | nvarchar | 42 | YES | ('') |
| SEGMENTRULESCOPE | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## SegmentRule
**Physical table:** `OSUSR_2wp_SegmentRule`  
**Description:** Segment Rule  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SEGMENTID | bigint |  | YES | (NULL) |
| SEGMENTRULEDEFINITIONID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| VALUE | nvarchar | -1 | YES | ('') |
| START | nvarchar | 50 | YES | ('') |
| END | nvarchar | 50 | YES | ('') |
| SEGMENTLOGICOPERATORID | int |  | YES | (NULL) |
| SEGMENTLOGICINTERVALID | int |  | YES | (NULL) |
| USECURRDATE | bit |  | YES | ((0)) |
| STARTDIFF | int |  | YES | ((0)) |
| ENDDIFF | int |  | YES | ((0)) |
| STARTTIMETYPEID | int |  | YES | (NULL) |
| ENDTIMETYPEID | int |  | YES | (NULL) |
| ISSPECIFICTIME | bit |  | YES | ((0)) |

## SegmentRule_Definition
**Physical table:** `OSUSR_2wp_SegmentRule_Definition`  
**Description:** Segment Rule Definition  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| RULETITLE | nvarchar | 50 | YES | ('') |
| RULEHELPTEXT | nvarchar | 500 | YES | ('') |
| MENULABEL | nvarchar | 50 | YES | ('') |
| TYPEID | int |  | YES | (NULL) |
| TEXTSTATEMENTBEFORE | nvarchar | 150 | YES | ('') |
| TEXTSTATEMENTBEFOREOTHER | nvarchar | 150 | YES | ('') |
| TEXTSTATEMENTAFTER | nvarchar | 150 | YES | ('') |
| TENANTBASEDUNITLABEL | bit |  | YES | ((0)) |
| UNITLABEL | nvarchar | 50 | YES | ('') |
| VERBACTION | nvarchar | 50 | YES | ('') |
| SCOPEID | int |  | YES | (NULL) |
| TABLENAME | nvarchar | 50 | YES | ('') |
| LABELNAME | nvarchar | 50 | YES | ('') |
| QUERYCONDITION | nvarchar | 500 | YES | ('') |
| ISMULTITENANT | bit |  | YES | ((0)) |
| ISATHLETEPICKLISTVALUE | bit |  | YES | ((0)) |
| ISLEADPICKLISTVALUE | bit |  | YES | ((0)) |
| USESPECIALLIST | bit |  | YES | ((0)) |
| ISBOOLEAN | bit |  | YES | ((0)) |
| ISCURRENCY | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| BOOLEANYESTEXT | nvarchar | 50 | YES | ('') |
| BOOLEANNOTEXT | nvarchar | 50 | YES | ('') |
| PEOPLELISTENDPOINT | nvarchar | 500 | YES | ('') |
| USELOGICOPERATORONPATTERN | bit |  | YES | ((0)) |
| ISATHLETESTATUSPICKLISTVALUE | bit |  | YES | ((0)) |
| ISLEADSTATUSPICKLISTVALUE | bit |  | YES | ((0)) |

## SegmentRule_Scope
**Physical table:** `OSUSR_2wp_SegmentRule_Scope`  
**Description:** Segment Rule Scope  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SCOPE | nvarchar | 34 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## SegmentRule_Type
**Physical table:** `OSUSR_2wp_SegmentRule_Type`  
**Description:** SegmentRule Type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 25 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## SegmentRuleTimeType
**Physical table:** `OSUSR_2wp_SegmentRuleTimeType`  
**Description:** Entity that has the values allowed when in custom time type definition  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
