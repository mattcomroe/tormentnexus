# Sample_Geo_CS

## Tables

- [Country](#country)
- [CountryState](#countrystate)

## Country
**Physical table:** `OSUSR_hpt_Country`  
**Description:** Entity that holds the records of type Country.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CODE | nvarchar | 50 | YES | ('') |
| NAME | nvarchar | 100 | YES | ('') |
| DIALCODE | nvarchar | 20 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CountryState
**Physical table:** `OSUSR_hpt_CountryState`  
**Description:** Entity that holds the records of type CountryState.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| COUNTRYID | int |  | YES | (NULL) |
| CODE | nvarchar | 50 | YES | ('') |
| NAME | nvarchar | 100 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
