# Payroll_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [CustomerSettingPayroll](#customersettingpayroll)
- [PayRateProgramCoach](#payrateprogramcoach)
- [PayRateServiceProvider](#payrateserviceprovider)
- [PayRateUserEmployee](#payrateuseremployee)
- [PayRateUserEmployeeHistory](#payrateuseremployeehistory)
- [PayrollInterval](#payrollinterval)
- [PayrollPayPeriod](#payrollpayperiod)
- [PayrollPayPeriodNote](#payrollpayperiodnote)
- [PayrollPayPeriodUser](#payrollpayperioduser)
- [PayrollPayPeriodUserType](#payrollpayperiodusertype)
- [PayrollPosition](#payrollposition)
- [PayrollPositionClass](#payrollpositionclass)
- [PayrollPositionClassUser](#payrollpositionclassuser)
- [PayrollPositionClassUserStatus](#payrollpositionclassuserstatus)
- [PayrollPositionLocation](#payrollpositionlocation)
- [PayrollPositionLocationUser](#payrollpositionlocationuser)
- [PayrollPositionPayType](#payrollpositionpaytype)
- [PayrollPositionRecurringClass](#payrollpositionrecurringclass)
- [PayrollPositionRecurringClassUser](#payrollpositionrecurringclassuser)
- [PayrollPositionRole](#payrollpositionrole)
- [PayrollPositionType](#payrollpositiontype)
- [Request](#request)
- [RequestType](#requesttype)

## AsyncProcess
**Physical table:** `OSUSR_G2S_ASYNCPROCESS`  
**Description:** Auxiliar entity that contains all asynchronous processes, which will run through the Waivers_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerSettingPayroll
**Physical table:** `OSUSR_72O_TENANTSETTINGPAYROLL`  
**Description:** Contains information for customer payroll settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| USEPAYROLL | bit |  | YES | ((0)) |
| PAYROLLINTERVALID | int |  | YES | (NULL) |
| REPLYTOEMAILREMINDERUSERID | int |  | YES |  |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| WEEKLYPAYROLLDAYOFWEEKID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | NO | ((0)) |
| MONTHLYPAYROLLDAYOFMONTHID | int |  | YES | (NULL) |

## PayRateProgramCoach
**Physical table:** `OSUSR_G2S_PAYRATEPROGRAMCOACH`  
**Description:** Set in the Coach's Client Profile (DefaultPayRateId), and when adding/editing a Program (PayRateId). Holds the Customer's Coach default and Program default PayRates per Coach and Program.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PROGRAMID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| DEFAULTPAYRATEID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PayRateServiceProvider
**Physical table:** `OSUSR_G2S_PAYRATESERVICEPROVIDER`  
**Description:** Set on Provider's Client Profile (DefaultPayRateId), and when adding/editing a Service Duration (PayRateId). Holds the Customer's default PayRates per Provider, Service Duration and Location.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SERVICEDURATIONID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| DEFAULTPAYRATEID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PayRateUserEmployee
**Physical table:** `OSUSR_G2S_PAYRATEUSEREMPLOYEE`  
**Description:** Set on Employee's Client Profile. Holds the Administrative and Fixed PayRates per Employee.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISADMINISTRATIVEPAYENABLED | bit |  | YES | ((0)) |
| ADMINISTRATIVEPAYRATEID | bigint |  | YES | (NULL) |
| ISFIXEDPAYENABLED | bit |  | YES | ((0)) |
| FIXEDPAYRATE | decimal |  | YES | ((0)) |
| FIXEDPAYPERIODID | int |  | YES | (NULL) |
| FUTUREFIXEDPAY | decimal |  | YES | ((0)) |
| FUTUREFIXEDPAYEFFECTIVEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| FUTUREFIXEDPAYRATE | decimal |  | YES | ((0)) |
| FUTUREFIXEDPAYPERIODID | int |  | YES | (NULL) |

## PayRateUserEmployeeHistory
**Physical table:** `OSUSR_G2S_PAYRATEUSEREMPLOYEEHISTORY1`  
**Description:** Holds the history for Administrative, Fixed and Program/Service default PayRates per Employee.   History examples:  Administrative Pay: "Added $20/hour as default administrative pay rate" "Updated default administrative pay rate from $20/hour to $25/hour"  Fixed Pay: "Added fixed pay $50,000 per year; effective date 03/03/2026" "Updated fixed pay from $50,000 per year to $60,000 per year; effective date 03/03/2026"  Program Coach: "Added Crossfit $25 as default pay rate for Crossfit Program" "Updated default pay rate for Crossfit Program from Crossfit $25 to Crossfit $35"  Service Provider: "Added $50 Flat as default pay rate for Yoga (60min) - New Yoga York" "Updated default pay rate for Yoga (60min) - New Yoga York from $50 Flat to $60 Flat"  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| HISTORY | nvarchar | 250 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PayrollInterval
**Physical table:** `OSUSR_72O_PAYROLLINTERVAL`  
**Description:** Default payroll intervals that customer can use  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| SHORTLABEL | nvarchar | 50 | YES | ('') |

## PayrollPayPeriod
**Physical table:** `OSUSR_72O_PAYROLLPAYPERIOD`  
**Description:** Contains customer payroll pay period information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 200 | YES | ('') |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXPECTEDENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISOPEN | bit |  | YES | ((0)) |
| HISTORY | nvarchar | -1 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| PROCESSEDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| TOTALPAY | decimal |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PayrollPayPeriodNote
**Physical table:** `OSUSR_72O_PAYROLLPAYPERIODNOTE`  
**Description:** Contains note related to payroll pay period  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPAYPERIODID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| PAYROLLPOSITIONPAYTYPEID | int |  | YES | (NULL) |
| NOTES | nvarchar | 2000 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PayrollPayPeriodUser
**Physical table:** `OSUSR_72O_PAYROLLPAYPERIODUSER`  
**Description:** Contain information of each pay period job (classes, hourly, extra,...) of employees by customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPAYPERIODID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CLASSID | int |  | YES | (NULL) |
| PAYROLLPOSITIONID | int |  | YES | (NULL) |
| PAYRATE | decimal |  | YES | ((0)) |
| HISTORY | nvarchar | -1 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| LOCATIONID | int |  | YES | (NULL) |
| PAYROLLPOSITIONPAYTYPEID | int |  | YES | (NULL) |
| HOURSWORKED | decimal |  | YES | ((0)) |
| TOTALPAY | decimal |  | YES | ((0)) |
| DATEWORKED | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYROLLPOSITIONLOCATIONUSERI | int |  | YES | (NULL) |
| PAYROLLPAYPERIODUSERTYPEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| APPOINTMENTID | bigint |  | YES | (NULL) |
| ADMINISTRATIVEPAYRATEID | bigint |  | YES | (NULL) |

## PayrollPayPeriodUserType
**Physical table:** `OSUSR_72O_PAYROLLPAYPERIODUSERTYPE`  
**Description:** Contains type of PayrollPayPeriodUser, use to differentiate actions related to PayrollPayPeriodUser (e.g: employee sign-in, no show)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## PayrollPosition
**Physical table:** `OSUSR_72O_PAYROLLPOSITION`  
**Description:** Contains information of payroll positions by customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| PAYROLLPOSITIONTYPEID | int |  | YES | (NULL) |
| HISTORY | nvarchar | -1 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PayrollPositionClass
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONCLASS`  
**Description:** Contains info of payroll position associated with a class  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPOSITIONID | int |  | YES | (NULL) |
| CLASSID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISSYSTEMRECORD | bit |  | YES | ((0)) |
| PAYROLLPOSITIONRECURRINGCLAS | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PayrollPositionClassUser
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONCLASSUSER`  
**Description:** Contains info and status of on payroll user associated with a class  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPOSITIONID | int |  | YES | (NULL) |
| CLASSID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| STATUSID | int |  | YES | (NULL) |
| PAYROLLPAYPERIODUSERID | int |  | YES | (NULL) |
| ISPREASSIGNED | bit |  | YES | ((0)) |
| HISTORY | nvarchar | -1 | YES | ('') |
| STATUSUPDATEHISTORY | nvarchar | 2000 | YES | ('') |
| SIGNINGUID | nvarchar | 50 | YES | ('') |
| CANCELGUID | nvarchar | 50 | YES | ('') |
| PAYROLLPOSITIONCLASSID | int |  | YES | (NULL) |
| PAYROLLPOSITIONRECURRINGCLAS | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISPRIMARY | bit |  | YES | ((0)) |
| PAYRATEID | bigint |  | YES | (NULL) |

## PayrollPositionClassUserStatus
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONCLASSUSERSTATUS`  
**Description:** Status of payroll position user associated with a class  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ABBREVIATION | nvarchar | 3 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## PayrollPositionLocation
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONLOCATION`  
**Description:** Contain location and gym program that is related to payroll position by customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPOSITIONID | int |  | YES | (NULL) |
| PROGRAMID | int |  | YES | (NULL) |
| PAYRATE | decimal |  | YES | ((0)) |
| PAYROLLPOSITIONPAYTYPEID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| FUTUREPAYRATE | decimal |  | YES | ((0)) |
| FUTUREPAYRATEEFFECTIVEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| FUTUREPAYROLLPOSITIONPAYTYPE | int |  | YES | (NULL) |
| HISTORY | nvarchar | -1 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ISSYTEMRECORD | bit |  | YES | ((0)) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| ISSYSTEMRECORD | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PayrollPositionLocationUser
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONLOCATIONUSER`  
**Description:** Contains information of payroll position at location of user by customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPOSITIONID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| PROGRAMID | int |  | YES | (NULL) |
| PAYRATE | decimal |  | YES | ((0)) |
| PAYROLLPOSITIONPAYTYPEID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| HISTORY | nvarchar | -1 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| FUTUREPAYRATE | decimal |  | YES | ((0)) |
| FUTUREPAYRATEEFFECTIVEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| FUTUREPAYROLLPOSITIONPAYTYPE | int |  | YES | (NULL) |
| ISCUSTOMRATE | bit |  | YES | ((0)) |
| EFFECTIVEFROMDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| EFFECTIVETODATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| GYMPROGRAMID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PayrollPositionPayType
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONPAYTYPE`  
**Description:** Pay types for a payroll position  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## PayrollPositionRecurringClass
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONRECURRINGCLASS`  
**Description:** Contains info of payroll positions associated with recurring classes  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPOSITIONID | int |  | YES | (NULL) |
| RECURRINGCLASSID | int |  | YES | (NULL) |
| DAYOFWEEKID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISSYSTEMRECORD | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PayrollPositionRecurringClassUser
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONRECURRINGCLASSUSER`  
**Description:** Contains info of on payroll user associated with recurring class  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPOSITIONID | int |  | YES | (NULL) |
| RECURRINGCLASSID | int |  | YES | (NULL) |
| DAYOFWEEKID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYROLLPOSITIONRECURRINGCLAS | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISPRIMARY | bit |  | YES | ((0)) |
| PAYRATEID | bigint |  | YES | (NULL) |

## PayrollPositionRole
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONROLE`  
**Description:** Contain role that is associated to a payroll position  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PAYROLLPOSITIONID | int |  | YES | (NULL) |
| ROLEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PayrollPositionType
**Physical table:** `OSUSR_72O_PAYROLLPOSITIONTYPE`  
**Description:** Default payroll position type that all customers will have  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_G2S_REQUEST`  
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

## RequestType
**Physical table:** `OSUSR_G2S_REQUESTTYPE`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
