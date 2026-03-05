# Membership_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [BillingDay](#billingday)
- [BulkFile](#bulkfile)
- [CommitmentTimeUnit](#commitmenttimeunit)
- [ContractEnforcementType](#contractenforcementtype)
- [CustomerSettingMembership](#customersettingmembership)
- [MemberPlan](#memberplan)
- [MemberPlanAttendanceType](#memberplanattendancetype)
- [MemberPlanDiscount](#memberplandiscount)
- [MemberPlanHold](#memberplanhold)
- [MemberPlanHoldType](#memberplanholdtype)
- [MemberPlanInvoiceDetail](#memberplaninvoicedetail)
- [MemberPlanLocation](#memberplanlocation)
- [MemberPlanProgram](#memberplanprogram)
- [MemberPlanTemplate](#memberplantemplate)
- [MemberPlanTemplateLocation](#memberplantemplatelocation)
- [MemberPlanTemplatePaymentScheduleTemplate](#memberplantemplatepaymentscheduletemplate)
- [MemberPlanTemplateProgram](#memberplantemplateprogram)
- [MemberPlanType](#memberplantype)
- [MembershipContractStatus](#membershipcontractstatus)
- [MembershipContractTemplate](#membershipcontracttemplate)
- [PaymentOption](#paymentoption)
- [PaymentOptionType](#paymentoptiontype)
- [PaymentSchedule](#paymentschedule)
- [PaymentScheduleTemplate](#paymentscheduletemplate)
- [PaymentScheduleTemplateLocationTaxRate](#paymentscheduletemplatelocationtaxrate)
- [PriceAdjustmentType](#priceadjustmenttype)
- [Request](#request)
- [Request_MassUpdateMemberships](#request-massupdatememberships)
- [Request_MassUpdateMemberships_File](#request-massupdatememberships-file)
- [RequestType](#requesttype)
- [SessionEnforcementType](#sessionenforcementtype)
- [SignedContractToSend](#signedcontracttosend)
- [UserMembershipContract](#usermembershipcontract)
- [UserMembershipContractLink](#usermembershipcontractlink)
- [UserMembershipContractMembershipInfo](#usermembershipcontractmembershipinfo)
- [UserMembershipContractPersonalInfo](#usermembershipcontractpersonalinfo)

## AsyncProcess
**Physical table:** `OSUSR_JUW_ASYNCPROCESS`  
**Description:** Auxiliar entity that contains all membership asynchronous processes, which will run through the Membership_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## BillingDay
**Physical table:** `OSUSR_72O_BILLINGDAY`  
**Description:** Contains all possible days a Membership can be billed on  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## BulkFile
**Physical table:** `OSUSR_JUW_BULKFILE`  
**Description:** Zip file containing several files to be sent to the user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| FILEKEY | nvarchar | 100 | YES | ('') |
| FILENAME | nvarchar | 100 | YES | ('') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| REQUESTID | bigint |  | YES | (NULL) |

## CommitmentTimeUnit
**Physical table:** `OSUSR_72O_COMMITMENTTIMEUNIT`  
**Description:** All possible commitment time units for a Membership  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SINGULARLABEL | nvarchar | 50 | YES | ('') |
| PLURALLABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| PAYMENTINTERVALLABEL | nvarchar | 50 | YES | ('') |

## ContractEnforcementType
**Physical table:** `OSUSR_72O_CONTRACTENFORCEMENTTYPE`  
**Description:** Contract enforcement configurations that can be applied to restrict or allow sign-ins/reservations.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 100 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CustomerSettingMembership
**Physical table:** `OSUSR_72O_TENANTSETTINGMEMBERSHIP`  
**Description:** Customer settings regarding memberships (enforcement options, reservation restrictions, etc.)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ENFORCEMEMBERSHIPLIMITS | bit |  | YES | ((0)) |
| CONTRACTENFORCEMENTTYPEID | int |  | YES | (NULL) |
| SESSIONENFORCEMENTTYPEID | int |  | YES | (NULL) |
| COUNTLATECANCELLATIONS | bit |  | YES | ((0)) |
| COUNTNOSHOWRESERVATIONS | bit |  | YES | ((0)) |
| ATHLETEDEFAULTLOCATIONID | int |  | YES | (NULL) |
| DEFAULTCONVERTEDATHLETESTATU | int |  | YES | (NULL) |
| WELCOMEEMAIL | nvarchar | -1 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| ENABLEONLINEMEMBERSHIPSALES | bit |  | YES | ((0)) |
| RESTRICTRESERVATIONS | bit |  | YES | ((0)) |
| RESTRICTRESERVATIONSNUMBER | int |  | YES | ((0)) |
| ATHLETEDEFAULTGYMPROGRAMID | int |  | YES | (NULL) |
| ENABLECONTRACTENFORCEMENT | bit |  | YES | ((0)) |
| ENABLEWAIVERENFORCEMENT | bit |  | YES | ((0)) |
| MEMBERBILLINGDAYID | int |  | YES | (NULL) |
| SHOWALLCLASSES | bit |  | YES | ((0)) |
| SHOWALLCLASSESUPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | NO | ((0)) |

## MemberPlan
**Physical table:** `OSUSR_72O_MEMBERPLAN`  
**Description:** Member Plans associated to a user.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| MEMBERPLANTEMPLATEID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| NAME | nvarchar | 250 | YES | ('') |
| MEMBERSHIPPLANTYPEID | int |  | YES | (NULL) |
| MEMBERSHIPATTENDANCETYPE | int |  | YES | (NULL) |
| ATTENDANCELIMITATIONTYPE | int |  | YES | (NULL) |
| ATTENDANCELIMITATION | int |  | YES | ((0)) |
| NUMBEROFSESSIONS | int |  | YES | ((0)) |
| PAYMENTSCHEDULEID | int |  | YES | (NULL) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXPIRES | bit |  | YES | ((0)) |
| EXPIRATIONLENGTH | int |  | YES | ((0)) |
| EXPIRATIONTYPE | int |  | YES | (NULL) |
| INCOMECATEGORY | int |  | YES | (NULL) |
| ISCONFIGURATIONCOMPLETE | bit |  | YES | ((0)) |
| ISMEMBERPLANACTIVE | bit |  | YES | ((0)) |
| HASBEENRENEWED | bit |  | YES | ((0)) |
| RENEWEDFROMMEMBERPLAN | int |  | YES | (NULL) |
| EXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| REVENUECATEGORYPICKLISTVALUE | int |  | YES | (NULL) |
| TAXRATEID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| USERMEMBERSHIPCONTRACTID | int |  | YES | (NULL) |
| SESSIONSALREADYUSED | int |  | YES | ((0)) |
| LEADID | int |  | YES | (NULL) |
| ORIGINALEXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| AUTORENEWEMAILSENT | bit |  | YES | ((0)) |
| MEMBERSHIPEXPIRINGEMAILSENT | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ABSORBFEES | bit |  | YES | ((0)) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ATTENDANCELIMITFREQUENCY | int |  | YES | ((1)) |
| SCHEDULEDDEACTIVATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| INITIALSESSIONSALREADYUSED | int |  | YES | ((0)) |
| ISCANCELSESSIONSONDEACTDATE | bit |  | YES | ((0)) |
| ALLOWROLLOVER | bit |  | YES | ((0)) |
| ROLLOVERSESSIONS | int |  | YES | ((0)) |
| MAXTOTALSESSIONS | int |  | YES | ((0)) |

## MemberPlanAttendanceType
**Physical table:** `OSUSR_72O_MEMBERPLANATTENDANCETYPE`  
**Description:** The attendace type that a Membership can have. Used to indicate if the Membership is Limited or Unlimited  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## MemberPlanDiscount
**Physical table:** `OSUSR_72O_MEMBERPLANDISCOUNT`  
**Description:** Entity to map the relation between memberships and the discounts (including promo codes) applied to it.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| MEMBERPLANID | int |  | YES | (NULL) |
| DISCOUNTID | int |  | YES | (NULL) |
| DISCOUNTTYPEID | int |  | YES | (NULL) |
| DISCOUNTPERCENTAGE | decimal |  | YES | ((0)) |
| DISCOUNTFLATAMOUNT | decimal |  | YES | ((0)) |
| APPLIESTOSETUPFEE | bit |  | YES | ((0)) |
| APPLIESTORENEWAL | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| APPLIESTOINITIAL | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MemberPlanHold
**Physical table:** `OSUSR_72O_MEMBERPLANHOLD`  
**Description:** Data for when a Membership is put on hold  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| MEMBERPLANID | int |  | YES | (NULL) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HOLDLENGTH | int |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| MEMBERPLANHOLDTYPEID | int |  | YES | (NULL) |

## MemberPlanHoldType
**Physical table:** `OSUSR_5K0_MEMBERPLANHOLDTYPE`  
**Description:** Defines the possible Values for a Picklist to be used in dropdowns  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## MemberPlanInvoiceDetail
**Physical table:** `OSUSR_JUW_MEMBERPLANINVOICEDETAIL`  
**Description:** Creates a relationship table between MemberPlan and Invoices.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| INVOICEDETAILID | int |  | NO |  |
| MEMBERPLANID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MemberPlanLocation
**Physical table:** `OSUSR_JUW_MEMBERPLANLOCATION`  
**Description:** Determines which business locations a member plan applies to.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| MEMBERPLANID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MemberPlanProgram
**Physical table:** `OSUSR_72O_MEMBERPLANPROGRAM`  
**Description:** Determines which programs a member plan applies to.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| MEMBERPLANID | int |  | YES | (NULL) |
| PROGRAMID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| GYMPROGRAMID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MemberPlanTemplate
**Physical table:** `OSUSR_72O_MEMBERPLANTEMPLATE`  
**Description:** Determines which programs a member plan template applies to.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| MEMBERSHIPPLANNAME | nvarchar | 250 | YES | ('') |
| MEMBERSHIPPLANTYPEID | int |  | YES | (NULL) |
| MEMBERSHIPATTENDANCETYPE | int |  | YES | (NULL) |
| ATTENDANCELIMITATIONTYPE | int |  | YES | (NULL) |
| ATTENDANCELIMITATION | int |  | YES | ((0)) |
| NUMBEROFSESSIONS | int |  | YES | ((0)) |
| LASTMODIFIEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXPIRES | bit |  | YES | ((0)) |
| EXPIRATIONLENGTH | int |  | YES | ((0)) |
| EXPIRATIONTYPE | int |  | YES | (NULL) |
| INCOMECATEGORY | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| REVENUECATEGORYPICKLISTVALUE | int |  | YES | (NULL) |
| TAXRATEID | int |  | YES | (NULL) |
| HASBEENMIGRATED | bit |  | YES | ((0)) |
| ISCONVERSIONEXCEPTION | bit |  | YES | ((0)) |
| EXCEPTIONDETAILS | nvarchar | 2000 | YES | ('') |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| MEMBERSHIPCONTRACTTEMPLATEID | int |  | YES | (NULL) |
| ISEDITABLE | bit |  | YES | ((0)) |
| CONFIRMATIONPAGETEXT | nvarchar | -1 | YES | ('') |
| AUTOMATEDEMAILID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ATTENDANCELIMITFREQUENCY | int |  | YES | ((1)) |
| ALLOWROLLOVER | bit |  | YES | ((0)) |
| MAXTOTALSESSIONS | int |  | YES | ((0)) |

## MemberPlanTemplateLocation
**Physical table:** `OSUSR_JUW_MEMBERPLANTEMPLATELOCATION`  
**Description:** Determines which business locations a member plan template applies to.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| MEMBERPLANTEMPLATEID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MemberPlanTemplatePaymentScheduleTemplate
**Physical table:** `OSUSR_72O_MEMBERPLANTEMPLATEPAYMENTSCHEDULETEMPLATE`  
**Description:** Connects PaymentScheduleTemplates with MemberPlanTemplates  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| MEMBERPLANTEMPLATEID | int |  | YES | (NULL) |
| PAYMENTSCHEDULETEMPLATEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MemberPlanTemplateProgram
**Physical table:** `OSUSR_72O_MEMBERPLANTEMPLATEPROGRAM`  
**Description:** Connects a MemberPlanTemplate with a GymProgram  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| MEMBERPLANTEMPLATEID | int |  | YES | (NULL) |
| PROGRAMID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| GYMPROGRAMID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MemberPlanType
**Physical table:** `OSUSR_72O_MEMBERPLANTYPE`  
**Description:** Static entity with the available member plan types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## MembershipContractStatus
**Physical table:** `OSUSR_JUW_MEMBERSHIPCONTRACTSTATUS`  
**Description:** Possible statuses that a Membership Contract can have.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## MembershipContractTemplate
**Physical table:** `OSUSR_JUW_MEMBERSHIPCONTRACTTEMPLATE`  
**Description:** Data for a contract template to be used for Memberships  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| MEMBERSHIPPOLICY | nvarchar | -1 | YES | ('') |
| EMAILTEMPLATE | nvarchar | -1 | YES | ('') |
| ISPHONENUMBERREQUIRED | bit |  | YES | ((0)) |
| COLLECTPAYMENTINFORMATION | bit |  | YES | ((0)) |
| MEMBERSHIPCONTRACTSTATUSID | int |  | YES | (NULL) |
| PARENTMEMBERSHIPCONTRACT | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| VERSION | decimal |  | YES | ((0)) |
| ISCURRENT | bit |  | YES | ((0)) |
| ISACITVE | bit |  | YES | ((0)) |
| EMAILSUBJECT | nvarchar | 500 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISAPPLYTOFUTUREMEMBERSHIPS | bit |  | YES | ((0)) |

## PaymentOption
**Physical table:** `OSUSR_72O_PAYMENTOPTION`  
**Description:** Data that defines the payment details for both Memberships and Membership Templates  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYMENTOPTIONTYPEID | int |  | YES | (NULL) |
| PREDISCOUNTSETUPFEE | decimal |  | YES | ((0)) |
| PREDISCOUNTTOTALSETUPFEE | decimal |  | YES | ((0)) |
| SETUPFEE | decimal |  | YES | ((0)) |
| TOTALSETUPFEE | decimal |  | YES | ((0)) |
| PREDISCOUNTFEE | decimal |  | YES | ((0)) |
| TOTALFEE | decimal |  | YES | ((0)) |
| PREDISCOUNTFIRSTMONTHFEE | decimal |  | YES | ((0)) |
| FIRSTMONTHSUBTOTAL | decimal |  | YES | ((0)) |
| MONTHLYSUBTOTAL | decimal |  | YES | ((0)) |
| PREDISCOUNTSUBTOTAL | decimal |  | YES | ((0)) |
| SUBTOTAL | decimal |  | YES | ((0)) |
| TOTALDISCOUNT | decimal |  | YES | ((0)) |
| FIRSTMONTHFEEDISCOUNT | decimal |  | YES | ((0)) |
| MONTHLYFEEDISCOUNT | decimal |  | YES | ((0)) |
| PREDISCOUNTTAX | decimal |  | YES | ((0)) |
| TOTALTAX | decimal |  | YES | ((0)) |
| PREDISCOUNTSETUPTAX | decimal |  | YES | ((0)) |
| SETUPTAX | decimal |  | YES | ((0)) |
| PREDISCOUNTFIRSTMONTHTAX | decimal |  | YES | ((0)) |
| FIRSTMONTHTAX | decimal |  | YES | ((0)) |
| MONTHLYTAX | decimal |  | YES | ((0)) |
| PREDISCOUNTTOTAL | decimal |  | YES | ((0)) |
| TOTAL | decimal |  | YES | ((0)) |
| FIRSTMONTHTOTAL | decimal |  | YES | ((0)) |
| MONTHLYTOTAL | decimal |  | YES | ((0)) |
| ISFIRSTMONTHPRORATED | bit |  | YES | ((0)) |
| PRORATERATE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SETUPFEEDISCOUNT | decimal |  | YES | ((0)) |
| PREDISCOUNTMONTHLYFEE | decimal |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| TOTALADMINFEES | decimal |  | YES | ((0)) |
| SETUPADMINFEES | decimal |  | YES | ((0)) |
| FIRSTMONTHADMINFEES | decimal |  | YES | ((0)) |
| MONTHLYADMINFEES | decimal |  | YES | ((0)) |
| PREDISCOUNTADMINFEES | decimal |  | YES | ((0)) |

## PaymentOptionType
**Physical table:** `OSUSR_JUW_PAYMENTOPTIONTYPE`  
**Description:** The types of Payment Options. Indicates the interval in which the payment option is paid  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## PaymentSchedule
**Physical table:** `OSUSR_72O_PAYMENTSCHEDULE`  
**Description:** Data for the Memberships Payment Plan  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYMENTSCHEDULETEMPLATE | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| ISFORTENANT | bit |  | YES | ((0)) |
| NAME | nvarchar | 250 | YES | ('') |
| INITIALCOMMITMENTLENGTH | int |  | YES | ((0)) |
| INITIALCOMMITMENTTIMEUNITID | int |  | YES | (NULL) |
| RENEWALCOMMITMENTLENGTH | int |  | YES | ((0)) |
| RENEWALCOMMITMENTTIMEUNITID | int |  | YES | (NULL) |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISTAXABLE | bit |  | YES | ((0)) |
| PAYMENTOPTIONID | int |  | YES | (NULL) |
| AUTORENEWPAYMENTOPTIONID | int |  | YES | (NULL) |
| ISAUTORENEW | bit |  | YES | ((0)) |
| PAYMENTOPTIONTYPEID | int |  | YES | (NULL) |
| AUTORENEWPAYMENTOPTIONTYPEID | int |  | YES | (NULL) |
| BILLINGDAYID | int |  | YES | (NULL) |
| AUTORENEWPAUSEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| AUTORENEWUNPAUSEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| AUTORENEWPAUSEDEACTIVATEUSER | bit |  | YES | ((0)) |
| HASUSERBEENDEACTIVATED | bit |  | YES | ((0)) |
| PAYMENTINTERVALLENGTH | int |  | YES | ((0)) |
| PAYMENTINTERVALTIMEUNITID | int |  | YES | (NULL) |
| RENEWALPAYMENTINTERVALLENGTH | int |  | YES | ((0)) |
| RENEWALPAYMENTINTERVALTIMEUN | int |  | YES | (NULL) |
| ORIGINALBILLINGDAYID | int |  | YES | (NULL) |
| ISSTOPSESSIONAUTORENEW | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISSTOPAUTORENEW | bit |  | YES | ((0)) |

## PaymentScheduleTemplate
**Physical table:** `OSUSR_72O_PAYMENTSCHEDULETEMPLATE`  
**Description:** Holds default payment information for a membership's payment schedule  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 250 | YES | ('') |
| INITIALCOMMITMENTLENGTH | int |  | YES | ((0)) |
| INITIALCOMMITMENTTIMEUNITID | int |  | YES | (NULL) |
| RENEWALCOMMITMENTLENGTH | int |  | YES | ((0)) |
| RENEWALCOMMITMENTTIMEUNITID | int |  | YES | (NULL) |
| ISTAXABLE | bit |  | YES | ((0)) |
| ISAUTORENEW | bit |  | YES | ((0)) |
| ONETIMEPAYMENTOPTIONID | int |  | YES | (NULL) |
| MONTHLYPAYMENTOPTIONID | int |  | YES | (NULL) |
| AUTORENEWMONTHLYPAYMENTOPTIO | int |  | YES | (NULL) |
| AUTORENEWONETIMEPAYMENTOPTIO | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYMENTINTERVALLENGTH | int |  | YES | ((0)) |
| PAYMENTINTERVALTIMEUNITID | int |  | YES | (NULL) |
| RENEWALPAYMENTINTERVALLENGTH | int |  | YES | ((0)) |
| RENEWALPAYMENTINTERVALTIMEUN | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ONLINESALESDISPLAYORDER | int |  | YES | ((0)) |

## PaymentScheduleTemplateLocationTaxRate
**Physical table:** `OSUSR_72O_PAYMENTSCHEDULETEMPLATELOCATIONTAXRATE`  
**Description:** Holds the Location/Tax rate relationships on a Payment Schedule Template  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYMENTSCHEDULEID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| TAXRATEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYMENTSCHEDULETEMPLATEID | int |  | YES | (NULL) |
| ISAVAILABLEONLINESALES | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PriceAdjustmentType
**Physical table:** `OSUSR_5K0_PRICEADJUSTMENTTYPE`  
**Description:** Contains types of price adjustments  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_5K0_REQUEST2`  
**Description:** Async requests related to memberships  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |
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

## Request_MassUpdateMemberships
**Physical table:** `OSUSR_5K0_REQUEST_MASSUPDATEMEMBERSHIPS`  
**Description:** Entity to keep evidences of mass update requests (memberships updated).  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUESTID | bigint |  | YES | (NULL) |
| MEMBERSHIPID | int |  | YES | (NULL) |
| PAYMENTSCHEDULEID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| INITIALCOMMITMENTPRICE | bit |  | YES | ((0)) |
| PAYMENTOPTIONTYPEID | int |  | YES | (NULL) |
| OLDMEMBFEEPRICE | decimal |  | YES | ((0)) |
| PAYMENTOPTION_DISCOUNT | decimal |  | YES | ((0)) |
| NEWMEMBFEEPRICE | decimal |  | YES | ((0)) |
| RENEWCOMMITMENTPRICE | bit |  | YES | ((0)) |
| RENEWALPAYMENTOPTIONTYPEID | int |  | YES | (NULL) |
| OLDRENEWALMEMBFEEPRICE | decimal |  | YES | ((0)) |
| AUTORENEWPAYMENTOPTION_DISCO | decimal |  | YES | ((0)) |
| NEWRENEWALMEMBFEEPRICE | decimal |  | YES | ((0)) |
| USERMEMBERSHIPCONTRACTID | int |  | YES | (NULL) |
| RESIGN | bit |  | YES | ((0)) |
| NRVOIDEDINVOICES | int |  | YES | ((0)) |
| NRGENERATEDINVOICES | int |  | YES | ((0)) |
| WASCONTRACTEMAILSENT | bit |  | YES | ((0)) |
| WASUPDATED | bit |  | YES | ((0)) |
| WASERROR | bit |  | YES | ((0)) |
| NOTES | nvarchar | -1 | YES | ('') |

## Request_MassUpdateMemberships_File
**Physical table:** `OSUSR_5K0_REQUEST_MASSUPDATEMEMBERSHIPS_FILE`  
**Description:** When the request type is MassUpdateMemberships, it saves a temporary excel file in this table, which will be extracted into Request_MassUpdateMemberships entity, and then it can be deleted  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| REQUESTID | bigint |  | NO |  |
| FILE | varbinary | -1 | YES | (NULL) |

## RequestType
**Physical table:** `OSUSR_5K0_REQUESTTYPE2`  
**Description:** Possible request types for the Request table  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## SessionEnforcementType
**Physical table:** `OSUSR_72O_SESSIONENFORCEMENTTYPE`  
**Description:** The enforcement types for session plans  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 100 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## SignedContractToSend
**Physical table:** `OSUSR_JUW_SIGNEDCONTRACTTOSEND`  
**Description:** Signed Contract to send  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SENDBYEMAILBULKID | bigint |  | YES | (NULL) |
| USERMEMBERSHIPCONTRACTID | int |  | YES | (NULL) |
| ISPROCESSED | bit |  | YES | ((0)) |
| ISERROR | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| REQUESTID | bigint |  | YES | (NULL) |

## UserMembershipContract
**Physical table:** `OSUSR_JUW_USERMEMBERSHIPCONTRACT`  
**Description:** The membership contract details.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| MEMBERSHIPCONTRACTTEMPLATEID | int |  | YES | (NULL) |
| CLOUDINARYFILEID | int |  | YES | (NULL) |
| FILESTORAGEID | int |  | YES | (NULL) |
| PARENTGUARDIANFULLNAME | nvarchar | 50 | YES | ('') |
| USERSIGNATURE | varbinary | -1 | YES | (NULL) |
| SIGNEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| INITIALS | nvarchar | 5 | YES | ('') |
| UNIQUEKEY | nvarchar | 50 | YES | ('') |
| ISUPLOADED | bit |  | YES | ((0)) |
| MEMBERPLANID | int |  | YES | (NULL) |
| HASAGREEDTOELECTRONICRECORDS | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| EXTERNALIMAGEID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## UserMembershipContractLink
**Physical table:** `OSUSR_5K0_USERMEMBERSHIPCONTRACTLINK`  
**Description:** Entity to hold anonymous-accessible links to sign contract.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LINKTOKEN | nvarchar | 100 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| USERMEMBERSHIPCONTRACTID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CREATEDAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | (CONVERT([datetime],'1900-01-01 00:00:00',(120))) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## UserMembershipContractMembershipInfo
**Physical table:** `OSUSR_JUW_USERMEMBERSHIPCONTRACTMEMBERSHIPINFO`  
**Description:** Details of the membership for which the contract was signed. This is a static copy of the membership information to be shown on the contract. This has a one-to-one relationship to the UserMembershipContract record.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| USERMEMBERSHIPCONTRACTID | int |  | NO |  |
| MEMBERSHIPNAME | nvarchar | 250 | YES | ('') |
| MEMBERSHIPPLANTYPEID | int |  | YES | (NULL) |
| NUMBEROFSESSIONS | int |  | YES | ((0)) |
| ATTENDANCELIMIT | nvarchar | 50 | YES | ('') |
| PROGRAMS | nvarchar | -1 | YES | ('') |
| SERVICENAME | nvarchar | 250 | YES | ('') |
| AUTORENEW | bit |  | YES | ((0)) |
| LOCATIONS | nvarchar | -1 | YES | ('') |
| DISCOUNTS | nvarchar | -1 | YES | ('') |
| BILLEDON | nvarchar | 250 | YES | ('') |
| INITIALCOMMITMENT | nvarchar | 50 | YES | ('') |
| INITIALPAYMENTOPTION | nvarchar | 100 | YES | ('') |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXPIRATION | nvarchar | 50 | YES | ('') |
| EXPIRATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| SETUPCOST | nvarchar | 50 | YES | ('') |
| SETUPTAX | nvarchar | 50 | YES | ('') |
| COMMITMENTCOST | nvarchar | 250 | YES | ('') |
| COMMITMENTTAX | nvarchar | 50 | YES | ('') |
| COMMITMENTTOTAL | nvarchar | 250 | YES | ('') |
| RENEWALCOMMITMENT | nvarchar | 50 | YES | ('') |
| RENEWALPAYMENTOPTION | nvarchar | 100 | YES | ('') |
| RENEWALCOST | nvarchar | 250 | YES | ('') |
| RENEWALTAX | nvarchar | 50 | YES | ('') |
| RENEWALTOTAL | nvarchar | 250 | YES | ('') |
| INITIALPAYMENT | nvarchar | 250 | YES | ('') |
| RENEWALPAYMENT | nvarchar | 250 | YES | ('') |
| RENEWALBILLEDON | nvarchar | 250 | YES | ('') |
| ISSHOWLABELTOTALPAYMENT | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| COMMITMENTADMINFEES | nvarchar | 50 | YES | ('') |
| RENEWALADMINFEES | nvarchar | 50 | YES | ('') |
| SETUPADMINFEES | nvarchar | 50 | YES | ('') |

## UserMembershipContractPersonalInfo
**Physical table:** `OSUSR_JUW_USERMEMBERSHIPCONTRACTPERSONALINFO`  
**Description:** The user's personal details provided with the signed contract.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERMEMBERSHIPCONTRACTID | int |  | YES | (NULL) |
| FULLNAME | nvarchar | 256 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| GENDERID | int |  | YES | (NULL) |
| STREETADDRESS | nvarchar | 200 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| PROVINCE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| DATEOFBIRTH | datetime |  | YES | ('1900-01-01 00:00:00') |
| PHONE | nvarchar | 20 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
