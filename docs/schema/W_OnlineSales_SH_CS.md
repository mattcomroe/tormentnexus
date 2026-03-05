# W_OnlineSales_SH_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [IllegalWodifySubdomain](#illegalwodifysubdomain)
- [OnlineMembership](#onlinemembership)
- [OnlineMembershipExpirationType](#onlinemembershipexpirationtype)
- [OnlineMembershipLocation](#onlinemembershiplocation)
- [OnlineMembershipPaymentOption](#onlinemembershippaymentoption)
- [OnlineMembershipPaymentOptionKey](#onlinemembershippaymentoptionkey)
- [OnlineMembershipProgram](#onlinemembershipprogram)
- [OnlineMembershipSale](#onlinemembershipsale)
- [OnlineMembershipSaleFailedPaymentMessage](#onlinemembershipsalefailedpaymentmessage)
- [OnlineMembershipType](#onlinemembershiptype)
- [Order](#order)
- [OrderFulfillmentJob](#orderfulfillmentjob)
- [OrderFulfillmentJobStatus](#orderfulfillmentjobstatus)
- [OrderFulfillmentLog](#orderfulfillmentlog)
- [OrderStatus](#orderstatus)
- [OrderType](#ordertype)
- [OrderUserMessage](#orderusermessage)
- [Request](#request)
- [RequestType](#requesttype)

## AsyncProcess
**Physical table:** `OSUSR_2o0_AsyncProcess`  
**Description:** Auxiliar entity that contains all membership asynchronous processes, which will run through the Membership_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## IllegalWodifySubdomain
**Physical table:** `OSUSR_72o_IllegalWodifySubdomain`  
**Description:** Entity holding reserved words that can't be used for an OSP subdomain  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SUBDOMAIN | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## OnlineMembership
**Physical table:** `OSUSR_72o_OnlineMembership`  
**Description:** Holds details for an online membership  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 250 | YES | ('') |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| ONLINEMEMBERSHIPTYPEID | int |  | YES | (NULL) |
| MEMBERPLANTEMPLATEID | int |  | YES | (NULL) |
| PAYMENTSCHEDULEID | int |  | YES | (NULL) |
| PICKLISTVALUEID | int |  | YES | (NULL) |
| ATTENDANCELIMIT | int |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISONLINESALESACTIVE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| EXPIRES | bit |  | YES | ((0)) |
| EXPIRATIONLENGTH | int |  | YES | ((0)) |
| EXPIRATIONTYPE | int |  | YES | (NULL) |
| EXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYATTHEGYMOPTION | bit |  | YES | ((0)) |
| MEMBERSHIPEXPIRATIONTYPEID | int |  | YES | (NULL) |
| CONFIRMATIONPAGETEXT | nvarchar | -1 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## OnlineMembershipExpirationType
**Physical table:** `OSUSR_72o_OnlineMembershipExpirationType`  
**Description:** Lookup table of the expiration types of OnlineMemberships  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## OnlineMembershipLocation
**Physical table:** `OSUSR_72o_OnlineMembershipLocation`  
**Description:** Records that hold information about online memberships per location  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| ONLINEMEMBERSHIPID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| TAXRATEID | int |  | YES | (NULL) |
| ISFREETRIALENABLED | bit |  | YES | ((0)) |
| ISDROPINENABLED | bit |  | YES | ((0)) |
| NONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| ATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| ISONLINESALESACTIVE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| EARLIESTSTARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYATTHEGYMOPTION | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ONLINESALESDISPLAYORDER | int |  | YES | ((0)) |
| ISMOBILESALESACTIVE | bit |  | YES | ((0)) |
| LATESTSTARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |

## OnlineMembershipPaymentOption
**Physical table:** `OSUSR_72o_OnlineMembershipPaymentOption`  
**Description:** Records that hold information about online membership payment options  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 150 | YES | ('') |
| ONLINEMEMBERSHIPID | int |  | YES | (NULL) |
| PAYMENTSCHEDULETEMPLATEID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| INITIALPAYMENTOPTIONID | int |  | YES | (NULL) |
| RENEWALPAYMENTOPTIONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISONLINESALESACTIVE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## OnlineMembershipPaymentOptionKey
**Physical table:** `OSUSR_72o_OnlineMembershipPaymentOptionKey`  
**Description:** Records that hold information about online membership payment option keys  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| ONLINEMEMBERSHIPPAYMENTOPTIO | int |  | YES | (NULL) |
| KEY | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## OnlineMembershipProgram
**Physical table:** `OSUSR_72o_OnlineMembershipProgram`  
**Description:** Records that hold information about online membership programs  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| ONLINEMEMBERSHIPID | int |  | YES | (NULL) |
| ONLINEMEMBERSHIPLOCATIONID | int |  | YES | (NULL) |
| PROGRAMID | int |  | YES | (NULL) |
| ISONLINESALESACTIVE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## OnlineMembershipSale
**Physical table:** `OSUSR_72o_OnlineMembershipSale`  
**Description:** Record for a sale made through the Online Sales portal.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| INVOICEHEADERID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| ATHLETENAME | nvarchar | 50 | YES | ('') |
| LOCATIONID | int |  | YES | (NULL) |
| ONLINEMEMBERSHIPID | int |  | YES | (NULL) |
| CLASSID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HASBEENSAVED | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| LEADID | int |  | YES | (NULL) |
| EMAIL | nvarchar | 250 | YES | ('') |
| GENDERID | int |  | YES | (NULL) |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| ATHLETEFULLNAME | nvarchar | 50 | YES | ('') |
| ISMOBILE | bit |  | YES | ((0)) |
| ONLINEMEMBERSHIPPAYMENTOPTIO | int |  | YES | (NULL) |
| PHONE | nvarchar | 20 | YES | ('') |
| WILLPAYATGYM | bit |  | YES | ((0)) |
| REFERENCENUMBER | nvarchar | 50 | YES | ('') |
| SENTATTENDEDEMAIL | bit |  | YES | ((0)) |
| SENTFREETRIALEMAIL | bit |  | YES | ((0)) |
| PAYMENTMETHODID | int |  | YES | (NULL) |
| SENTFAILEDPAYMENTEMAIL | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DROPINID | bigint |  | YES | (NULL) |

## OnlineMembershipSaleFailedPaymentMessage
**Physical table:** `OSUSR_2o0_OnlineMembershipSaleFailedPaymentMessage`  
**Description:** Record for an error message that occurs when a membership was created but the payment failed in sale from Online Sales Portal.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| ONLINEMEMBERSHIPSALEID | int |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## OnlineMembershipType
**Physical table:** `OSUSR_72o_OnlineMembershipType`  
**Description:** Lookup table of online membership types  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| PLURALLABEL | nvarchar | 50 | YES | ('') |

## Order
**Physical table:** `OSUSR_2o0_Order`  
**Description:** used to track an order as it moves from creation to payment to fulfillment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ONLINEMEMBERSHIPSALEID | int |  | YES | (NULL) |
| STRIPEPAYMENTINTENTID | nvarchar | 50 | YES | ('') |
| STRIPECUSTOMERID | nvarchar | 50 | YES | ('') |
| AMOUNT | decimal |  | YES | ((0)) |
| CURRENCY | nvarchar | 3 | YES | ('') |
| ORDERSTATUSID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMEREMAIL | nvarchar | 250 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| STRIPECHARGEID | nvarchar | 50 | YES | ('') |
| SOURCE | nvarchar | 50 | YES | ('') |
| NOTES | nvarchar | 2000 | YES | ('') |
| ORDERATTRIBUTESJSON | nvarchar | -1 | YES | ('') |
| ORDERATTRIBUTESTYPE | nvarchar | 100 | YES | ('') |
| ORDERATTRIBUTESVERSION | int |  | YES | ((0)) |
| ONLINEMEMBERSHIPID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| DROPINID | bigint |  | YES | (NULL) |
| MEMBERPLANID | bigint |  | YES | ((0)) |
| CARTID | bigint |  | YES | ((0)) |
| ORDERTYPEID | int |  | YES | (NULL) |
| STRIPERECEIPTURL | nvarchar | 255 | YES | ('') |

## OrderFulfillmentJob
**Physical table:** `OSUSR_2o0_OrderFulfillmentJob4`  
**Description:** the BPT “work item” for an order.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ORDERID | bigint |  | YES | (NULL) |
| ATTEMPTS | int |  | YES | ((0)) |
| ORDERFULFILLMENTSTATUSID | int |  | YES | (NULL) |
| LASTERRORMESSAGE | nvarchar | 255 | YES | ('') |
| LASTERRORDETAILS | nvarchar | 2000 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| LASTRUNON | datetime |  | YES | ('1900-01-01 00:00:00') |
| NEXTRUNON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CURRENTSTEPCODE | nvarchar | 50 | YES | ('') |
| CURRENTSTEPLABEL | nvarchar | 255 | YES | ('') |

## OrderFulfillmentJobStatus
**Physical table:** `OSUSR_2o0_OrderFulfillmentStatus`  
**Description:** the possible statuses of order fulfillment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## OrderFulfillmentLog
**Physical table:** `OSUSR_2o0_OrderFulfillmentLog`  
**Description:** log of fulfillment attempts for an order  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ORDERID | bigint |  | YES | (NULL) |
| ATTEMPTNUMBER | int |  | YES | ((0)) |
| ORDERFULFILLMENTSTATUSID | int |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 255 | YES | ('') |
| ERRORDETAILS | nvarchar | 2000 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| JOBID | bigint |  | YES | (NULL) |
| STEPNAME | nvarchar | 100 | YES | ('') |
| STATUS | nvarchar | 50 | YES | ('') |
| MESSAGE | nvarchar | 255 | YES | ('') |

## OrderStatus
**Physical table:** `OSUSR_2o0_OrderStatus`  
**Description:** static lookup of possible order statuses  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## OrderType
**Physical table:** `OSUSR_2o0_OrderType`  
**Description:** Enumerates the types of orders to process (membership, free, POS)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## OrderUserMessage
**Physical table:** `OSUSR_2o0_OrderUserMessage`  
**Description:** Holds user-facing messages encountered during the purchase process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ORDERID | bigint |  | YES | (NULL) |
| SEVERITY | nvarchar | 50 | YES | ('') |
| CODE | nvarchar | 50 | YES | ('') |
| MESSAGETEXT | nvarchar | 255 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Request
**Physical table:** `OSUSR_2o0_OnlineSaleRequest`  
**Description:** Async requests related to online membership sales  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |
| ONLINESALEREQUESTTYPEID | int |  | YES | (NULL) |
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
| REQUESTTYPEID | int |  | YES | (NULL) |

## RequestType
**Physical table:** `OSUSR_2o0_OnlineSaleRequestType`  
**Description:** Possible request types for the Request table  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
