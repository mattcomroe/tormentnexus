# Sample_Energy_CS

## Tables

- [EnergyDailyConsumption](#energydailyconsumption)
- [EnergyHourlyConsumption](#energyhourlyconsumption)
- [EnergyInvoice](#energyinvoice)
- [EnergyMonthlyConsumption](#energymonthlyconsumption)
- [EnergyService](#energyservice)
- [InvoiceStatus](#invoicestatus)
- [RatePlan](#rateplan)

## EnergyDailyConsumption
**Physical table:** `OSUSR_gon_EnergyDailyConsumption`  
**Description:** Daily consumption for a contracted service  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ENERGYSERVICEID | bigint |  | YES | (NULL) |
| DAY | datetime |  | YES | ('1900-01-01 00:00:00') |
| CONSUMPTIONKWH | decimal |  | YES | ((0)) |
| VALUE | decimal |  | YES | ((0)) |
| ESTIMATEDCONSUMPTIONKWH | decimal |  | YES | ((0)) |
| ESTIMATEDVALUE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## EnergyHourlyConsumption
**Physical table:** `OSUSR_gon_EnergyHourlyConsumption`  
**Description:** Hourly consumption for a contracted service  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ENERGYSERVICEID | bigint |  | YES | (NULL) |
| HOUR | datetime |  | YES | ('1900-01-01 00:00:00') |
| DAY | datetime |  | YES | ('1900-01-01 00:00:00') |
| CONSUMPTIONKWH | decimal |  | YES | ((0)) |
| VALUE | decimal |  | YES | ((0)) |
| ESTIMATEDCONSUMPTIONKWH | decimal |  | YES | ((0)) |
| ESTIMATEDVALUE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## EnergyInvoice
**Physical table:** `OSUSR_gon_EnergyInvoice`  
**Description:** Invoice for a specific period in a service provision.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SERVICEID | bigint |  | YES | (NULL) |
| INVOICENUMBER | nvarchar | 50 | YES | ('') |
| INVOICESTATUSID | int |  | YES | (NULL) |
| PERIODSTARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| PERIODENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| DUEON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAIDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| AMOUNT | decimal |  | YES | ((0)) |
| RATEPLANID | int |  | YES | (NULL) |
| TARIFF | decimal |  | YES | ((0)) |
| TOTALKWH | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## EnergyMonthlyConsumption
**Physical table:** `OSUSR_gon_EnergyMonthlyConsumption`  
**Description:** Monthly consumption for a contracted service  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ENERGYSERVICEID | bigint |  | YES | (NULL) |
| MONTH | int |  | YES | ((0)) |
| YEAR | int |  | YES | ((0)) |
| CONSUMPTIONKWH | decimal |  | YES | ((0)) |
| VALUE | decimal |  | YES | ((0)) |
| ESTIMATEDCONSUMPTIONKWH | decimal |  | YES | ((0)) |
| ESTIMATEDVALUE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## EnergyService
**Physical table:** `OSUSR_gon_EnergyService`  
**Description:** Contracted service.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CONTRACTNUMBER | nvarchar | 50 | YES | ('') |
| SERVICEADDRESS | nvarchar | 250 | YES | ('') |
| SERVICEZIPCODE | nvarchar | 20 | YES | ('') |
| SERVICESTATE | nvarchar | 200 | YES | ('') |
| SERVICECOUNTRY | nvarchar | 200 | YES | ('') |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| RATEPLANID | int |  | YES | (NULL) |
| TARIFF | decimal |  | YES | ((0)) |
| UNITCHARGE | nvarchar | 100 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## InvoiceStatus
**Physical table:** `OSUSR_gon_InvoiceStatus`  
**Description:** Status of the invoice.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| BACKGROUNDCLASS | nvarchar | 50 | YES | ('') |
| TEXTCLASS | nvarchar | 50 | YES | ('') |

## RatePlan
**Physical table:** `OSUSR_gon_RatePlan`  
**Description:** Package name of the service.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
