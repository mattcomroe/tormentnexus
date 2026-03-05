# BetaCustomer_CS

## Tables

- [BetaCustomer](#betacustomer)
- [Feature](#feature)
- [FeatureSettings](#featuresettings)

## BetaCustomer
**Physical table:** `OSUSR_XLR_BETATENANT`  
**Description:** The beta Customer records that tie a given Customer to a beta Customer type.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| FEATUREID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ISFEATUREON | bit |  | YES | ((0)) |

## Feature
**Physical table:** `OSUSR_XLR_FEATURE`  
**Description:** It represents the features that are available only for Beta Customers. As an example, Social, White Labeling, etc  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## FeatureSettings
**Physical table:** `OSUSR_8RV_GAFEATURE`  
**Description:** Settings for each feature  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| FEATUREID | int |  | NO |  |
| ISGENERALAVAILABILITYON | bit |  | YES | ((0)) |
| ISDEMOINTERNALACCOUNTSON | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
