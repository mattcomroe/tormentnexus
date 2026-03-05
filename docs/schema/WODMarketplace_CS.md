# WODMarketplace_CS

## Tables

- [Partner](#partner)
- [PartnerProgram](#partnerprogram)
- [ProcessCopyWODS](#processcopywods)
- [ProcessCopyWODSSubscription](#processcopywodssubscription)
- [Subscription](#subscription)
- [SubscriptionError](#subscriptionerror)
- [SubscriptionProgram](#subscriptionprogram)
- [SubscriptionProgramLocation](#subscriptionprogramlocation)

## Partner
**Physical table:** `OSUSR_27V_PARTNER`  
**Description:** A partner represents a Customer that is responsible for creating WODs that will be copied into Subscriber's Gyms.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| WODSEARCHTAG | nvarchar | 50 | YES | ('') |
| PARTNERNOTES | nvarchar | 1500 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| NOTES | nvarchar | 1500 | YES | ('') |
| CUSTOMERID | bigint |  | YES | ((0)) |

## PartnerProgram
**Physical table:** `OSUSR_27V_PARTNERPROGRAM`  
**Description:** A program map that will determine where are partner is creating the WODs that will be copied.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PARTNERID | bigint |  | YES | (NULL) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## ProcessCopyWODS
**Physical table:** `OSUSR_27V_PROCESSCOPYWODS`  
**Description:** Contains logs regarding the asynchronous Copy WODs process based on subscriptions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TOTALSUBSCRIBERSTOPROCESS | int |  | YES | ((0)) |
| TOTALSUBSCRIBERSPROCESSED | int |  | YES | ((0)) |
| TOTALWODSTOCOPY | int |  | YES | ((0)) |
| TOTALWODSCOPIED | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATEFORCED | bit |  | YES | ((0)) |
| TOTALSUBSCRIPTIONSTOPROCESS | int |  | YES | ((0)) |
| TOTALSUBSCRIPTIONSPROCESSED | int |  | YES | ((0)) |
| ISAUTOMATIC | bit |  | YES | ((0)) |
| NOTIFICATIONID | nvarchar | 50 | YES | ('') |

## ProcessCopyWODSSubscription
**Physical table:** `OSUSR_27V_PROCESSCOPYWODSSUBSCRIBER`  
**Description:** Contains logs regarding the asynchronous Copy WODs process for each subscription.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SUBSCRIBERID | bigint |  | YES | (NULL) |
| PROCESSCOPYWODSID | bigint |  | YES | (NULL) |
| TOTALWODSTOCOPY | int |  | YES | ((0)) |
| TOTALWODSCOPIED | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HASERRORS | bit |  | YES | ((0)) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| SUBSCRIPTIONID | bigint |  | YES | (NULL) |

## Subscription
**Physical table:** `OSUSR_27V_SUBSCRIBER`  
**Description:** A Subscription represents a Customer that is able to receive WODs from a Partner.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| WODTAGS | nvarchar | 50 | YES | ('') |
| SUBSCRIBERNOTES | nvarchar | 1500 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| TRAYIOUSERID | nvarchar | 50 | YES | ('') |
| PARTNERID | bigint |  | YES | (NULL) |
| NOTES | nvarchar | 1500 | YES | ('') |
| CUSTOMERID | bigint |  | YES | ((0)) |

## SubscriptionError
**Physical table:** `OSUSR_27V_SUBSCRIBERERROR`  
**Description:** Errors that were reported during the CopyWODs migration.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SUBSCRIBERID | bigint |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| CREATEDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| SUBSCRIPTIONID | bigint |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PROCESSCOPYWODSID | bigint |  | YES | (NULL) |

## SubscriptionProgram
**Physical table:** `OSUSR_27V_SUBSCRIBERPROGRAM`  
**Description:** A Subscription program that allows a Gym receive WODs(Copied) from a Partner's program.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SUBSCRIBERID | bigint |  | YES | (NULL) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| PARTNERPROGRAMID | bigint |  | YES | (NULL) |
| SUBSCRIPTIONID | bigint |  | YES | (NULL) |

## SubscriptionProgramLocation
**Physical table:** `OSUSR_27V_SUBSCRIBERPROGRAMLOCATION`  
**Description:** The locations mapped to a Subscription program.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SUBSCRIBERPROGRAMID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| SUBSCRIPTIONPROGRAMID | bigint |  | YES | (NULL) |
| PARTNERID | bigint |  | YES | (NULL) |
