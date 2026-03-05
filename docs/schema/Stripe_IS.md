# Stripe_IS

## Tables

- [StripeCapabilityStatus](#stripecapabilitystatus)
- [StripeErrorCode](#stripeerrorcode)
- [StripeErrorType](#stripeerrortype)
- [StripePaymentMethodType](#stripepaymentmethodtype)

## StripeCapabilityStatus
**Physical table:** `OSUSR_QYL_STRIPECAPABILITYSTATUS`  
**Description:** List of possible statuses of a customer's payment method type capability  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## StripeErrorCode
**Physical table:** `OSUSR_QYL_STRIPEERRORCODE`  
**Description:** List of error codes that can be returned by Stripe's API. See https://docs.stripe.com/error-codes for more details  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 200 | YES | ('') |

## StripeErrorType
**Physical table:** `OSUSR_QYL_STRIPEERRORTYPE`  
**Description:** List of error types that can be returned by Stripe's API. See https://docs.stripe.com/api/errors#errors-type for more details  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 200 | YES | ('') |

## StripePaymentMethodType
**Physical table:** `OSUSR_QYL_STRIPEPAYMENTMETHOD`  
**Description:** List of supported Stripe payment method types. See https://docs.stripe.com/api/payment_methods/object#payment_method_object-type for more details  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
