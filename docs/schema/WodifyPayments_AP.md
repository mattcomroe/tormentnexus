# WodifyPayments_AP

## Tables

- [InvoiceHeaderForAdjustmentTemp](#invoiceheaderforadjustmenttemp)
- [StripeTransactionAdjustmentsTemp](#stripetransactionadjustmentstemp)
- [TransactionAdjustmentsTemp](#transactionadjustmentstemp)

## InvoiceHeaderForAdjustmentTemp
**Physical table:** `OSUSR_LFL_INVOICEHEADERFORADJUSTMENTTEMP`  
**Description:** Table to hold the InvoiceHeaderIds that we want to update  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| INVOICEHEADERID | int |  | YES | (NULL) |

## StripeTransactionAdjustmentsTemp
**Physical table:** `OSUSR_LFL_STRIPETRANSACTIONADJUSTMENTSTEMP`  
**Description:** Temp table to hold stripe transaction entity adjustment records  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPETRANSACTIONID | bigint |  | YES | (NULL) |
| FEEADJUSTMENTAMOUNT | decimal |  | YES | ((0)) |
| FEES_CURRENT | decimal |  | YES | ((0)) |
| FEES_UPDATED | decimal |  | YES | ((0)) |
| NETAMOUNT_CURRENT | decimal |  | YES | ((0)) |
| NETAMOUNT_UPDATED | decimal |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CURRENCYCODE | nvarchar | 3 | YES | ('') |

## TransactionAdjustmentsTemp
**Physical table:** `OSUSR_LFL_TRANSACTIONADJUSTMENTSTEMP`  
**Description:** Temp table to hold transaction entity adjustment records  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TRANSACTIONID | int |  | YES | (NULL) |
| FEEADJUSTMENTAMOUNT | decimal |  | YES | ((0)) |
| FEES_CURRENT | decimal |  | YES | ((0)) |
| FEES_UPDATED | decimal |  | YES | ((0)) |
| NETAMOUNT_CURRENT | decimal |  | YES | ((0)) |
| NETAMOUNT_UPDATED | decimal |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CURRENCYCODE | nvarchar | 3 | YES | ('') |
| CUSTOMERSTRIPEACCOUNTID | nvarchar | 50 | YES | ('') |
| WODIFYSTRIPEACCOUNTID | nvarchar | 50 | YES | ('') |
| TRANSFERCOMPLETEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| STRIPECONFIGURATIONID | bigint |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | -1 | YES | ('') |
