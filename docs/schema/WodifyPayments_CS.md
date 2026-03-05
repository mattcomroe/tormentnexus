# WodifyPayments_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [BeneficialOwnerBusinessRole](#beneficialownerbusinessrole)
- [ChargebackStatus](#chargebackstatus)
- [DisputeEvidence](#disputeevidence)
- [Request](#request)
- [RequestType](#requesttype)
- [StripeChargebackFee](#stripechargebackfee)
- [StripeConfiguration](#stripeconfiguration)
- [StripeConfigurationAccess](#stripeconfigurationaccess)
- [StripeConfigurationBusinessType](#stripeconfigurationbusinesstype)
- [StripeConfigurationDisabledReason](#stripeconfigurationdisabledreason)
- [StripeConfigurationPaymentAccountType](#stripeconfigurationpaymentaccounttype)
- [StripeConfigurationRate](#stripeconfigurationrate)
- [StripeConfigurationStatus](#stripeconfigurationstatus)
- [StripeCustomer](#stripecustomer)
- [StripeCustomerGlobaUser](#stripecustomerglobauser)
- [StripeDispute](#stripedispute)
- [StripeDisputeReason](#stripedisputereason)
- [StripeDisputeStatus](#stripedisputestatus)
- [StripeDisputeTransaction](#stripedisputetransaction)
- [StripeFailedTransfersTemp](#stripefailedtransferstemp)
- [StripeNegativePayoutsPending](#stripenegativepayoutspending)
- [StripePaymentMethod](#stripepaymentmethod)
- [StripePaymentMethodCustomerDefault](#stripepaymentmethodcustomerdefault)
- [StripePaymentMethodStatus](#stripepaymentmethodstatus)
- [StripePayout](#stripepayout)
- [StripePayoutNotificationContact](#stripepayoutnotificationcontact)
- [StripePayoutQueue](#stripepayoutqueue)
- [StripePayoutRecalculateQueue](#stripepayoutrecalculatequeue)
- [StripePayoutStatus](#stripepayoutstatus)
- [StripePayoutTransaction](#stripepayouttransaction)
- [StripePayoutTransactionQueue](#stripepayouttransactionqueue)
- [StripePayoutTransactionType](#stripepayouttransactiontype)
- [StripePendingTransfer](#stripependingtransfer)
- [StripeRefundReason](#striperefundreason)
- [StripeSEPAMandateRequest](#stripesepamandaterequest)
- [StripeSharedPaymentMethod](#stripesharedpaymentmethod)
- [StripeSupportedCurrency](#stripesupportedcurrency)
- [StripeTransaction](#stripetransaction)
- [StripeTransactionType](#stripetransactiontype)
- [StripeTransfer](#stripetransfer)
- [StripeTransferStatus](#stripetransferstatus)
- [StripeTransferTransaction](#stripetransfertransaction)
- [StripeWebhookEvent](#stripewebhookevent)
- [StripeWebhookEventType](#stripewebhookeventtype)
- [WodifyPaymentsAccountDetail](#wodifypaymentsaccountdetail)
- [WodifyPaymentsBeneficialOwner](#wodifypaymentsbeneficialowner)

## AsyncProcess
**Physical table:** `OSUSR_sdl_AsyncProcess4`  
**Description:** Auxiliar entity that contains all Wodify Payments asynchronous processes, which will run through the WodifyPayments_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ASYNCPROCESSTYPEID | int |  | YES | (NULL) |
| REQUESTID | bigint |  | YES | (NULL) |

## BeneficialOwnerBusinessRole
**Physical table:** `OSUSR_sdl_BeneficialOwnerBusinessRole`  
**Description:** Types of individuals associated with a business for a Stripe account.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ChargebackStatus
**Physical table:** `OSUSR_sdl_ChargebackStatus`  
**Description:** Represents the possible chargeback statuses.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## DisputeEvidence
**Physical table:** `OSUSR_sdl_DisputeEvidence`  
**Description:** Evidence submitted as response to a dispute.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TRANSACTIONDISPUTEID | bigint |  | YES | (NULL) |
| SERVICEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ATHLETENAME | nvarchar | 200 | YES | ('') |
| CUSTOMEREMAILADDRESS | nvarchar | 250 | YES | ('') |
| BILLINGADDRESS | nvarchar | 200 | YES | ('') |
| PRODUCTDESCRIPTION | nvarchar | 2000 | YES | ('') |
| REFUNDREFUSALEXPLANATION | nvarchar | 2000 | YES | ('') |
| EVIDENCESUBMITCOUNT | int |  | YES | ((0)) |
| SUBMITSIGNEDCONTRACT | bit |  | YES | ((0)) |
| SUBMITATTENDANCEHISTORY | bit |  | YES | ((0)) |
| SUBMITEMAILEDRECEIPT | bit |  | YES | ((0)) |
| ADDITIONALEVIDENCEFSTORAGEID | int |  | YES | (NULL) |
| SIGNEDCONTRACTFILESTORAGEID | int |  | YES | (NULL) |
| ATTENDANCEHISTORYFSTORAGEID | int |  | YES | (NULL) |
| RECEIPTFILESTORAGEID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |

## Request
**Physical table:** `OSUSR_sdl_Request`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ISACTIVATE | bit |  | YES | ((0)) |
| ACCOUNTID | nvarchar | 50 | YES | ('') |
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
| ATTRIBUTES | nvarchar | -1 | YES | ('') |

## RequestType
**Physical table:** `OSUSR_sdl_RequestTypeId`  
**Description:** Type of request record  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## StripeChargebackFee
**Physical table:** `OSUSR_sdl_StripeChargebackFee`  
**Description:** Chargeback Fees  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COUNTRYID | int |  | YES | (NULL) |
| CHARGEBACKFEE | decimal |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## StripeConfiguration
**Physical table:** `OSUSR_ksl_StripeConfiguration`  
**Description:** Represents a Stripe or "Wodify Payments" configuration. These are the configurable settings on the Stripe configuration screen and drive the behavior of how Stripe is used.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPECONFIGURATIONSTATUSID | int |  | YES | (NULL) |
| STRIPECONFIGURATIONRATEID | bigint |  | YES | (NULL) |
| BUSINESSTYPEID | int |  | YES | (NULL) |
| LEGALBUSINESSNAME | nvarchar | 50 | YES | ('') |
| EMPLOYERIDENTIFICATIONNUMBER | nvarchar | 50 | YES | ('') |
| STREETADDRESSLINE1 | nvarchar | 50 | YES | ('') |
| STREETADDRESSLINE2 | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| PROVINCE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| POSTALCODE | nvarchar | 20 | YES | ('') |
| DESCRIPTION | nvarchar | 350 | YES | ('') |
| OWNERFIRSTNAME | nvarchar | 50 | YES | ('') |
| OWNERLASTNAME | nvarchar | 50 | YES | ('') |
| OWNERDATEOFBIRTH | datetime |  | YES | ('1900-01-01 00:00:00') |
| OWNERLASTFOURSSN | nvarchar | 4 | YES | ('') |
| STATEMENTDESCRIPTOR | nvarchar | 22 | YES | ('') |
| SUPPORTPHONENUMBER | nvarchar | 20 | YES | ('') |
| BANKROUTINGNUMBER | nvarchar | 20 | YES | ('') |
| BANKACCOUNTNUMBER | nvarchar | 2000 | YES | ('') |
| SECRETKEY | nvarchar | 50 | YES | ('') |
| PUBLISHABLEKEY | nvarchar | 50 | YES | ('') |
| ACCOUNTID | nvarchar | 50 | YES | ('') |
| FIELDSNEEDED | nvarchar | 2000 | YES | ('') |
| FIELDSNEEDEDBY | datetime |  | YES | ('1900-01-01 00:00:00') |
| DISABLEDREASONID | int |  | YES | (NULL) |
| TERMSOFSERVICEACCEPTEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| IDENTITYDOCUMENTFILEID | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENABLENOTIFICATIONPAYOUT | bit |  | YES | ((0)) |
| ENABLEFRAUDPREVENTIONCVV | bit |  | YES | ((0)) |
| ENABLEFRAUDPREVENTIONZIPCODE | bit |  | YES | ((0)) |
| NAME | nvarchar | 50 | YES | ('') |
| BANKACCOUNTUPDATEDBY | int |  | YES | (NULL) |
| BANKACCOUNTUPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| VERIFICATIONINFOPROVIDEDBY | int |  | YES | (NULL) |
| VERIFICATIONINFOPROVIDEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CURRENCYCODE | nvarchar | 3 | YES | ('') |
| TERMSOFSERVICEACCEPTEDIP | nvarchar | 45 | YES | ('') |
| SORTCODE | nvarchar | 6 | YES | ('') |
| TRANSITNUMBER | nvarchar | 5 | YES | ('') |
| INSTITUTIONNUMBER | nvarchar | 3 | YES | ('') |
| TAXID | nvarchar | 50 | YES | ('') |
| BANKACCOUNTHOLDERNAME | nvarchar | 200 | YES | ('') |
| BANKACCOUNTHOLDERTYPE | int |  | YES | (NULL) |
| ACCOUNTUPDATEDEMAILLASTSENT | datetime |  | YES | ('1900-01-01 00:00:00') |
| INSTANTPAYOUTREMAINDER | decimal |  | YES | ((0)) |

## StripeConfigurationAccess
**Physical table:** `OSUSR_sdl_StripeConfigurationAccess`  
**Description:** Entity to keep track of the users who have access to a StripeConfiguration, which means, admins and managers for Core and organizers for Arena.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| WODIFYPRODUCTID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## StripeConfigurationBusinessType
**Physical table:** `OSUSR_ksl_StripeConfigurationBusinessType`  
**Description:** Represents the possible business types applied to a configuration.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## StripeConfigurationDisabledReason
**Physical table:** `OSUSR_ksl_StripeConfigurationDisabledReason`  
**Description:** The possible reasons a Stripe Configuration can be disabled.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## StripeConfigurationPaymentAccountType
**Physical table:** `OSUSR_ksl_StripeConfigurationPaymentAccountType`  
**Description:** The payment account types for a given Stripe Configuration.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| PAYMENTACCOUNTTYPEID | int |  | YES | (NULL) |
| ISENABLEDFORMEMBERSHIP | bit |  | YES | ((0)) |
| ISENABLEDFORRETAIL | bit |  | YES | ((0)) |
| ISENABLEDFORDROPIN | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## StripeConfigurationRate
**Physical table:** `OSUSR_ksl_StripeConfigurationRate`  
**Description:** Represents the rates for a Stripe or "Wodify Payments" configuration. These are configurable from the Customer Edit screen in Management and apply for all Locations at the Customer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| PERCENTAGEPERTRANSACTION | decimal |  | YES | ((0)) |
| AMOUNTPERTRANSACTION | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CC_PERCENTAGEPERTRANSACTION | decimal |  | YES | ((0)) |
| CC_AMOUNTPERTRANSACTION | decimal |  | YES | ((0)) |
| ACH_PERCENTAGEPERTRANSACTION | decimal |  | YES | ((0)) |
| ACH_AMOUNTPERTRANSACTION | decimal |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |

## StripeConfigurationStatus
**Physical table:** `OSUSR_ksl_StripeConfigurationStatus`  
**Description:** Represents the status of a Stripe Configuration.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## StripeCustomer
**Physical table:** `OSUSR_ksl_StripeCustomer`  
**Description:** Represents a Customer inside Stripe.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |
| CUSTOMERID | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## StripeCustomerGlobaUser
**Physical table:** `OSUSR_ksl_StripeCustomerGlobaUser`  
**Description:** Represents a Global User's Stripe Customer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| STRIPECUSTOMERID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |

## StripeDispute
**Physical table:** `OSUSR_ksl_StripeDispute`  
**Description:** Represents a dispute created in Stripe. A dispute occurs when a customer questions a charge with their bank or credit card company made via Stripe.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DISPUTEID | nvarchar | 50 | YES | ('') |
| AMOUNT | decimal |  | YES | ((0)) |
| CHARGEID | nvarchar | 50 | YES | ('') |
| STRIPEDISPUTESTATUSID | int |  | YES | (NULL) |
| STRIPEDISPUTEREASONID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EVIDENCEDUEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| STRIPECREATETIMESTAMP | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## StripeDisputeReason
**Physical table:** `OSUSR_ksl_StripeDisputeReason1`  
**Description:** Represents the possible reasons a Stripe Dispute can have.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 500 | YES | ('') |

## StripeDisputeStatus
**Physical table:** `OSUSR_ksl_StripeDisputeStatus1`  
**Description:** Represents the possible statuses a Stripe Dispute can have.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISFINALSTATUS | bit |  | YES | ((0)) |

## StripeDisputeTransaction
**Physical table:** `OSUSR_sdl_StripeDisputeTransaction`  
**Description:** Relates a Transaction to a Stripe Dispute (chargeback). Whenever a dispute is created in Stripe and we are notified, a record is created here referencing the StripeDispute record.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPETRANSACTIONID | bigint |  | YES | (NULL) |
| STRIPEDISPUTEID | bigint |  | YES | (NULL) |
| CHARGEBACKSTATUSID | int |  | YES | (NULL) |
| LASTSTATUSCHANGEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CHARGEBACKOCCURRED | bit |  | YES | ((0)) |
| ISACCEPTED | bit |  | YES | ((0)) |
| ACCEPTEDBY | int |  | YES | (NULL) |
| ACCEPTEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## StripeFailedTransfersTemp
**Physical table:** `OSUSR_sdl_StripeFailedTransfersTemp`  
**Description:** holds transaction info for failed transfers that need to be re-run. table will be deleted when transfers are re-run.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TRANSACTIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| TRANSACTIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TRANSFERDESTINATION | nvarchar | 50 | YES | ('') |
| TRANSFERSOURCE | nvarchar | 50 | YES | ('') |
| TRANSFERCURRENCY | nvarchar | 50 | YES | ('') |
| TRANSFERAMOUNT | bigint |  | YES | ((0)) |
| CHARGEID | nvarchar | 50 | YES | ('') |
| DISPUTEID | nvarchar | 50 | YES | ('') |
| TRANSACTIONID | bigint |  | YES | ((0)) |
| INVOICEHEADERID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ISREADYTORERUN | bit |  | YES | ((0)) |
| SUCCESSDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ERRORMESSAGE | nvarchar | 2000 | YES | ('') |

## StripeNegativePayoutsPending
**Physical table:** `OSUSR_sdl_StripeNegativePayoutsPending`  
**Description:** Table containing negative Stripe Payouts that were not yet processed by Stripe. When Stripe confirms the payout (either with success or not) the record is deleted from this table.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| STRIPEPAYOUTID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## StripePaymentMethod
**Physical table:** `OSUSR_ksl_StripePaymentMethod`  
**Description:** Represents a payment method used for purchases against a Stripe Configuration. This is tied to the global user and can be used against any Stripe Configurations associated with any account (Customer).  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| STRIPECUSTOMERID | bigint |  | YES | (NULL) |
| PAYMENTACCOUNTSOURCEID | int |  | YES | (NULL) |
| STRIPEPAYMENTMETHODSTATUSID | int |  | YES | (NULL) |
| STRIPEID | nvarchar | 200 | YES | ('') |
| PLAIDACCESSTOKEN | nvarchar | -1 | YES | ('') |
| LASTFOURDIGITS | nvarchar | 4 | YES | ('') |
| EXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| VERIFICATIONATTEMPTS | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| STRIPEAPI | int |  | YES | ((0)) |
| SETUPFORMERCHINITIATEDTRANS | bit |  | YES | ((0)) |
| STRIPESETUPINTENTID | nvarchar | 200 | YES | ('') |
| STRIPEMANDATEID | nvarchar | 200 | YES | ('') |

## StripePaymentMethodCustomerDefault
**Physical table:** `OSUSR_ksl_StripePaymentMethodTenantDefault`  
**Description:** Represents the default payment method for a Global User at a given customer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |
| STRIPEPAYMENTMETHODID | bigint |  | YES | (NULL) |
| TENANTID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | ((0)) |

## StripePaymentMethodStatus
**Physical table:** `OSUSR_ksl_StripePaymentMethodStatus`  
**Description:** The possible statuses a Stripe payment method can have.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## StripePayout
**Physical table:** `OSUSR_sdl_StripePayout`  
**Description:** A payout is a transfer of funds from the payment processor to the client's bank account. It usually occurs daily and has an amount that matches the sum of all transactions the client executed since the last payout. If a configuration is deleted, all payouts tied to that configuration will be deleted as well.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| PAYOUTSTATUSID | int |  | YES | (NULL) |
| EXTERNALID | nvarchar | 50 | YES | ('') |
| CHARGESTOTAL | decimal |  | YES | ((0)) |
| REFUNDSTOTAL | decimal |  | YES | ((0)) |
| ADJUSTMENTSTOTAL | decimal |  | YES | ((0)) |
| FEESTOTAL | decimal |  | YES | ((0)) |
| NETTOTAL | decimal |  | YES | ((0)) |
| RETRIEDONPAYOUTID | bigint |  | YES | (NULL) |
| ISFAILED | bit |  | YES | ((0)) |
| FAILEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| FAILURECODE | nvarchar | 50 | YES | ('') |
| FAILUREMESSAGE | nvarchar | 500 | YES | ('') |
| PASSEDFEESTOTAL | decimal |  | YES | ((0)) |
| CAPITALPAYDOWNTOTAL | decimal |  | YES | ((0)) |
| ISINSTANTPAYOUT | bit |  | YES | ((0)) |
| TRANSFERSTOTAL | decimal |  | YES | ((0)) |
| HASINSTANTPAYOUTTRANSACTIONS | bit |  | YES | ((0)) |
| UNATTRIBUTEDREMAINDER | decimal |  | YES | ((0)) |

## StripePayoutNotificationContact
**Physical table:** `OSUSR_ksl_StripePayoutNotification`  
**Description:** Users and email addresses that should be emailed when a Stripe Payout occurs.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| PAYOUTNOTIFICATIONUSERID | int |  | YES | (NULL) |
| PAYOUTNOTIFICATIONEMAIL | nvarchar | 300 | YES | ('') |

## StripePayoutQueue
**Physical table:** `OSUSR_sdl_StripePayoutQueue`  
**Description:** Represents a payout that needs to be processed. This involves matching the balance transactions in the payment processor's system with ours and updating the payout status.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PAYOUTID | bigint |  | YES | (NULL) |
| ATTEMPTS | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| LASTATTEMPTED | datetime |  | YES | ('1900-01-01 00:00:00') |

## StripePayoutRecalculateQueue
**Physical table:** `OSUSR_sdl_StripePayoutRecalculateQueue`  
**Description:** Represents a payout that needs to have its totals updated.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPEPAYOUTID | bigint |  | YES | (NULL) |

## StripePayoutStatus
**Physical table:** `OSUSR_sdl_StripePayoutStatus`  
**Description:** Possible statuses a payout can have.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## StripePayoutTransaction
**Physical table:** `OSUSR_sdl_StripePayoutTransaction`  
**Description:** Indicates in which payout a transaction is included, which is to say, it points to the date the transaction's money will be transfered to the client's bank account.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPEPAYOUTID | bigint |  | YES | (NULL) |
| STRIPETRANSACTIONID | bigint |  | YES | (NULL) |
| BALANCETRANSACTIONID | nvarchar | 50 | YES | ('') |
| ISREMOVED | bit |  | YES | ((0)) |
| ISINFERRED | bit |  | YES | ((0)) |
| INFERREDBYPAYOUTID | bigint |  | YES | (NULL) |

## StripePayoutTransactionQueue
**Physical table:** `OSUSR_sdl_StripePayoutTransactionQueue`  
**Description:** Represents a transaction that needs to be processed and assigned to a payout. When a transaction occurs, we insert a record here to be queried from the payment processor's system and then added a payout on our side.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPETRANSACTIONID | bigint |  | YES | (NULL) |
| TRANSFERID | nvarchar | 50 | YES | ('') |
| ATTEMPTS | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| LASTATTEMPTED | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISREMOVED | bit |  | YES | ((0)) |

## StripePayoutTransactionType
**Physical table:** `OSUSR_sdl_StripePayoutTransactionType`  
**Description:** Represents the type of transactions available in a payout.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## StripePendingTransfer
**Physical table:** `OSUSR_sdl_StripePendingTransfer`  
**Description:** Entity that stores the data for failed transfers due to insufficient funds.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPETRANSFERID | bigint |  | YES | (NULL) |
| COUNTRYID | int |  | YES | (NULL) |
| PACKAGEID | nvarchar | 50 | YES | ('') |
| BANK_FAILEDPAYMENTFEE | decimal |  | YES | ((0)) |
| CARD_FAILEDPAYMENTFEE | decimal |  | YES | ((0)) |
| STRIPETRANSACTIONID | bigint |  | YES | (NULL) |
| TENANT_ID | int |  | YES | (NULL) |
| WODIFYPRODUCTID | int |  | YES | (NULL) |
| INVOICEHEADERID | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| STRIPEDISPUTEID | bigint |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| ISDISPUTE | bit |  | YES | ((0)) |
| AMOUNT | decimal |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |

## StripeRefundReason
**Physical table:** `OSUSR_ksl_StripeRefundReason`  
**Description:** The possible refund reasons.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| CODE | nvarchar | 50 | YES | ('') |

## StripeSEPAMandateRequest
**Physical table:** `OSUSR_sdl_StripeSEPAMandateRequest`  
**Description:** Entity with information related with mandates for direct debits. Only used for Wodify Payments accounts that uses SEPA.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| STRIPEPAYMENTMETHODID | bigint |  | YES | (NULL) |
| COUNTRYID | int |  | YES | (NULL) |
| CUSTOMERIP | nvarchar | 15 | YES | ('') |
| ISSIGNED | bit |  | YES | ((0)) |
| USERSIGNMANDATE | varbinary | -1 | YES | (NULL) |
| DATESIGNED | datetime |  | YES | ('1900-01-01 00:00:00') |
| MANDATEREFERENCE | nvarchar | 35 | YES | ('') |
| MANDATEURL | nvarchar | 300 | YES | ('') |
| SENTBYEMAILON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## StripeSharedPaymentMethod
**Physical table:** `OSUSR_ksl_StripeSharedPaymentMethod`  
**Description:** Entity that will have the information for the shared payment methods.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| STRIPEPAYMENTMETHODID | bigint |  | YES | (NULL) |
| STRIPECUSTOMERGLOBAUSERID | bigint |  | YES | (NULL) |
| GLOBALUSERID | int |  | YES | (NULL) |
| SHAREDGLOBALUSERID | int |  | YES | (NULL) |
| ISDEFAULT | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## StripeSupportedCurrency
**Physical table:** `OSUSR_ksl_StripeSupportedCurrency`  
**Description:** The supported currencies by Stripe.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| CURRENCYCODE | nvarchar | 50 | YES | ('') |

## StripeTransaction
**Physical table:** `OSUSR_sdl_StripeTransaction`  
**Description:** Record of a money transaction.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DESCRIPTION | nvarchar | 200 | YES | ('') |
| EXTERNALID | nvarchar | 50 | YES | ('') |
| AMOUNT | decimal |  | YES | ((0)) |
| FEES | decimal |  | YES | ((0)) |
| NETAMOUNT | decimal |  | YES | ((0)) |
| WODIFYPRODUCTID | int |  | YES | (NULL) |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| TRANSACTIONTYPEID | int |  | YES | (NULL) |
| TRANSACTIONRESULTSTATUSID | int |  | YES | (NULL) |
| PAYMENTACCOUNTSOURCEID | int |  | YES | (NULL) |
| STRIPEPAYMENTMETHODID | bigint |  | YES | (NULL) |
| PARENTTRANSACTIONID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| TRANSFERGROUP | nvarchar | 50 | YES | ('') |
| CHARGEAVAILABLEONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| IPADDRESS | nvarchar | 45 | YES | ('') |
| PAYMENTINTENTID | nvarchar | 50 | YES | ('') |
| PASSEDFEES | decimal |  | YES | ((0)) |
| CAPITALPAYDOWNAMOUNT | decimal |  | YES | ((0)) |

## StripeTransactionType
**Physical table:** `OSUSR_sdl_StripeTransactionType`  
**Description:** Type of operation that generated the transaction.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| PAYOUTLABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| STRIPEPAYOUTTRANSACTIONTYPE | int |  | YES | (NULL) |
| WODIFYPRODUCTID | int |  | YES | (NULL) |
| SHOWINPAYOUT | bit |  | YES | ((0)) |

## StripeTransfer
**Physical table:** `OSUSR_ksl_StripeTransfer`  
**Description:** Represents a transfer created in Stripe. A transfer can be created manually to move funds from one account to another, or automatically via Stripe.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TRANSFERID | nvarchar | 50 | YES | ('') |
| AMOUNT | decimal |  | YES | ((0)) |
| SOURCEACCOUNT | nvarchar | 50 | YES | ('') |
| DESTINATIONACCOUNT | nvarchar | 50 | YES | ('') |
| STRIPETRANSFERSTATUSID | int |  | YES | (NULL) |
| STRIPECREATETIMESTAMP | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CURRENCYCODE | nvarchar | 3 | YES | ('') |
| SOURCESTRIPECONFIGID | bigint |  | YES | (NULL) |
| DESTINATIONSTRIPECONFIGID | bigint |  | YES | (NULL) |
| WODIFYPRODUCTID | int |  | YES | (NULL) |
| SCHEDULEDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## StripeTransferStatus
**Physical table:** `OSUSR_ksl_StripeTransferStatus`  
**Description:** The possible transfer statuses.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## StripeTransferTransaction
**Physical table:** `OSUSR_sdl_StripeTransferTransaction`  
**Description:** Transactions that were generated as a result of executing a Stripe Transfer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPETRANSFERID | bigint |  | YES | (NULL) |
| STRIPETRANSACTIONID | bigint |  | YES | (NULL) |

## StripeWebhookEvent
**Physical table:** `OSUSR_sdl_StripeWebhookEvent`  
**Description:** Represents a webhook event that was delivered to our Stripe API from Stripe.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EVENTID | nvarchar | 50 | YES | ('') |
| OBJECTID | nvarchar | 50 | YES | ('') |
| STRIPEWEBHOOKEVENTTYPEID | int |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## StripeWebhookEventType
**Physical table:** `OSUSR_sdl_StripeWebhookEventType`  
**Description:** Represents the types of webhook events we store in the database.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| EVENTTYPE | nvarchar | 50 | YES | ('') |

## WodifyPaymentsAccountDetail
**Physical table:** `OSUSR_sdl_WodifyPaymentsAccountDetail`  
**Description:** Entity that coutains information related with a Wodify Payments Account.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| STRIPECONFIGURATIONID | bigint |  | NO |  |
| LEGALNAME | nvarchar | 200 | YES | ('') |
| EIN | nvarchar | 12 | YES | ('') |
| MCC | nvarchar | 4 | YES | ('') |
| PHONENUMBER | nvarchar | 20 | YES | ('') |
| STREETADDRESSLINE1 | nvarchar | 50 | YES | ('') |
| STREETADDRESSLINE2 | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| PROVINCE | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| COUNTRYID | int |  | YES | (NULL) |
| ZIPCODE | nvarchar | 20 | YES | ('') |
| DESCRIPTION | nvarchar | 350 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ALLDIRECTORSDECLARED | bit |  | YES | ((0)) |
| ALLRELEVANTOWNERSDECLARED | bit |  | YES | ((0)) |
| BUSINESSNAME | nvarchar | 200 | YES | ('') |
| BUSINESSURL | nvarchar | 1024 | YES | ('') |
| SUPPORTEMAIL | nvarchar | 250 | YES | ('') |
| SUPPORTURL | nvarchar | 1024 | YES | ('') |
| COMPANYVATNUMBER | nvarchar | 50 | YES | ('') |

## WodifyPaymentsBeneficialOwner
**Physical table:** `OSUSR_sdl_WodifyPaymentsBeneficialOwner`  
**Description:** Information related with the owners of a Wodify Payments Account.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| STRIPECONFIGURATIONID | bigint |  | YES | (NULL) |
| BUSINESSROLEID | int |  | YES | (NULL) |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| DATEOFBIRTH | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAIL | nvarchar | 250 | YES | ('') |
| TITLE | nvarchar | 50 | YES | ('') |
| OWNERSHIPPERCENTAGE | decimal |  | YES | ((0)) |
| PHONENUMBER | nvarchar | 20 | YES | ('') |
| STREETADDRESSLINE1 | nvarchar | 50 | YES | ('') |
| STREETADDRESSLINE2 | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| PROVINCE | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| COUNTRYID | int |  | YES | (NULL) |
| ZIPCODE | nvarchar | 20 | YES | ('') |
| LASTFOURSSN | nvarchar | 4 | YES | ('') |
| PERSONID | nvarchar | 50 | YES | ('') |
| IDENTITYDOCUMENTFILEID | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| BACKOFIDENTITYDOCUMENTFILEID | nvarchar | 50 | YES | ('') |
| FIELDSNEEDED | nvarchar | 500 | YES | ('') |
| IDENTITYDOCUMENTERRORMESSAGE | nvarchar | 1024 | YES | ('') |
| VERIFICATIONSTATUS | int |  | YES | ((0)) |
| VERIFICATIONERRORMESSAGE | nvarchar | 1024 | YES | ('') |
