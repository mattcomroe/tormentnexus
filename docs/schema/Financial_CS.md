# Financial_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [AutoBillAttempts](#autobillattempts)
- [Discount](#discount)
- [DiscountType](#discounttype)
- [FinancialLocationSettings](#financiallocationsettings)
- [FinancialSettings](#financialsettings)
- [InvoiceBillingAttempt](#invoicebillingattempt)
- [InvoiceDetail](#invoicedetail)
- [InvoiceDetailDisplayType](#invoicedetaildisplaytype)
- [InvoiceDetailExtraDiscount](#invoicedetailextradiscount)
- [InvoiceDetailSource](#invoicedetailsource)
- [InvoiceHeader](#invoiceheader)
- [InvoiceHeaderStatus](#invoiceheaderstatus)
- [PartialRefundTransaction](#partialrefundtransaction)
- [PaymentMethod](#paymentmethod)
- [PaymentMethodTestMapping](#paymentmethodtestmapping)
- [PaymentProcessor](#paymentprocessor)
- [PaymentProcessorConfiguration](#paymentprocessorconfiguration)
- [PaymentProcessorConfigurationType](#paymentprocessorconfigurationtype)
- [PaymentProcessorConfigurationVersion](#paymentprocessorconfigurationversion)
- [Request](#request)
- [RequestImportPaymentMethodImportFile](#requestimportpaymentmethodimportfile)
- [RequestImportPaymentMethodImportLog](#requestimportpaymentmethodimportlog)
- [RequestType](#requesttype)
- [SharedPaymentMethod](#sharedpaymentmethod)
- [StoreCredit](#storecredit)
- [TaxRate](#taxrate)
- [TaxRateType](#taxratetype)
- [Transaction](#transaction)
- [TransactionStripePaymentMethod](#transactionstripepaymentmethod)
- [TransactionStripeTransaction](#transactionstripetransaction)
- [TransactionType](#transactiontype)

## AsyncProcess
**Physical table:** `OSUSR_c31_AsyncProcess`  
**Description:** Auxiliar entity that contains all asynchronous processes, which will run through the AP module in BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## AutoBillAttempts
**Physical table:** `OSUSR_c31_AutoBillAttempts`  
**Description:** Number and labels of the auto bill attempts.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| NUMBEROFATTEMPTS | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((1)) |

## Discount
**Physical table:** `OSUSR_72o_Discount`  
**Description:** Contains information of any discount of customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| DISCOUNTNAME | nvarchar | 100 | YES | ('') |
| DISCOUNTTYPEID | int |  | YES | (NULL) |
| PERCENTAGE | decimal |  | YES | ((0)) |
| FLATAMOUNT | decimal |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISARCHIVED | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## DiscountType
**Physical table:** `OSUSR_72o_DiscountType`  
**Description:** Static record of Discount types  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## FinancialLocationSettings
**Physical table:** `OSUSR_72o_FinancialLocationSettings`  
**Description:** Contains all the Financial settings of a Customer per Location.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LOCATIONID | int |  | NO |  |
| PAYMENTPROCESSORCONFIGURATIO | int |  | YES | (NULL) |
| PAYMENTMETHODID | int |  | YES | (NULL) |
| BILLINGCONTACT | int |  | YES | (NULL) |
| BILLINGCONTACTCC | int |  | YES | (NULL) |
| BILLINGCONTACTPHONE | nvarchar | 20 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYMENTPROCESSCONFIGID | int |  | YES | (NULL) |

## FinancialSettings
**Physical table:** `OSUSR_72o_FinancialSettings`  
**Description:** Contains all the settings of a Customer regarding Financial. One record per Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANTID | int |  | YES | ((0)) |
| PAYMENTPROCESSORID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISWODIFYBILLINGOVERDUE | bit |  | YES | ((0)) |
| SHOWBANNERWODBILLINGOVERDUE | bit |  | YES | ((0)) |
| INVOICEFOOTER | nvarchar | 1000 | YES | ('') |
| CREDITCARDNUMBEROFATTEMPTS | int |  | YES | (NULL) |
| BANKACCOUNTNUMBEROFATTEMPTS | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | NO |  |

## InvoiceBillingAttempt
**Physical table:** `OSUSR_c31_InvoiceBillingAttempt`  
**Description:** Stores the number of billing attempts for an invoice.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INVOICEHEADERID | int |  | YES | (NULL) |
| PAYMENTACCOUNTTYPEID | int |  | YES | (NULL) |
| NUMBEROFATTEMPTS | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## InvoiceDetail
**Physical table:** `OSUSR_72o_InvoiceDetail`  
**Description:** Contains details of invoice  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| INVOICEHEADERID | int |  | YES | (NULL) |
| MEMBERPLANID | int |  | YES | (NULL) |
| PRODUCTID | int |  | YES | ((0)) |
| PRODUCTNAME | nvarchar | 500 | YES | ('') |
| PRODUCTTYPEID | bigint |  | YES | ((0)) |
| REVENUECATEGORYPICKLISTVALUE | int |  | YES | (NULL) |
| LISTPRICE | decimal |  | YES | ((0)) |
| SALESPRICE | decimal |  | YES | ((0)) |
| QUANTITY | int |  | YES | ((0)) |
| INVENTORYRETURNS | int |  | YES | ((0)) |
| PRICEADJUSTMENT | decimal |  | YES | ((0)) |
| NETINVENTORYISSUED | int |  | YES | ((0)) |
| EXPECTEDREVENUE | decimal |  | YES | ((0)) |
| GROSSLINEDISCOUNT | decimal |  | YES | ((0)) |
| NETLINEDISCOUNT | decimal |  | YES | ((0)) |
| DISCOUNTAMOUNT | decimal |  | YES | ((0)) |
| DISCOUNTPERCENTAGE | decimal |  | YES | ((0)) |
| GROSSHEADERDISCOUNT | decimal |  | YES | ((0)) |
| NETHEADERDISCOUNT | decimal |  | YES | ((0)) |
| HEADERDISCOUNTAMOUNT | decimal |  | YES | ((0)) |
| HEADERDISCOUNTPERCENTAGE | decimal |  | YES | ((0)) |
| GROSSTOTALDISCOUNT | decimal |  | YES | ((0)) |
| NETTOTALDISCOUNT | decimal |  | YES | ((0)) |
| GROSSREVENUEADJUSTMENT | decimal |  | YES | ((0)) |
| NETREVENUEADJUSTMENT | decimal |  | YES | ((0)) |
| REFUNDEDREVENUE | decimal |  | YES | ((0)) |
| GROSSREVENUE | decimal |  | YES | ((0)) |
| POSTHEADERGROSSREVENUE | decimal |  | YES | ((0)) |
| NETREVENUE | decimal |  | YES | ((0)) |
| POSTHEADERNETREVENUE | decimal |  | YES | ((0)) |
| TAXRATEID | int |  | YES | (NULL) |
| TAXRATE | decimal |  | YES | ((0)) |
| GROSSTAX | decimal |  | YES | ((0)) |
| REFUNDEDTAX | decimal |  | YES | ((0)) |
| FINALREFUNDEDAMOUNT | decimal |  | YES | ((0)) |
| FINALTAX | decimal |  | YES | ((0)) |
| FINALCHARGE | decimal |  | YES | ((0)) |
| REFUNDABLEFINALCHARGE | decimal |  | YES | ((0)) |
| HISTORY | nvarchar | -1 | YES | ('') |
| ISFULFILLED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CONVERTEDFROMINVOICELINEID | int |  | YES | (NULL) |
| PRODUCTVARIANTID | bigint |  | YES | ((0)) |
| ONLINEMEMBERSHIPID | bigint |  | YES | ((0)) |
| OPTION1 | nvarchar | 500 | YES | ('') |
| OPTION2 | nvarchar | 500 | YES | ('') |
| OPTION3 | nvarchar | 500 | YES | ('') |
| LOCATIONID | int |  | YES | (NULL) |
| CURRENCYSIGNIFICANTDIGITS | int |  | YES | ((0)) |
| ISSETUPFEE | bit |  | YES | ((0)) |
| INVOICEDETAILDISPLAYTYPEID | int |  | YES | (NULL) |
| COSTPERUNIT | decimal |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| FEE | decimal |  | YES | ((0)) |
| REFUNDEDFEE | decimal |  | YES | ((0)) |
| FEETAX | decimal |  | YES | ((0)) |
| ISADDEDTOUPCOMINGINVOICE | bit |  | YES | ((0)) |
| INVOICEDETAILSOURCEID | int |  | YES | (NULL) |

## InvoiceDetailDisplayType
**Physical table:** `OSUSR_72o_InvoiceDetailDisplayType`  
**Description:** Static records of InvoiceDetailDisplay type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## InvoiceDetailExtraDiscount
**Physical table:** `OSUSR_72o_InvoiceDetailExtraDiscount`  
**Description:** Additional discounts applied to an invoice detail. Usually created by applying promo codes to an invoice.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| INVOICEDETAILID | int |  | YES | (NULL) |
| DISCOUNTTYPEID | int |  | YES | (NULL) |
| DISCOUNTAMOUNT | decimal |  | YES | ((0)) |
| DISCOUNTID | int |  | YES | (NULL) |
| DISCOUNTLABEL | nvarchar | 100 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## InvoiceDetailSource
**Physical table:** `OSUSR_c31_InvoiceDetailSource`  
**Description:** Possible retail channels an invoice detail with an associated productid could be added from  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## InvoiceHeader
**Physical table:** `OSUSR_72o_InvoiceHeader`  
**Description:** Contains information of invoice header  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| INVOICEID | nvarchar | 50 | YES | ('') |
| ISAUTOBILL | bit |  | YES | ((0)) |
| USERID | int |  | YES | (NULL) |
| PAYMENTDUE | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAIDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| LOCATIONID | int |  | YES | (NULL) |
| USERCLASSLOGINID | bigint |  | YES | ((0)) |
| CLASSRESERVATIONID | bigint |  | YES | ((0)) |
| ISFORTENANT | bit |  | YES | ((0)) |
| DISCOUNTAMOUNT | decimal |  | YES | ((0)) |
| DISCOUNTPERCENTAGE | decimal |  | YES | ((0)) |
| INVOICEHEADERSTATUSID | int |  | YES | (NULL) |
| EXPECTEDREVENUE | decimal |  | YES | ((0)) |
| GROSSLINEDISCOUNTS | decimal |  | YES | ((0)) |
| NETLINEDISCOUNTS | decimal |  | YES | ((0)) |
| GROSSHEADERDISCOUNTS | decimal |  | YES | ((0)) |
| NETHEADERDISCOUNTS | decimal |  | YES | ((0)) |
| GROSSTOTALDISCOUNTS | decimal |  | YES | ((0)) |
| NETTOTALDISCOUNTS | decimal |  | YES | ((0)) |
| GROSSREVENUEADJUSTMENT | decimal |  | YES | ((0)) |
| NETREVENUEADJUSTMENT | decimal |  | YES | ((0)) |
| REFUNDEDREVENUE | decimal |  | YES | ((0)) |
| GROSSREVENUE | decimal |  | YES | ((0)) |
| POSTHEADERGROSSREVENUE | decimal |  | YES | ((0)) |
| NETREVENUE | decimal |  | YES | ((0)) |
| POSTHEADERNETREVENUE | decimal |  | YES | ((0)) |
| GROSSTAX | decimal |  | YES | ((0)) |
| REFUNDEDTAX | decimal |  | YES | ((0)) |
| FINALREFUNDEDAMOUNT | decimal |  | YES | ((0)) |
| FINALTAX | decimal |  | YES | ((0)) |
| FINALCHARGE | decimal |  | YES | ((0)) |
| REFUNDABLEFINALCHARGE | decimal |  | YES | ((0)) |
| PAIDAMOUNT | decimal |  | YES | ((0)) |
| UNPAIDAMOUNT | decimal |  | YES | ((0)) |
| NOTES | nvarchar | 2000 | YES | ('') |
| HISTORY | nvarchar | -1 | YES | ('') |
| INVOICEFOOTER | nvarchar | 1000 | YES | ('') |
| WODIFYBILLINGINTERNALNOTES | nvarchar | 2000 | YES | ('') |
| ATHLETENAME | nvarchar | 250 | YES | ('') |
| RECEIPTEMAILADDRESS | nvarchar | 250 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CONVERTEDFROMINVOICEID | int |  | YES | (NULL) |
| PAIDONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| LEADID | int |  | YES | (NULL) |
| REFERENCENUMBER | nvarchar | 50 | YES | ('') |
| CREATEDONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ORDERNUMBER | nvarchar | 50 | YES | ('') |
| OPTIMALFINALCHARGE | decimal |  | YES | ((0)) |
| PAYMENTMETHODID | int |  | YES | (NULL) |
| TAXIDENTIFICATIONNUMBER | nvarchar | 50 | YES | ('') |
| LASTSTATUSCHANGEBY | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| TOTALFEES | decimal |  | YES | ((0)) |
| ABSORBFEES | bit |  | YES | ((0)) |
| UNAPPLIEDFEES | decimal |  | YES | ((0)) |
| REFUNDEDTOTALFEES | decimal |  | YES | ((0)) |
| SOLDBY | int |  | YES | (NULL) |
| DROPINID | bigint |  | YES | (NULL) |

## InvoiceHeaderStatus
**Physical table:** `OSUSR_72o_InvoiceHeaderStatus`  
**Description:** Static records of Invoice Header status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PartialRefundTransaction
**Physical table:** `OSUSR_72o_PartialRefundTransaction`  
**Description:** Registers which invoice item was refunded by a partial refund transaction.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| TRANSACTIONID | int |  | YES | (NULL) |
| INVOICEDETAILID | int |  | YES | (NULL) |
| REFUNDEDITEMQUANTITY | int |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PaymentMethod
**Physical table:** `OSUSR_72o_PaymentMethod`  
**Description:** Contains information of payment method  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | ((0)) |
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| PAYMENTACCOUNTSOURCEID | int |  | YES | (NULL) |
| ISFORTENANT | bit |  | YES | ((0)) |
| REFERENCENUMBER | nvarchar | 75 | YES | ('') |
| ACCOUNTNUMBERLASTFOUR | nvarchar | 4 | YES | ('') |
| ISDEFAULT | bit |  | YES | ((0)) |
| EXPIRATIONMONTH | int |  | YES | ((0)) |
| EXPIRATIONYEAR | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISANONYMOUSPAYMENTMETHOD | bit |  | YES | ((0)) |
| BILLINGPOSTALCODE | nvarchar | 10 | YES | ('') |
| BILLINGFIRSTNAME | nvarchar | 60 | YES | ('') |
| BILLINGLASTNAME | nvarchar | 60 | YES | ('') |
| BILLINGSTREET1 | nvarchar | 50 | YES | ('') |
| BILLINGSTREET2 | nvarchar | 50 | YES | ('') |
| BILLINGCITY | nvarchar | 40 | YES | ('') |
| BILLINGREGION | nvarchar | 40 | YES | ('') |
| BILLINGSTATEID | int |  | YES | (NULL) |
| BILLINGCOUNTRYID | int |  | YES | (NULL) |
| BILLINGPHONENUMBER | nvarchar | 20 | YES | ('') |
| ACHBANKNAME | nvarchar | 40 | YES | ('') |
| ACHROUTINGNUMBER | nvarchar | 11 | YES | ('') |
| ACHENCRYPTEDACCOUNTNUMBER | nvarchar | 2000 | YES | ('') |
| PAYMENTPROCESSORCONFIGURATIO | int |  | YES | (NULL) |
| BILLINGFULLNAME | nvarchar | 120 | YES | ('') |
| HASMANDATEREQUESTBEENSENT | bit |  | YES | ((0)) |
| EFFECTIVEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ACHBANKSTREET1 | nvarchar | 50 | YES | ('') |
| ACHBANKSTREET2 | nvarchar | 50 | YES | ('') |
| ACHBANKCITY | nvarchar | 40 | YES | ('') |
| ACHBANKREGION | nvarchar | 40 | YES | ('') |
| ACHBANKPOSTALCODE | nvarchar | 10 | YES | ('') |
| ACHBANKCOUNTRYID2 | int |  | YES | (NULL) |
| ISHARDDECLINE | bit |  | YES | ((0)) |
| OPTIMALSHOULDUSESTORECREDIT | bit |  | YES | ((0)) |
| PAYMENTCONTACT | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PaymentMethodTestMapping
**Physical table:** `OSUSR_72o_PaymentMethodTestMapping`  
**Description:** Entity used for non-production environments to do the mapping between credit cards from different payment processors.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SOURCE_PAYMENTPROCESSORID | int |  | YES | (NULL) |
| TARGET_PAYMENTPROCESSORID | int |  | YES | (NULL) |
| SOURCE_PAYMENTMETHODNUMBER | nvarchar | 50 | YES | ('') |
| TARGET_PAYMENTMETHODNUMBER | nvarchar | 50 | YES | ('') |

## PaymentProcessor
**Physical table:** `OSUSR_72o_PaymentProcessor`  
**Description:** The available payment processors.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |

## PaymentProcessorConfiguration
**Physical table:** `OSUSR_c31_PaymentProcessorConfiguration`  
**Description:** Payment processor configuration. Used for Ezidebit  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| PAYMENTPROCESSORID | int |  | YES | (NULL) |
| NAME | nvarchar | 50 | YES | ('') |
| SERVICEUSERNUMBER | int |  | YES | ((0)) |
| STATEMENTDESCRIPTOR | nvarchar | 22 | YES | ('') |
| ACCEPTVISA | bit |  | YES | ((0)) |
| ACCEPTMASTERCARD | bit |  | YES | ((0)) |
| ACCEPTAMEX | bit |  | YES | ((0)) |
| ACCEPTDISCOVER | bit |  | YES | ((0)) |
| ACCEPTDINERSCLUB | bit |  | YES | ((0)) |
| ACCEPTJCB | bit |  | YES | ((0)) |
| ACCEPTBANKACCOUNTS | bit |  | YES | ((0)) |
| ACCEPTCASH | bit |  | YES | ((0)) |
| ACCEPTCHECKS | bit |  | YES | ((0)) |
| AVAILABLEFORALLVISA | bit |  | YES | ((0)) |
| AVAILABLEFORALLMASTERCARD | bit |  | YES | ((0)) |
| AVAILABLEFORALLAMEX | bit |  | YES | ((0)) |
| AVAILABLEFORALLDISCOVER | bit |  | YES | ((0)) |
| AVAILABLEFORALLDINERSCLUB | bit |  | YES | ((0)) |
| AVAILABLEFORALLCREDITCARD | bit |  | YES | ((0)) |
| AVAILABLEFORALLBANKACCOUNTS | bit |  | YES | ((0)) |
| AVAILABLEFORALLCASH | bit |  | YES | ((0)) |
| AVAILABLEFORALLCHECKS | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILVISA | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILMASTERCARD | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILAMEX | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILDISCOVER | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILDINERSCLUB | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILCREDITCARD | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILBANKACCOUN | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILCASH | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILCHECKS | bit |  | YES | ((0)) |
| AVAILABLEFORDROPINSCREDITCAR | bit |  | YES | ((0)) |
| AVAILABLEFORDROPINSBANKACCOU | bit |  | YES | ((0)) |
| AVAILABLEFORDROPINSCASH | bit |  | YES | ((0)) |
| AVAILABLEFORDROPINSCHECK | bit |  | YES | ((0)) |
| ISREALTIMEENABLED | bit |  | YES | ((0)) |
| EZIDEBITBRANCHCODE | nvarchar | 50 | YES | ('') |
| EZIDEBITCLIENTCODE | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | ((0)) |

## PaymentProcessorConfigurationType
**Physical table:** `OSUSR_72o_PaymentProcessorConfigurationType`  
**Description:** Static records of PaymentProcessorConfiguration type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PaymentProcessorConfigurationVersion
**Physical table:** `OSUSR_72o_GoEmerchantConfiguration`  
**Description:** Version of payment processor configurations. Old version are kep, so we can perform operation os transactions that wre made with different credentials.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| TRANSACTIONCENTERID | int |  | YES | ((0)) |
| CREDITCARDMID | nvarchar | 50 | YES | ('') |
| CREDITCARDTID | nvarchar | 50 | YES | ('') |
| CREDITCARDPROCESSOR | nvarchar | 50 | YES | ('') |
| CREDITCARDPROCESSORID | nvarchar | 50 | YES | ('') |
| GATEWAYID | nvarchar | 50 | YES | ('') |
| ACHCATEGORY | nvarchar | 50 | YES | ('') |
| DEBITPROCESSORID | nvarchar | 50 | YES | ('') |
| HIGHESTTICKETVALUECC | decimal |  | YES | ((0)) |
| HIGHESTTICKETVALUEACH | decimal |  | YES | ((0)) |
| ACCEPTVISA | bit |  | YES | ((0)) |
| ACCEPTMASTERCARD | bit |  | YES | ((0)) |
| ACCEPTAMEX | bit |  | YES | ((0)) |
| ACCEPTDISCOVER | bit |  | YES | ((0)) |
| ACCEPTBANKACCOUNTS | bit |  | YES | ((0)) |
| ACCEPTCASH | bit |  | YES | ((0)) |
| ACCEPTCHECKS | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| AVAILABLEFORALLVISA | bit |  | YES | ((0)) |
| AVAILABLEFORALLMASTERCARD | bit |  | YES | ((0)) |
| AVAILABLEFORALLAMEX | bit |  | YES | ((0)) |
| AVAILABLEFORALLDISCOVER | bit |  | YES | ((0)) |
| AVAILABLEFORALLBANKACCOUNTS | bit |  | YES | ((0)) |
| AVAILABLEFORALLCASH | bit |  | YES | ((0)) |
| AVAILABLEFORALLCHECKS | bit |  | YES | ((0)) |
| RETAILPROCESSORID | nvarchar | 50 | YES | ('') |
| ACCEPTCARDSWIPE | bit |  | YES | ((0)) |
| AVAILABLEFORALLCARDSWIPE | bit |  | YES | ((0)) |
| ALLOWCARDSWIPEONCOACHBOARD | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILVISA | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILMASTERCARD | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILAMEX | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILDISCOVER | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILBANKACCOUN | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILCASH | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILCHECKS | bit |  | YES | ((0)) |
| PAYMENTPROCESSORID | int |  | YES | (NULL) |
| CREDITCARDMERCHANTACCOUNTNUM | nvarchar | 10 | YES | ('') |
| CREDITCARDSTOREID | nvarchar | 80 | YES | ('') |
| CREDITCARDSTOREPASSWORD | nvarchar | 20 | YES | ('') |
| ACHMERCHANTACCOUNTNUM | nvarchar | 10 | YES | ('') |
| ACHSTOREID | nvarchar | 80 | YES | ('') |
| ACHSTOREPASSWORD | nvarchar | 20 | YES | ('') |
| NAME | nvarchar | 50 | YES | ('') |
| DIGITALKEY | nvarchar | 36 | YES | ('') |
| ACCEPTDINERSCLUB | bit |  | YES | ((0)) |
| AVAILABLEFORALLDINERSCLUB | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILDINERSCLUB | bit |  | YES | ((0)) |
| ISSEPAENABLED | bit |  | YES | ((0)) |
| PAYEE | nvarchar | 81 | YES | ('') |
| CLIENTCODE | nvarchar | 50 | YES | ('') |
| BRANCHCODE | nvarchar | 50 | YES | ('') |
| ISREALTIMEENABLED | bit |  | YES | ((0)) |
| PPCONFIGURATIONTYPEID | int |  | YES | (NULL) |
| ABNNUMBER | nvarchar | 50 | YES | ('') |
| BEANSTREAMMERCHANTID | nvarchar | 50 | YES | ('') |
| BEANSTREAMPAYMENTPROFILEPASS | nvarchar | 50 | YES | ('') |
| BEANSTREAMORDERSETTINGSPASS | nvarchar | 50 | YES | ('') |
| BEANSTREAMREPORTINGPASS | nvarchar | 50 | YES | ('') |
| BEANSTREAMBATCHFILEPASS | nvarchar | 50 | YES | ('') |
| OPTIMALPAYMENTSKEYID | nvarchar | 50 | YES | ('') |
| OPTIMALPAYMENTSKEYPASSWORD | nvarchar | 250 | YES | ('') |
| SERVICEUSERNUMBER | int |  | YES | ((0)) |
| ACCEPTJCB | bit |  | YES | ((0)) |
| AVAILABLEFORALLCREDITCARD | bit |  | YES | ((0)) |
| AVAILABLEFORRETAILCREDITCARD | bit |  | YES | ((0)) |
| AVAILABLEFORDROPINSCREDITCAR | bit |  | YES | ((0)) |
| AVAILABLEFORDROPINSBANKACCOU | bit |  | YES | ((0)) |
| AVAILABLEFORDROPINSCASH | bit |  | YES | ((0)) |
| AVAILABLEFORDROPINSCHECK | bit |  | YES | ((0)) |
| GSTNUMBER | nvarchar | 50 | YES | ('') |
| STATEMENTDESCRIPTOR | nvarchar | 22 | YES | ('') |
| PAYMENTPROCESSORCONFIGHASH | nvarchar | 40 | YES | ('') |
| PPCONFIGURATIONID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_c31_Request`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| REQUESTTYPEID | int |  | YES | (NULL) |
| ISRUNNINGSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISMANUALLYRETRIED | bit |  | YES | ((0)) |
| RETRIEDBY | int |  | YES | (NULL) |
| NUMBEROFTRIES | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| HASFINISHED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERPAYMENTPROCESSORCONF | bigint |  | YES | ((0)) |
| SETDEFAULTPAYMENTMETHODOPTIO | int |  | YES | ((0)) |
| SENDUNVERIFIEDACHEMAILS | bit |  | YES | ((0)) |
| APPLYALLOWEDPAYMENTMETHODS | bit |  | YES | ((0)) |
| ISACTIVATE | bit |  | YES | ((0)) |
| AUTOMATEDEMAILSUBEMAILID | int |  | YES | (NULL) |
| AUTOMATEDEMAILSUBEMAILTEMPID | int |  | YES | (NULL) |
| INVOICEHEADERID | int |  | YES | (NULL) |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |

## RequestImportPaymentMethodImportFile
**Physical table:** `OSUSR_c31_RequestImportPaymentMethodImportFile`  
**Description:** Represents a payment method import file to be completed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUESTID | bigint |  | YES | (NULL) |
| IMPORTTYPE | int |  | YES | ((0)) |
| IMPORTFILE | varbinary | -1 | YES | (NULL) |

## RequestImportPaymentMethodImportLog
**Physical table:** `OSUSR_c31_RequestImportPaymentMethodImportLog`  
**Description:** Represents a log for a given payment method import.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUESTIMPORTFILEID | bigint |  | YES | (NULL) |
| SHEETNAME | nvarchar | 50 | YES | ('') |
| LINE | int |  | YES | ((0)) |
| VALID | bit |  | YES | ((0)) |
| INVALIDMESSAGE | nvarchar | 1500 | YES | ('') |

## RequestType
**Physical table:** `OSUSR_c31_RequestType`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## SharedPaymentMethod
**Physical table:** `OSUSR_72o_SharedPaymentMethod`  
**Description:** Entity that will have the information for the shared payment methods.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| PAYMENTMETHODID | int |  | YES | (NULL) |
| SHAREDUSERID | int |  | YES | (NULL) |
| ISDEFAULT | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## StoreCredit
**Physical table:** `OSUSR_72o_StoreCredit`  
**Description:** Represents the store credit that a user has available at a given Customer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| PAYMENTPROCESSORCONFIGURATIO | int |  | YES | (NULL) |
| CREDITAVAILABLE | decimal |  | YES | ((0)) |

## TaxRate
**Physical table:** `OSUSR_72o_TaxRate`  
**Description:** Contains information of tax rate  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| TAXRATETYPEID | int |  | YES | (NULL) |
| TAXRATENAME | nvarchar | 500 | YES | ('') |
| TAXRATE | decimal |  | YES | ((0)) |
| DISPLAYNAME | nvarchar | 525 | YES | ('') |
| ISSYSTEMTAXRATE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## TaxRateType
**Physical table:** `OSUSR_72o_TaxRateType`  
**Description:** Static records of Tax Rate type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Transaction
**Physical table:** `OSUSR_72o_Transaction`  
**Description:** Financial transaction. Represents a transfer of money.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| INVOICEID | int |  | YES | (NULL) |
| PAYMENTMETHODID | int |  | YES | (NULL) |
| AMOUNT | decimal |  | YES | ((0)) |
| CHECKNUMBER | nvarchar | 20 | YES | ('') |
| TRANSACTIONTYPEID | int |  | YES | (NULL) |
| TRANSACTIONRESULTID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ORDERID | nvarchar | 50 | YES | ('') |
| ERRORTEXT | nvarchar | 2000 | YES | ('') |
| REFERENCENUMBER | nvarchar | 50 | YES | ('') |
| PARENTTRANSACTION | int |  | YES | (NULL) |
| FULLRESPONSE | nvarchar | 2000 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HASSETTLED | bit |  | YES | ((0)) |
| STATUSUPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| LOCATIONID | int |  | YES | (NULL) |
| CREDITCARDTYPE | nvarchar | 50 | YES | ('') |
| CREDITCARDLASTFOURDIGITS | nvarchar | 4 | YES | ('') |
| INVOICEHEADERID | int |  | YES | (NULL) |
| PARENTTRANSACTIONID | int |  | YES | (NULL) |
| ERRORCODE | nvarchar | 50 | YES | ('') |
| TRANSACTIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYMENTPROCESSORCONFIGURATIO | int |  | YES | (NULL) |
| BANKRECEIPTID | nvarchar | 50 | YES | ('') |
| CREATEDONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISPENDING | bit |  | YES | ((0)) |
| SETTLEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| EFFECTIVEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ACTUALSETTLEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ANONCCPAYMENTACCOUNTSOURCEID | int |  | YES | (NULL) |
| AUTHTEXT | nvarchar | 2000 | YES | ('') |
| POSTURL | nvarchar | 500 | YES | ('') |
| OUTBOUNDPOST | nvarchar | -1 | YES | ('') |
| FEES | decimal |  | YES | ((0)) |
| NETAMOUNT | decimal |  | YES | ((0)) |
| PAYMENTPROCESSORCONFIGHASH | nvarchar | 40 | YES |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PASSEDFEES | decimal |  | YES | ((0)) |
| CAPITALPAYDOWNAMOUNT | decimal |  | YES | ((0)) |

## TransactionStripePaymentMethod
**Physical table:** `OSUSR_72o_TransactionStripePaymentMethod`  
**Description:** Relates a Transaction to a Stripe Payment Method. Whenever a Transaction occurs in a Stripe Customer, a record is created here.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TRANSACTIONID | int |  | NO |  |
| STRIPEPAYMENTMETHODID | bigint |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| TENANT_ID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## TransactionStripeTransaction
**Physical table:** `OSUSR_72o_TransactionStripeTransaction`  
**Description:** Relates a Core transaction to a Stripe transaction.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| STRIPETRANSACTIONID | bigint |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## TransactionType
**Physical table:** `OSUSR_72o_TransactionType`  
**Description:** Possible transaction types  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INTERNALNAME | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| LABEL | nvarchar | 50 | YES | ('') |
| PAYMENTACCOUNTTYPE | int |  | YES | (NULL) |
| ISREFUND | bit |  | YES | ((0)) |
| ISPAYMENT | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CANSETTLE | bit |  | YES | ((0)) |
| AUTOUPDATESTATUS | bit |  | YES | ((0)) |
| ISVOID | bit |  | YES | ((0)) |
| CANVOID | bit |  | YES | ((0)) |
| RECHECKSETTLEPOSTSETTLE | bit |  | YES | ((0)) |
| ISSTORECREDIT | bit |  | YES | ((0)) |
| ISSYSTEMCREDIT | bit |  | YES | ((0)) |
