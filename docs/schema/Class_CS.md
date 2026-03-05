# Class_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [Class](#class)
- [Class_CancelDeleted](#class-canceldeleted)
- [ClassCountDisplayType](#classcountdisplaytype)
- [ClassDropInPricing](#classdropinpricing)
- [ClassEmailStatus](#classemailstatus)
- [ClassGoogleCalendar](#classgooglecalendar)
- [ClassIntegrationAvailability](#classintegrationavailability)
- [ClassLateCancellationSetting](#classlatecancellationsetting)
- [ClassNoShowSetting](#classnoshowsetting)
- [ClassOnlineSalesSetting](#classonlinesalessetting)
- [ClassRepeatType](#classrepeattype)
- [ClassReservation](#classreservation)
- [ClassReservationPenalty](#classreservationpenalty)
- [ClassReservationSetting](#classreservationsetting)
- [ClassReservationSource](#classreservationsource)
- [ClassReservationStatus](#classreservationstatus)
- [ClassSignInSetting](#classsigninsetting)
- [ClassStat](#classstat)
- [ClassStatType](#classstattype)
- [ClassWarningStatus](#classwarningstatus)
- [CustomerSettingClassPolicy](#customersettingclasspolicy)
- [RecurringClass](#recurringclass)
- [RecurringClassDropInPricing](#recurringclassdropinpricing)
- [RecurringClassEndType](#recurringclassendtype)
- [RecurringClassIntegrationAvailability](#recurringclassintegrationavailability)
- [RecurringClassLateCancellationSetting](#recurringclasslatecancellationsetting)
- [RecurringClassNoShowSetting](#recurringclassnoshowsetting)
- [RecurringClassOnlineSalesSetting](#recurringclassonlinesalessetting)
- [RecurringClassRepeatType](#recurringclassrepeattype)
- [RecurringClassReservation](#recurringclassreservation)
- [RecurringClassReservationEmailItem](#recurringclassreservationemailitem)
- [RecurringClassReservationStatus](#recurringclassreservationstatus)
- [RecurringClassSignInSetting](#recurringclasssigninsetting)
- [RejectedSignInLog](#rejectedsigninlog)
- [Request](#request)
- [RequestType](#requesttype)
- [TimerMissingAthleteEmailControl](#timermissingathleteemailcontrol)
- [WaitlistType](#waitlisttype)

## AsyncProcess
**Physical table:** `OSUSR_tr2_AsyncProcess`  
**Description:** Asynchronous process data  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Class
**Physical table:** `OSUSR_72o_Class`  
**Description:** Table that will store Class relative information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| LOCATIONID | int |  | YES | (NULL) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLASSLIMIT | int |  | YES | ((0)) |
| RECURRINGCLASSID | int |  | YES | (NULL) |
| CALENDARCOLOR | nvarchar | 6 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ALLOWWAITLIST | bit |  | YES | ((0)) |
| RESERVED | int |  | YES | ((0)) |
| SIGNEDIN | int |  | YES | ((0)) |
| DROPIN | int |  | YES | ((0)) |
| WAITLISTED | int |  | YES | ((0)) |
| AVAILABLE | int |  | YES | ((0)) |
| CANCELLED | int |  | YES | ((0)) |
| PERCENTFILLED | int |  | YES | ((0)) |
| ISFULL | bit |  | YES | ((0)) |
| NOSHOW | int |  | YES | ((0)) |
| CLASSWARNINGSTATUSID | int |  | YES | (NULL) |
| WARNING | nvarchar | 500 | YES | ('') |
| ISWARNINGIGNORED | bit |  | YES | ((0)) |
| ISCHANGED | bit |  | YES | ((0)) |
| CHANGELOG | nvarchar | -1 | YES | ('') |
| STARTTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISMARKEDFORREMOVAL | bit |  | YES | ((0)) |
| COUNTTOWARDSATTENDANCELIMITS | bit |  | YES | ((0)) |
| RESERVATIONOPEN | int |  | YES | ((0)) |
| RESERVATIONOPENTIMEFORMAT | int |  | YES | (NULL) |
| RESERVATIONCLOSE | int |  | YES | ((0)) |
| RESERVATIONCLOSETIMEFORMAT | int |  | YES | (NULL) |
| CANCELLATIONTIME | int |  | YES | ((0)) |
| CANCELLATIONTIMETIMEFORMAT | int |  | YES | (NULL) |
| CANCELCLASSIFNORESERVATIONS | bit |  | YES | ((0)) |
| ISCANCELLED | bit |  | YES | ((0)) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| RESERVATIONCLOSEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISDROPINONLINE | bit |  | YES | ((0)) |
| ISFREETRIALONLINE | bit |  | YES | ((0)) |
| ISNOSHOWWARNINGCOMPLETED | bit |  | YES | ((0)) |
| ISNOSHOWCOMPLETED | bit |  | YES | ((0)) |
| STARTDATETIMESERVER | datetime |  | YES | ('1900-01-01 00:00:00') |
| STARTDATESERVER | datetime |  | YES | ('1900-01-01 00:00:00') |
| STARTTIMESERVER | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIMESERVER | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATESERVER | datetime |  | YES | ('1900-01-01 00:00:00') |
| RESERVATIONCLOSEDATETIMESERV | datetime |  | YES | ('1900-01-01 00:00:00') |
| CANCELCLASSTIME | int |  | YES | ((0)) |
| CANCELCLASSTIMEFORMAT | int |  | YES | (NULL) |
| CANCELCLOSEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CANCELCLASSDATETIMESERVER | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISDELETED | bit |  | YES | ((0)) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| WAITLISTTYPEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DESCRIPTION | nvarchar | 1000 | YES | ('') |
| FREETRIALLIMIT | int |  | YES | ((0)) |
| HASFREETRIALLIMIT | bit |  | YES | ((0)) |
| ISFREETRIALFULL | bit |  | YES | ((0)) |
| CANCELCLASSNUMBERRESERVATION | int |  | YES | ((0)) |
| RESERVATIONSCLOSETIMERELATIO | int |  | YES | (NULL) |
| RESERVATIONSCLOSETIMEPOINT | int |  | YES | (NULL) |
| ISCLASSPASSENABLED | bit |  | YES |  |

## Class_CancelDeleted
**Physical table:** `OSUSR_oc9_Class_CancelDeleted`  
**Description:** table that will handle the records when we delete or cancel a class via calendar. Each record is for a admin or coach for each class  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| AUTOMATEDEMAILTEMPLATEID | int |  | YES | (NULL) |
| CLASSSTARTTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLASSSTARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLASSNAME | nvarchar | 100 | YES | ('') |
| CLASSRESERVATIONCLOSEDATETIM | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLASSCANCELCLOSEDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| PROGRAMNAME | nvarchar | 50 | YES | ('') |
| USERINPAYROLL | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| AUTOMATEDEMAILSUBEMAILID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ClassCountDisplayType
**Physical table:** `OSUSR_tr2_ClassCountDisplayType`  
**Description:** Determines the behavior when displaying class reservation counts to clients.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 100 | YES | ('') |

## ClassDropInPricing
**Physical table:** `OSUSR_tr2_ClassDropInPricing`  
**Description:** Table that will store Class DropIn Pricing information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASSID | int |  | NO |  |
| NONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| ATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ClassEmailStatus
**Physical table:** `OSUSR_72o_ClassEmailStatus`  
**Description:** Static Entity that will store Class Email Status values  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ClassGoogleCalendar
**Physical table:** `OSUSR_6sr_ClassGoogleCalendar`  
**Description:** Keeps records of the Google Calendars a class has been exported to  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CLASSID | int |  | YES | (NULL) |
| GOOGLECALENDARID | bigint |  | YES | (NULL) |
| EXTERNALID | nvarchar | 1000 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ClassIntegrationAvailability
**Physical table:** `OSUSR_tr2_ClassIntegrationAvailability2`  
**Description:** Table that will store the class integration availability for a given class. The primary key is a Class Id  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASSID | int |  | NO |  |
| ISCLASSPASSENABLED | bit |  | YES | ((0)) |
| ISWELLHUBENABLED | bit |  | YES | ((0)) |

## ClassLateCancellationSetting
**Physical table:** `OSUSR_tr2_ClassLateCancellationSetting`  
**Description:** Table that will store Class late cancellation settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASSID | int |  | NO |  |
| COUNTLATECANCELLATIONS | bit |  | YES | ((0)) |
| CHARGELATECANCELLATIONFEE | bit |  | YES | ((0)) |
| LATECANCELLATIONFEE | decimal |  | YES | ((0)) |
| LATECANCELLATIONFEETAXRATEID | int |  | YES | (NULL) |

## ClassNoShowSetting
**Physical table:** `OSUSR_tr2_ClassNoShowSetting1`  
**Description:** Table that will store Class No Show settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASSID | int |  | NO |  |
| COUNTNOSHOWRESERVATIONS | bit |  | YES | ((0)) |
| CHARGENOSHOWFEE | bit |  | YES | ((0)) |
| NOSHOWFEE | decimal |  | YES | ((0)) |
| NOSHOWFEETAXRATEID | int |  | YES | (NULL) |

## ClassOnlineSalesSetting
**Physical table:** `OSUSR_tr2_ClassOnlineSalesSetting`  
**Description:** Table that will store Class online sales settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASSID | int |  | NO |  |
| DROPINLIMIT | int |  | YES | ((0)) |
| HASDROPINLIMIT | bit |  | YES | ((0)) |
| ISDROPINFULL | bit |  | YES | ((0)) |

## ClassRepeatType
**Physical table:** `OSUSR_oc9_ClassRepeatType`  
**Description:** Static with the values of the Class repeat type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ClassReservation
**Physical table:** `OSUSR_72o_ClassReservation`  
**Description:** Table that will store Class Reservation relative information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| CLASSID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| DROPINNAME | nvarchar | 255 | YES | ('') |
| CLASSRESERVATIONSTATUSID | int |  | YES | (NULL) |
| SEQUENCEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | ntext | 1073741823 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLASSEMAILSTATUSID | int |  | YES | (NULL) |
| ACCEPTGUID | nvarchar | 50 | YES | ('') |
| CANCELGUID | nvarchar | 50 | YES | ('') |
| ALLOWEDCANCELLATIONMINUTES | int |  | YES | ((0)) |
| ACTUALCANCELLATIONMINUTES | int |  | YES | ((0)) |
| MEMBERPLANID | int |  | YES | (NULL) |
| ISCANCELLEDFROMWAITLIST | bit |  | YES | ((0)) |
| ISLATECANCELLATION | bit |  | YES | ((0)) |
| HASCHECKEDLATECANCELLATION | bit |  | YES | ((0)) |
| ISUSERNOTIFIED | bit |  | YES | ((0)) |
| ONLINEMEMBERSHIPSALEID | int |  | YES | (NULL) |
| DROPINEMAIL | nvarchar | 250 | YES | ('') |
| LEADID | int |  | YES | (NULL) |
| COUNTTOWARDSATTENDANCELIMITS | bit |  | YES | ((0)) |
| ENFORCEMEMBERSHIPLIMITS | bit |  | YES | ((0)) |
| CHARGELATECANCELLATIONFEE | bit |  | YES | ((0)) |
| LATECANCELLATIONFEE | decimal |  | YES | ((0)) |
| LATECANCELLATIONFEETAXRATEID | int |  | YES | (NULL) |
| CLASSRESERVATIONSOURCEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| DROPINID | bigint |  | YES | (NULL) |
| RECURRINGCLASSRESERVATIONID | bigint |  | YES | (NULL) |

## ClassReservationPenalty
**Physical table:** `OSUSR_tr2_ClassReservationPenalty`  
**Description:** Class Revervation Penalty record, which will give the state that the penalties are in for a Class reservation and the date/time if they were updated (fee waived/session forgiven/refunded).  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASSRESERVATIONID | int |  | NO |  |
| ISPENALTYFEEWAIVED | bit |  | YES | ((0)) |
| ISPENALTYSESSIONFORGIVEN | bit |  | YES | ((0)) |
| PENALTYFEEWAIVEDBY | int |  | YES | (NULL) |
| PENALTYFEEWAIVEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PENALTYSESSIONFORGIVENBY | int |  | YES | (NULL) |
| PENALTYSESSIONFORGIVENON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISPENALTYREFUNDED | bit |  | YES | ((0)) |
| PENALTYREFUNDEDBY | int |  | YES | (NULL) |
| PENALTYREFUNDEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISPENALTYFEEREFUNDED | bit |  | YES | ((0)) |
| PENALTYFEEREFUNDEDBY | int |  | YES | (NULL) |
| PENALTYFEEREFUNDEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ClassReservationSetting
**Physical table:** `OSUSR_tr2_ClassReservationSetting3`  
**Description:** Table that will store Class reservation settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASSID | int |  | NO |  |
| WASAUTOCANCELCHECKED | bit |  | YES | ((0)) |

## ClassReservationSource
**Physical table:** `OSUSR_6sr_ClassReservationSource`  
**Description:** Defines where the user makes a class reservation.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ClassReservationStatus
**Physical table:** `OSUSR_72o_ClassReservationStatus`  
**Description:** Static Entity that will store Class Reservation Status values  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| ISWAITLIST | bit |  | YES | ((0)) |

## ClassSignInSetting
**Physical table:** `OSUSR_tr2_ClassSignInSetting`  
**Description:** Table that will store Class sign in settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASSID | int |  | NO |  |
| CLIENTSIGNISENABLED | bit |  | YES | ((0)) |
| CLIENTSIGNSTART | int |  | YES | ((0)) |
| CLIENTSIGNSTARTTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDRES | int |  | YES | ((0)) |
| CLIENTSIGNENDRESTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDRESTIMERELATION | int |  | YES | (NULL) |
| CLIENTSIGNENDRESTIMEPOINT | int |  | YES | (NULL) |
| CLIENTSIGNENDNORES | int |  | YES | ((0)) |
| CLIENTSIGNENDNORESTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDNORESTIMERELATI | int |  | YES | (NULL) |
| CLIENTSIGNENDNORESTIMEPOINT | int |  | YES | (NULL) |
| EMPLOYEESIGNSTART | int |  | YES | ((0)) |
| EMPLOYEESIGNSTARTTIMEFORMAT | int |  | YES | (NULL) |

## ClassStat
**Physical table:** `OSUSR_72o_ClassStat`  
**Description:** Table that will store Class Stat relative information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CLASSID | int |  | YES | (NULL) |
| CLASSSTATTYPEID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| DATETIMEVALUE | datetime |  | YES | ('1900-01-01 00:00:00') |

## ClassStatType
**Physical table:** `OSUSR_72o_ClassStatType`  
**Description:** Static Entity that will store Class Stat Type values  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ClassWarningStatus
**Physical table:** `OSUSR_72o_ClassWarningStatus`  
**Description:** Static Entity that will store Class Warning Status values  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CustomerSettingClassPolicy
**Physical table:** `OSUSR_72o_TenantSettingClassPolicy`  
**Description:** Table that will store Customer Setting Class Policy relative information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CHARGELATECANCELLATIONFEE | bit |  | YES | ((0)) |
| LATECANCELLATIONFEE | decimal |  | YES | ((0)) |
| LATECANCELLATIONFEETAXRATEID | int |  | YES | (NULL) |
| CHARGENOSHOWFEE | bit |  | YES | ((0)) |
| NOSHOWFEE | decimal |  | YES | ((0)) |
| NOSHOWFEETAXRATEID | int |  | YES | (NULL) |
| ALLOWDROPINPAYMENTS | bit |  | YES | ((0)) |
| ALLOWDROPINNOCHARGEPAYMENT | bit |  | YES | ((0)) |
| NONWODIFYDROPINFEE | decimal |  | YES | ((0)) |
| WODIFYDROPINFEE | decimal |  | YES | ((0)) |
| DROPINFEETAXRATEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| RESERVATIONOPEN | int |  | YES | ((0)) |
| RESERVATIONOPENTIMEFORMAT | int |  | YES | (NULL) |
| RESERVATIONCLOSE | int |  | YES | ((0)) |
| RESERVATIONCLOSETIMEFORMAT | int |  | YES | (NULL) |
| CANCELLATIONTIME | int |  | YES | ((0)) |
| CANCELLATIONTIMETIMEFORMAT | int |  | YES | (NULL) |
| CANCELCLASSTIME | int |  | YES | ((0)) |
| CANCELCLASSTIMEFORMAT | int |  | YES | (NULL) |
| CANCELCLASSIFNORESERVATIONS | bit |  | YES | ((0)) |
| HASREGENERATEDCLASSES | bit |  | YES | ((0)) |
| CLASSATTENDANCEVISIBLE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | NO | ((0)) |
| USESEPARATEDROPINFEE | bit |  | YES | ((1)) |
| CLIENTSIGNISENABLED | bit |  | YES | ((1)) |
| CLIENTSIGNSTART | int |  | YES | ((24)) |
| CLIENTSIGNSTARTTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDRES | int |  | YES | ((0)) |
| CLIENTSIGNENDRESTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDRESTIMERELATION | int |  | YES | (NULL) |
| CLIENTSIGNENDRESTIMEPOINT | int |  | YES | (NULL) |
| CLIENTSIGNENDNORES | int |  | YES | ((0)) |
| CLIENTSIGNENDNORESTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDNORESTIMERELATI | int |  | YES | (NULL) |
| CLIENTSIGNENDNORESTIMEPOINT | int |  | YES | (NULL) |
| EMPLOYEESIGNSTART | int |  | YES | ((24)) |
| EMPLOYEESIGNSTARTTIMEFORMAT | int |  | YES | (NULL) |
| CANCELCLASSNUMBERRESERVATION | int |  | YES | ((1)) |
| RESERVATIONSCLOSETIMERELATIO | int |  | YES | (NULL) |
| RESERVATIONSCLOSETIMEPOINT | int |  | YES | (NULL) |
| CLASSCOUNTDISPLAYTYPEID | int |  | YES | (NULL) |
| ATTENDANCECOUNTDISPLAYTYPEID | int |  | YES | (NULL) |

## RecurringClass
**Physical table:** `OSUSR_72o_RecurringClass`  
**Description:** Table that will store Recurring Class relative information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| PROGRAMID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| STARTTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| DAYOFWEEKID | int |  | YES | (NULL) |
| ISSUNDAY | bit |  | YES | ((0)) |
| SUNDAYLIMIT | int |  | YES | ((0)) |
| SUNDAYCOACH | int |  | YES | (NULL) |
| ISMONDAY | bit |  | YES | ((0)) |
| MONDAYLIMIT | int |  | YES | ((0)) |
| MONDAYCOACH | int |  | YES | (NULL) |
| ISTUESDAY | bit |  | YES | ((0)) |
| TUESDAYLIMIT | int |  | YES | ((0)) |
| TUESDAYCOACH | int |  | YES | (NULL) |
| ISWEDNESDAY | bit |  | YES | ((0)) |
| WEDNESDAYLIMIT | int |  | YES | ((0)) |
| WEDNESDAYCOACH | int |  | YES | (NULL) |
| ISTHURSDAY | bit |  | YES | ((0)) |
| THURSDAYLIMIT | int |  | YES | ((0)) |
| THURSDAYCOACH | int |  | YES | (NULL) |
| ISFRIDAY | bit |  | YES | ((0)) |
| FRIDAYLIMIT | int |  | YES | ((0)) |
| FRIDAYCOACH | int |  | YES | (NULL) |
| ISSATURDAY | bit |  | YES | ((0)) |
| SATURDAYLIMIT | int |  | YES | ((0)) |
| SATURDAYCOACH | int |  | YES | (NULL) |
| RECURRINGCLASSENDTYPEID | int |  | YES | (NULL) |
| OCCURRENCES | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CALENDARCOLOR | nvarchar | 6 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ALLOWSUNDAYWAITLIST | bit |  | YES | ((0)) |
| SUNDAYASSISTANTCOACHID | int |  | YES | (NULL) |
| ALLOWMONDAYWAITLIST | bit |  | YES | ((0)) |
| MONDAYASSISTANTCOACHID | int |  | YES | (NULL) |
| ALLOWTUESDAYWAITLIST | bit |  | YES | ((0)) |
| TUESDAYASSISTANTCOACHID | int |  | YES | (NULL) |
| ALLOWWEDNESDAYWAITLIST | bit |  | YES | ((0)) |
| WEDNESDAYASSISTANTCOACHID | int |  | YES | (NULL) |
| ALLOWTHURSDAYWAITLIST | bit |  | YES | ((0)) |
| THURSDAYASSISTANTCOACHID | int |  | YES | (NULL) |
| ALLOWFRIDAYWAITLIST | bit |  | YES | ((0)) |
| FRIDAYASSISTANTCOACHID | int |  | YES | (NULL) |
| ALLOWSATURDAYWAITLIST | bit |  | YES | ((0)) |
| SATURDAYASSISTANTCOACHID | int |  | YES | (NULL) |
| ISRESERVATIONHOURSOVERRIDE | bit |  | YES | ((0)) |
| RESERVATIONHOURS | int |  | YES | ((0)) |
| ISCANCELLATIONHOURSOVERRIDE | bit |  | YES | ((0)) |
| CANCELLATIONHOURS | int |  | YES | ((0)) |
| COUNTTOWARDSATTENDANCELIMITS | bit |  | YES | ((0)) |
| RESERVATIONOPEN | int |  | YES | ((0)) |
| RESERVATIONOPENTIMEFORMAT | int |  | YES | (NULL) |
| RESERVATIONCLOSE | int |  | YES | ((0)) |
| RESERVATIONCLOSETIMEFORMAT | int |  | YES | (NULL) |
| CANCELLATIONTIME | int |  | YES | ((0)) |
| CANCELLATIONTIMETIMEFORMAT | int |  | YES | (NULL) |
| CANCELCLASSIFNORESERVATIONS | bit |  | YES | ((0)) |
| ISDROPINONLINE | bit |  | YES | ((0)) |
| ISFREETRIALONLINE | bit |  | YES | ((0)) |
| SUNDAYISDROPINONLINE | bit |  | YES | ((0)) |
| SUNDAYISFREETRIALONLINE | bit |  | YES | ((0)) |
| MONDAYISDROPINONLINE | bit |  | YES | ((0)) |
| MONDAYISFREETRIALONLINE | bit |  | YES | ((0)) |
| TUESDAYISDROPINONLINE | bit |  | YES | ((0)) |
| TUESDAYISFREETRIALONLINE | bit |  | YES | ((0)) |
| WEDNESDAYISDROPINONLINE | bit |  | YES | ((0)) |
| WEDNESDAYISFREETRIALONLINE | bit |  | YES | ((0)) |
| THURSDAYISDROPINONLINE | bit |  | YES | ((0)) |
| THURSDAYISFREETRIALONLINE | bit |  | YES | ((0)) |
| FRIDAYISDROPINONLINE | bit |  | YES | ((0)) |
| FRIDAYISFREETRIALONLINE | bit |  | YES | ((0)) |
| SATURDAYISDROPINONLINE | bit |  | YES | ((0)) |
| SATURDAYISFREETRIALONLINE | bit |  | YES | ((0)) |
| DROPINHASBEENMODIFIED | bit |  | YES | ((0)) |
| FREETRIALHASBEENMODIFIED | bit |  | YES | ((0)) |
| CANCELCLASSTIME | int |  | YES | ((0)) |
| CANCELCLASSTIMEFORMAT | int |  | YES | (NULL) |
| CLASSREPEATTYPEID | int |  | YES | (NULL) |
| CLASSREPEATCUSTOMTYPEID | int |  | YES | (NULL) |
| CLASSREPEATCUSTOMSTEP | int |  | YES | ((0)) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| WAITLISTTYPEID | int |  | YES | (NULL) |
| DESCRIPTION | nvarchar | 1000 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| MONDAYFREETRIALLIMIT | int |  | YES | ((0)) |
| MONDAYHASFREETRIALLIMIT | bit |  | YES | ((0)) |
| MONDAYISFREETRIALFULL | bit |  | YES | ((0)) |
| TUESDAYFREETRIALLIMIT | int |  | YES | ((0)) |
| TUESDAYHASFREETRIALLIMIT | bit |  | YES | ((0)) |
| TUESDAYISFREETRIALFULL | bit |  | YES | ((0)) |
| WEDNESDAYFREETRIALLIMIT | int |  | YES | ((0)) |
| WEDNESDAYHASFREETRIALLIMIT | bit |  | YES | ((0)) |
| WEDNESDAYISFREETRIALFULL | bit |  | YES | ((0)) |
| THURSDAYFREETRIALLIMIT | int |  | YES | ((0)) |
| THURSDAYHASFREETRIALLIMIT | bit |  | YES | ((0)) |
| THURSDAYISFREETRIALFULL | bit |  | YES | ((0)) |
| FRIDAYFREETRIALLIMIT | int |  | YES | ((0)) |
| FRIDAYHASFREETRIALLIMIT | bit |  | YES | ((0)) |
| FRIDAYISFREETRIALFULL | bit |  | YES | ((0)) |
| SATURDAYFREETRIALLIMIT | int |  | YES | ((0)) |
| SATURDAYHASFREETRIALLIMIT | bit |  | YES | ((0)) |
| SATURDAYISFREETRIALFULL | bit |  | YES | ((0)) |
| SUNDAYFREETRIALLIMIT | int |  | YES | ((0)) |
| SUNDAYHASFREETRIALLIMIT | bit |  | YES | ((0)) |
| SUNDAYISFREETRIALFULL | bit |  | YES | ((0)) |
| MONDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| MONDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| TUESDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| TUESDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| WEDNESDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| WEDNESDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| THURSDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| THURSDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| FRIDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| FRIDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| SATURDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| SATURDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| SUNDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| SUNDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| CANCELCLASSNUMBERRESERVATION | int |  | YES | ((0)) |
| RESERVATIONSOPENTIMERELATION | int |  | YES | (NULL) |
| RESERVATIONSOPENTIMEPOINT | int |  | YES | (NULL) |
| RESERVATIONSCLOSETIMERELATIO | int |  | YES | (NULL) |
| RESERVATIONSCLOSETIMEPOINT | int |  | YES | (NULL) |
| ISCLASSPASSENABLED | bit |  | YES |  |

## RecurringClassDropInPricing
**Physical table:** `OSUSR_tr2_RecurringClassDropInPricing`  
**Description:** Table that will store the RecurringClass DropIn Pricing information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| RECURRINGCLASSID | int |  | NO |  |
| MONDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| MONDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| TUESDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| TUESDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| WEDNESDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| WEDNESDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| THURSDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| THURSDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| FRIDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| FRIDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| SATURDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| SATURDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| SUNDAYNONATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| SUNDAYATHLETEDROPINFEE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## RecurringClassEndType
**Physical table:** `OSUSR_72o_RecurringClassEndType`  
**Description:** Contains the end type for the recurring class  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## RecurringClassIntegrationAvailability
**Physical table:** `OSUSR_tr2_RecurringClassIntegrationAvailability6`  
**Description:** Table that will store Class Integration Availability  Should be unique to RecurringClassId/DayOfWeekId  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| RECURRINGCLASSID | int |  | YES | (NULL) |
| DAYOFWEEKID | int |  | YES | (NULL) |
| ISCLASSPASSENABLED | bit |  | YES | ((0)) |
| ISWELLHUBENABLED | bit |  | YES | ((0)) |

## RecurringClassLateCancellationSetting
**Physical table:** `OSUSR_tr2_RecurringClassLateCancellationSetting6`  
**Description:** Table that will store Recurring Class late cancellation settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| RECURRINGCLASSID | int |  | NO |  |
| COUNTLATECANCELLATIONS | bit |  | YES | ((0)) |
| CHARGELATECANCELLATIONFEE | bit |  | YES | ((0)) |
| LATECANCELLATIONFEE | decimal |  | YES | ((0)) |
| LATECANCELLATIONFEETAXRATEID | int |  | YES | (NULL) |

## RecurringClassNoShowSetting
**Physical table:** `OSUSR_tr2_RecurringClassNoShowSetting6`  
**Description:** Table that will store Recurring Class No Show settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| RECURRINGCLASSID | int |  | NO |  |
| COUNTNOSHOWRESERVATIONS | bit |  | YES | ((0)) |
| CHARGENOSHOWFEE | bit |  | YES | ((0)) |
| NOSHOWFEE | decimal |  | YES | ((0)) |
| NOSHOWFEETAXRATEID | int |  | YES | (NULL) |

## RecurringClassOnlineSalesSetting
**Physical table:** `OSUSR_tr2_RecurringClassOnlineSalesSetting`  
**Description:** Table that will store Class online sales settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| RECURRINGCLASSID | int |  | YES | (NULL) |
| DAYOFWEEKID | int |  | YES | (NULL) |
| DROPINLIMIT | int |  | YES | ((0)) |
| HASDROPINLIMIT | bit |  | YES | ((0)) |

## RecurringClassRepeatType
**Physical table:** `OSUSR_oc9_RecurringClassRepeatType`  
**Description:** The repeat type when a recurring class will occur for instance every 2 weeks in Sundays  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## RecurringClassReservation
**Physical table:** `OSUSR_tr2_RecurringClassReservation6`  
**Description:** Represents a class reservation that repeats across instances of a recurring class  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| STATUSID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| MEMBERPLANID | int |  | YES | (NULL) |
| REPEATTYPEID | int |  | YES | (NULL) |
| ENDTYPEID | int |  | YES | (NULL) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMREPEATINTERVAL | int |  | YES | ((0)) |
| OCCURRENCES | int |  | YES | ((0)) |
| ISSUNDAY | bit |  | YES | ((0)) |
| ISMONDAY | bit |  | YES | ((0)) |
| ISTUESDAY | bit |  | YES | ((0)) |
| ISWEDNESDAY | bit |  | YES | ((0)) |
| ISTHURSDAY | bit |  | YES | ((0)) |
| ISFRIDAY | bit |  | YES | ((0)) |
| ISSATURDAY | bit |  | YES | ((0)) |
| OVERRIDEWAITLIST | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| RECURRINGCLASSID | int |  | YES | (NULL) |

## RecurringClassReservationEmailItem
**Physical table:** `OSUSR_tr2_RecurringClassReservationEmailItem1`  
**Description:** Represents a line item to be sent with a recurring class reservation email  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| RECURRINGCLASSRESERVATIONID | bigint |  | YES | (NULL) |
| CLASSID | int |  | YES | (NULL) |
| ISSUE | nvarchar | 200 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## RecurringClassReservationStatus
**Physical table:** `OSUSR_tr2_RecurringClassReservationStatus6`  
**Description:** Contains the statuses of a recurring class reservation  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |

## RecurringClassSignInSetting
**Physical table:** `OSUSR_tr2_RecurringClassSignInSetting`  
**Description:** Table that will store Class sign in settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| RECURRINGCLASSID | int |  | NO |  |
| CLIENTSIGNISENABLED | bit |  | YES | ((0)) |
| CLIENTSIGNSTART | int |  | YES | ((0)) |
| CLIENTSIGNSTARTTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDRES | int |  | YES | ((0)) |
| CLIENTSIGNENDRESTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDRESTIMERELATION | int |  | YES | (NULL) |
| CLIENTSIGNENDRESTIMEPOINT | int |  | YES | (NULL) |
| CLIENTSIGNENDNORES | int |  | YES | ((0)) |
| CLIENTSIGNENDNORESTIMEFORMAT | int |  | YES | (NULL) |
| CLIENTSIGNENDNORESTIMERELATI | int |  | YES | (NULL) |
| CLIENTSIGNENDNORESTIMEPOINT | int |  | YES | (NULL) |
| EMPLOYEESIGNSTART | int |  | YES | ((0)) |
| EMPLOYEESIGNSTARTTIMEFORMAT | int |  | YES | (NULL) |

## RejectedSignInLog
**Physical table:** `OSUSR_6sr_RejectedSignInLog`  
**Description:** Table that will store Rejected Sign In Log relative information  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| DATE | nvarchar | 50 | YES | ('') |
| CLASSID | int |  | YES | (NULL) |
| MESSAGE | nvarchar | 2000 | YES | ('') |
| ISSESSIONPLANEXPIRED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## Request
**Physical table:** `OSUSR_tr2_Request`  
**Description:** Request data to be used in an Asynchronous Process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUESTTYPEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| MESSAGE | nvarchar | 1500 | YES | ('') |
| SENDER | nvarchar | 400 | YES | ('') |
| RECIPIENT | nvarchar | 400 | YES | ('') |
| CONVERSATIONSSID | nvarchar | 50 | YES | ('') |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |
| SEGMENTID | bigint |  | YES | ((0)) |
| TASKID | nvarchar | 50 | YES | ('') |
| PARTICIPANTSID | nvarchar | 50 | YES | ('') |
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
**Physical table:** `OSUSR_tr2_RequestType`  
**Description:** The type of request  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TimerMissingAthleteEmailControl
**Physical table:** `OSUSR_tr2_TimerMissingAthleteEmailControl`  
**Description:** Entity used to control which emails were already sent to a specific Customer. This entity was cretaed in order to be able to abort the cycle that where the process of sending emails is being done, and after restart doesn't send an email to a client that already sent  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| LASTUSERPROCESSED | int |  | YES | (NULL) |
| EXECUTIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |

## WaitlistType
**Physical table:** `OSUSR_6sr_WaitlistType`  
**Description:** Waitlist behavior type FirstReply - All clients emailed, first to reply gets added to class. PriorityWaitlist_FirstSignUp - Client automatically added to the class in the order they signed up.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
