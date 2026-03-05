# Pricing_CS

## Tables

- [BillingCustomerCache](#billingcustomercache)
- [BillingGlobalCache](#billingglobalcache)
- [CustomerFeature](#customerfeature)
- [CustomerFeatureBillingLog](#customerfeaturebillinglog)
- [CustomerFeatureLog](#customerfeaturelog)
- [CustomerPackage](#customerpackage)
- [Feature](#feature)
- [FeatureLog](#featurelog)
- [LogStatus](#logstatus)
- [Package](#package)
- [PackageFeature](#packagefeature)

## BillingCustomerCache
**Physical table:** `OSUSR_b84_BillingTenantCache`  
**Description:** Stores last update on Customer billing (Package configuration).  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES |  |

## BillingGlobalCache
**Physical table:** `OSUSR_b84_BillingGlobalCache`  
**Description:** Stores last update on global billing (Package configuration).  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerFeature
**Physical table:** `OSUSR_b84_TenantFeature`  
**Description:** Associates a Customer with a feature.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FEATUREID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES |  |

## CustomerFeatureBillingLog
**Physical table:** `OSUSR_b84_CustomerFeatureBillingLog`  
**Description:** Log for timer when billing customer for certain feature individually  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| FEATUREID | bigint |  | YES | (NULL) |
| LOGSTATUSID | int |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 1500 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerFeatureLog
**Physical table:** `OSUSR_b84_TenantFeatureLog`  
**Description:** Log that holds information about a Customer associated to a FeatureLog that needs to be processed  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FEATURELOGID | bigint |  | YES | (NULL) |
| LOGSTATUSID | int |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 1500 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES |  |

## CustomerPackage
**Physical table:** `OSUSR_b84_TenantPackage`  
**Description:** Associates a Customer with a package.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PACKAGEID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES |  |

## Feature
**Physical table:** `OSUSR_b84_Feature`  
**Description:** Pricing feature.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LABEL | nvarchar | 150 | YES | ('') |
| FEATUREORDER | int |  | YES | ((0)) |

## FeatureLog
**Physical table:** `OSUSR_b84_FeatureLog`  
**Description:** Log that holds information about a feature that is being added or removed from a package, a Customer or multiple Customers  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FEATUREID | bigint |  | YES | (NULL) |
| PACKAGEID | bigint |  | YES | (NULL) |
| ISTOACTIVATE | bit |  | YES | ((0)) |
| ISTOREMOVEADHOC | bit |  | YES | ((0)) |
| TRIES | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 1500 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| AFFECTMULTIPLETENANTS | bit |  | YES | ((0)) |
| GROUPGUID | nvarchar | 50 | YES | ('') |
| LOGSTATUSID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES |  |

## LogStatus
**Physical table:** `OSUSR_b84_FeatureLogStatus`  
**Description:** Log status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## Package
**Physical table:** `OSUSR_b84_Package`  
**Description:** Pricing package.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LABEL | nvarchar | 150 | YES | ('') |
| ISBILLEDINWODIFY | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| ISLEGACYPACKAGE | bit |  | YES | ((0)) |

## PackageFeature
**Physical table:** `OSUSR_b84_PackageFeature`  
**Description:** Associates a feature with a package.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PACKAGEID | bigint |  | YES | (NULL) |
| FEATUREID | bigint |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
