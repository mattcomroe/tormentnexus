# Sample_Inspections_CS

## Tables

- [AnswerType](#answertype)
- [Establishment](#establishment)
- [Inspection](#inspection)
- [InspectionAnswer](#inspectionanswer)
- [InspectionReason](#inspectionreason)
- [InspectionStatus](#inspectionstatus)
- [Question](#question)
- [QuestionCategory](#questioncategory)

## AnswerType
**Physical table:** `OSUSR_D4O_ANSWERTYPE`  
**Description:** Type of the answer to the inspection questions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CODE | nvarchar | 50 | YES | ('') |
| COLORCLASS | nvarchar | 50 | YES | ('') |
| BACKGROUNDCOLOR | nvarchar | 50 | YES | ('') |

## Establishment
**Physical table:** `OSUSR_D4O_ESTABLISHMENT`  
**Description:** For bootstrapping purposes only. Matches the establishment with the corresponding sample location.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ESTABLISHMENTCODE | nvarchar | 50 | YES | ('') |
| LOCATIONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## Inspection
**Physical table:** `OSUSR_D4O_INSPECTION`  
**Description:** Represents an inspection associated with a location.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ESTABLISHMENTID | int |  | YES | (NULL) |
| INSPECTIONNUMBER | int |  | YES | ((0)) |
| REASONID | int |  | YES | (NULL) |
| INSPECTIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| INSPECTORID | bigint |  | YES | (NULL) |
| TIMEIN | datetime |  | YES | ('1900-01-01 00:00:00') |
| TIMEOUT | datetime |  | YES | ('1900-01-01 00:00:00') |
| INSPECTIONSTATUSID | int |  | YES | (NULL) |
| FOLLOWUPNOTES | nvarchar | 1500 | YES | ('') |
| FINALSCOREPOINTS | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## InspectionAnswer
**Physical table:** `OSUSR_D4O_INSPECTIONANSWER`  
**Description:** Represents the answer to a specific question in an inspection.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| INSPECTIONID | bigint |  | YES | (NULL) |
| QUESTIONID | bigint |  | YES | (NULL) |
| ANSWERTYPEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## InspectionReason
**Physical table:** `OSUSR_D4O_INSPECTIONREASON`  
**Description:** Reason for the inspection.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| SHOWADDITIONALFIELD | bit |  | YES | ((0)) |

## InspectionStatus
**Physical table:** `OSUSR_D4O_INSPECTIONSTATUS`  
**Description:** Status of the inspection.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| BACKGROUNDCLASS | nvarchar | 50 | YES | ('') |
| TEXTCLASS | nvarchar | 50 | YES | ('') |

## Question
**Physical table:** `OSUSR_D4O_QUESTION`  
**Description:** Represents a question in an inspection.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| QUESTIONCATEGORYID | bigint |  | YES | (NULL) |
| CODE | nvarchar | 50 | YES | ('') |
| QUESTIONTEXT | nvarchar | 1000 | YES | ('') |
| HASNA | bit |  | YES | ((0)) |
| HASNO | bit |  | YES | ((0)) |
| SCORE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## QuestionCategory
**Physical table:** `OSUSR_D4O_QUESTIONCATEGORY`  
**Description:** Represents a category of questions in an inspection.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 500 | YES | ('') |
| FORFIRSTFORM | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
