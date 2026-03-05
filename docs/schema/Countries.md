# Countries

## Tables

- [Country](#country)
- [CountryCallingCode](#countrycallingcode)
- [CountryConceptLocalization](#countryconceptlocalization)
- [CurrencyConfiguration](#currencyconfiguration)
- [LocalizableConcept](#localizableconcept)
- [State](#state)

## Country
**Physical table:** `OSUSR_I7M_COUNTRY1`  
**Description:** List of ISO known countries  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| CODE | nvarchar | 50 | YES | ('') |
| HASSTATES | bit |  | YES | ((0)) |
| CURRENCYCODE | nvarchar | 50 | YES | ('') |
| POSTALCODEMANDATORY | bit |  | YES | ((0)) |
| ISUNITEDSTATESTERRITORY | bit |  | YES | ((0)) |
| IBANCOUNTRYCODE | nvarchar | 4 | YES | ('') |
| CALLINGCODE | nvarchar | 50 | YES | ('') |

## CountryCallingCode
**Physical table:** `OSUSR_I7M_COUNTRYCALLINGCODE`  
**Description:** List of ISO known countries  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| COUNTRYID | int |  | YES | (NULL) |
| COUNTRYCALLINGCODE | int |  | YES | ((0)) |

## CountryConceptLocalization
**Physical table:** `OSUSR_I7M_COUNTRYCONCEPTLOCALIZATION1`  
**Description:** the joining table that maps Localizable Concepts to their names in different country or areas  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COUNTRYID | int |  | YES | (NULL) |
| LOCALIZABLECONCEPTID | int |  | YES | (NULL) |
| TERM | nvarchar | 200 | YES | ('') |

## CurrencyConfiguration
**Physical table:** `OSUSR_I7M_CURRENCYCONFIGURATION`  
**Description:** Contains a list of currency configurations  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CURRENCYCODE | nvarchar | 50 | NO |  |
| CURRENCYNAME | nvarchar | 50 | YES | ('') |
| COUNTRYNAME | nvarchar | 50 | YES | ('') |
| CURRENCYSYMBOL | nvarchar | 50 | YES | ('') |
| SIGNIFICANTDIGITS | int |  | YES | ((0)) |
| DECIMALSEPARATOR | nvarchar | 50 | YES | ('') |
| GROUPSEPARATOR | nvarchar | 50 | YES | ('') |

## LocalizableConcept
**Physical table:** `OSUSR_I7M_LOCALIZABLECONCEPT1`  
**Description:** Concepts that have different names or terms based on different country of area. ex.Tax ID, Personal ID; Personal ID in the US would be SSN and Portugal CC number.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## State
**Physical table:** `OSUSR_I7M_STATE1`  
**Description:** States by country  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| CODE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
