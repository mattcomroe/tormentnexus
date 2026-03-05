# W_OnlineSalesPort_CS

## Tables

- [CoachPageClientAppSetting](#coachpageclientappsetting)
- [CoachPageOnlineSalesSetting](#coachpageonlinesalessetting)
- [CustomerSettingCoachPage](#customersettingcoachpage)
- [CustomerSettingOnlineSales](#customersettingonlinesales)
- [LocationSettingCoachPage](#locationsettingcoachpage)

## CoachPageClientAppSetting
**Physical table:** `OSUSR_5NJ_COACHPAGECLIENTAPPSETTING2`  
**Description:** Coach settings for Coach Page in Client App  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| COACHID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ISVISIBLE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CoachPageOnlineSalesSetting
**Physical table:** `OSUSR_5NJ_COACHPAGEONLINESALESSETTING`  
**Description:** Coach settings for Coach Page in Online Sales  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| LOCATIONID | bigint |  | YES | ((0)) |
| COACHID | bigint |  | YES | ((0)) |
| ISVISIBLE | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerSettingCoachPage
**Physical table:** `OSUSR_5NJ_CUSTOMERSETTINGCOACHPAGE1`  
**Description:** Customer settings for Coach Page  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CUSTOMERID | bigint |  | NO |  |
| SHOWINONLINESALES | bit |  | YES | ((0)) |
| SHOWINCLIENTAPP | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerSettingOnlineSales
**Physical table:** `OSUSR_5NJ_TENANTSETTINGONLINESALES`  
**Description:** Online Sales settings for the Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANTID | int |  | YES | ((0)) |
| DISPLAYTAXBEFORECHECKOUT | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| CUSTOMERID | bigint |  | NO | ((0)) |
| HIDESETUPFEEFROMTOTALPRICE | bit |  | YES | ((0)) |
| GUARDIANCANPURCHASEFORDEP | bit |  | YES | ((1)) |
| FORCEWAIVERSIGNING | bit |  | YES | ((1)) |

## LocationSettingCoachPage
**Physical table:** `OSUSR_5NJ_LOCATIONSETTINGCOACHPAGE1`  
**Description:** Location settings for Coach Page  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LOCATIONID | bigint |  | NO |  |
| SHOWINONLINESALES | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
