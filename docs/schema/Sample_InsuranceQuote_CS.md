# Sample_InsuranceQuote_CS

## Tables

- [Coverage](#coverage)
- [Driver](#driver)
- [InsuranceType](#insurancetype)
- [Plan](#plan)
- [PlanCoverage](#plancoverage)
- [Quote](#quote)
- [QuoteCar](#quotecar)
- [Vehicle](#vehicle)

## Coverage
**Physical table:** `OSUSR_AG5_COVERAGE`  
**Description:** Entity that holds the records of diferent coverages of the insurance plans.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| INSURANCETYPEID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## Driver
**Physical table:** `OSUSR_AG5_DRIVER`  
**Description:** Entity that holds the records of type Driver.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FULLNAME | nvarchar | 250 | YES | ('') |
| BIRTHDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| DRIVERLICENSEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ZIPCODE | nvarchar | 15 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| PHONENUMBER | nvarchar | 20 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## InsuranceType
**Physical table:** `OSUSR_AG5_INSURANCETYPE`  
**Description:** Static entity that holds the differente types of insurances.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TYPE | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## Plan
**Physical table:** `OSUSR_AG5_PLAN`  
**Description:** Entity that holds the records of insurance plans.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| MONTHLYPAYMENT | decimal |  | YES | ((0)) |
| ISSIMULATIONSHOW | bit |  | YES | ((0)) |
| ISSIMULATIONSUGGESTED | bit |  | YES | ((0)) |
| INSURANCETYPEID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## PlanCoverage
**Physical table:** `OSUSR_AG5_PLANCOVERAGE`  
**Description:** Entity that holds the records that relate the insurance plans and its coverages.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PLANID | int |  | YES | (NULL) |
| COVERAGEID | int |  | YES | (NULL) |

## Quote
**Physical table:** `OSUSR_AG5_QUOTE`  
**Description:** Entity that holds the records of type Quote.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| INSURANCETYPEID | int |  | YES | (NULL) |
| POLICYSTARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## QuoteCar
**Physical table:** `OSUSR_AG5_QUOTECAR`  
**Description:** Entity that holds the records of type QuoteCar.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| VEHICLEID | bigint |  | YES | (NULL) |
| DRIVERID | bigint |  | YES | (NULL) |
| PLANID | int |  | YES | (NULL) |

## Vehicle
**Physical table:** `OSUSR_AG5_VEHICLE`  
**Description:** Entity that holds the records of type Vehicle.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| VEHICLEBRANDID | bigint |  | YES | (NULL) |
| VEHICLEMODELID | bigint |  | YES | (NULL) |
| VEHICLEVERSIONID | bigint |  | YES | (NULL) |
| LICENSEPLATE | nvarchar | 15 | YES | ('') |
| LICENSEPLATEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
