# CorePayments_CS

## Tables

- [StripeConfigurationCustomer](#stripeconfigurationcustomer)
- [StripeConfigurationLocation](#stripeconfigurationlocation)
- [StripeDefaultCountryRate](#stripedefaultcountryrate)

## StripeConfigurationCustomer
**Physical table:** `OSUSR_RT6_STRIPECONFIGURATIONTENANT`  
**Description:** Represents a Wodify Payments configuration for a Customer.  These are the configurable settings on the Stripe configuration screen and drive the behavior of how Stripe is used in the given Customer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | ((0)) |

## StripeConfigurationLocation
**Physical table:** `OSUSR_RT6_STRIPECONFIGURATIONLOCATION`  
**Description:** Relates a Location to a Stripe Configuration. When a Location uses a given Stripe Configuration, a record will exist in this table. Only one record may exist per Location.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## StripeDefaultCountryRate
**Physical table:** `OSUSR_RT6_STRIPEDEFAULTCOUNTRYRATE`  
**Description:** Represents the default rates that a business that uses Wodify Payments will pay, when using Wodify Core.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COUNTRYID | int |  | YES | (NULL) |
| PACKAGEID | bigint |  | YES | (NULL) |
| CC_PERCENTAGEPERTRANSACTION | decimal |  | YES | ((0)) |
| CC_AMOUNTPERTRANSACTION | decimal |  | YES | ((0)) |
| BA_PERCENTAGEPERTRANSACTION | decimal |  | YES | ((0)) |
| BA_AMOUNTPERTRANSACTION | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CC_FAILEDPAYMENTFEE | decimal |  | YES | ((0)) |
| BA_FAILEDPAYMENTFEE | decimal |  | YES | ((0)) |
