# FinancialHistory_CS

## Tables

- [CustomerPaymentProcessorConfigurationHistory](#customerpaymentprocessorconfigurationhistory)
- [LocationPaymentProcessorConfigurationHistory](#locationpaymentprocessorconfigurationhistory)
- [PaymentMethodStatusHistory](#paymentmethodstatushistory)

## CustomerPaymentProcessorConfigurationHistory
**Physical table:** `OSUSR_a3y_TenantPaymentProcessorConfigurationHistory`  
**Description:** Represents payment processor configuration histories. This is the customer-level history record for when a customer's payment processor changed from one to another.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FROMPAYMENTPROCESSORID | int |  | YES | (NULL) |
| TOPAYMENTPROCESSORID | int |  | YES | (NULL) |
| CHANGEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CHANGEDBY | int |  | YES | (NULL) |
| ISSELECTED | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## LocationPaymentProcessorConfigurationHistory
**Physical table:** `OSUSR_a3y_LocationPaymentProcessorConfigurationHistory`  
**Description:** Represents a change of a Location's payment processor configuration. This is so we can go back and forth between the configuration if we should need to.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| TENANTPAYMENTPROCESSORCONFIG | bigint |  | YES | (NULL) |
| FROMPAYMENTPROCESSORCONFIGUR | int |  | YES | (NULL) |
| FROMSTRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| TOPAYMENTPROCESSORCONFIGURAT | int |  | YES | (NULL) |
| TOSTRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PaymentMethodStatusHistory
**Physical table:** `OSUSR_a3y_PaymentMethodStatusHistory`  
**Description:** Represents a status change made to a payment method due to a payment processor change. This relates a payment method to the payment processor configuration history record so it can be changed back if we should need to.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| PAYMENTMETHODID | int |  | YES | (NULL) |
| TENANTPAYMENTPROCESSORCONFIG | bigint |  | YES | (NULL) |
| ISDEFAULT | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
