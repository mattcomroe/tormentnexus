# WodifyManagement

## Tables

- [BusinessType](#businesstype)
- [CloudsearchTertiaryMenuItems](#cloudsearchtertiarymenuitems)

## BusinessType
**Physical table:** `OSUSR_l8g_BusinessType`  
**Description:** Contains all business types.  If a Customer has multiple locations, it is possible to have a different business type for each location, otherwise the customer will have one business type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| EXTERNALVALUE | nvarchar | 50 | YES | ('') |

## CloudsearchTertiaryMenuItems
**Physical table:** `OSUSR_l8g_CloudsearchTertiaryMenuItems`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CAPTION | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
