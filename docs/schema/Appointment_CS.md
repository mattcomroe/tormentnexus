# Appointment_CS

## Tables

- [Appointment](#appointment)
- [AppointmentGenerationError](#appointmentgenerationerror)
- [AppointmentGoogleCalendar](#appointmentgooglecalendar)
- [AppointmentSyncQueue](#appointmentsyncqueue)
- [AsyncProcess](#asyncprocess)
- [Availability](#availability)
- [AvailabilityServices](#availabilityservices)
- [Booking](#booking)
- [BookingCancellation](#bookingcancellation)
- [BookingDefaultConfiguration](#bookingdefaultconfiguration)
- [BookingPenalty](#bookingpenalty)
- [BookingStatus](#bookingstatus)
- [CalendarEventType](#calendareventtype)
- [CalendarView](#calendarview)
- [CalendarViewService](#calendarviewservice)
- [Color](#color)
- [ProviderCalendarView](#providercalendarview)
- [ProviderCalendarViewService](#providercalendarviewservice)
- [RecurringAppointment](#recurringappointment)
- [RecurringAppointmentBooking](#recurringappointmentbooking)
- [Repetition](#repetition)
- [RepetitionCategory](#repetitioncategory)
- [RepetitionEndType](#repetitionendtype)
- [RepetitionServices](#repetitionservices)
- [RepetitionSyncQueue](#repetitionsyncqueue)
- [RepetitionType](#repetitiontype)
- [Request](#request)
- [RequestAppointmentForUpdate](#requestappointmentforupdate)
- [RequestBookingForUpdate](#requestbookingforupdate)
- [RequestRepetitionForUpdate](#requestrepetitionforupdate)
- [RequestType](#requesttype)
- [Service](#service)
- [ServiceDuration](#serviceduration)
- [ServiceLocation](#servicelocation)
- [ServiceMembership](#servicemembership)
- [ServiceProvider](#serviceprovider)
- [ServiceProviderEmail](#serviceprovideremail)
- [ServiceWaiver](#servicewaiver)

## Appointment
**Physical table:** `OSUSR_591_APPOINTMENT`  
**Description:** Entity that stores appointments in a Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| SERVICEID | bigint |  | YES | (NULL) |
| PROVIDERID | int |  | YES | (NULL) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| PROVIDERCHECKINAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| SIGNATURE | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SERVICEDURATIONID | bigint |  | YES | (NULL) |
| EXTERNALID | bigint |  | YES | ((0)) |
| STARTDATETIMESERVER | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| REPETITIONID | bigint |  | YES | (NULL) |
| FLAGTODELETE | bit |  | YES | ((0)) |
| ISFREEINTROFULL | bit |  | YES | ((0)) |
| APPOINTMENTGUID | nvarchar | 36 | YES | ('') |
| PAYRATEID | bigint |  | YES | (NULL) |

## AppointmentGenerationError
**Physical table:** `OSUSR_MJX_APPOINTMENTGENERATIONERROR`  
**Description:** When an error occurs during appointment generation, logs error associated with failed generation  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| REPETITIONID | bigint |  | YES | (NULL) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## AppointmentGoogleCalendar
**Physical table:** `OSUSR_591_APPOINTMENTGOOGLECALENDAR`  
**Description:** Keeps records of the Google Calendars an appointment has been exported to  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| APPOINTMENTID | bigint |  | YES | (NULL) |
| GOOGLECALENDARID | bigint |  | YES | (NULL) |
| EXTERNALID | nvarchar | 1000 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## AppointmentSyncQueue
**Physical table:** `OSUSR_591_APPOINTMENTSYNCQUEUE`  
**Description:** Queue of appointments that need to be exported to Google Calendar.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| APPOINTMENTID | bigint |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## AsyncProcess
**Physical table:** `OSUSR_591_ASYNCPROCESS`  
**Description:** Asynchronous Process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| REQUESTID | bigint |  | YES | (NULL) |

## Availability
**Physical table:** `OSUSR_591_AVAILABILITY`  
**Description:** Provider availability  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REPETITIONID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| PROVIDERID | int |  | YES | (NULL) |
| ISBLOCKEDTIME | bit |  | YES | ((0)) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| EXTERNALID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## AvailabilityServices
**Physical table:** `OSUSR_591_AVAILABILITYSERVICES`  
**Description:** Services that are associated with an availability  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| AVAILABILITYID | bigint |  | YES | (NULL) |
| SERVICEID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## Booking
**Physical table:** `OSUSR_591_BOOKING`  
**Description:** Entity that stores appointment bookings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| APPOINTMENTID | bigint |  | YES | (NULL) |
| CLIENTID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| BOOKINGSTATUSID | int |  | YES | (NULL) |
| MEMBERSHIPID | int |  | YES | (NULL) |
| REPETITIONID | bigint |  | YES | (NULL) |
| ORIGINALREPETITIONID | bigint |  | YES | (NULL) |
| ISFREETRIAL | bit |  | YES | ((0)) |
| CHECKINON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SENTREMINDEREMAIL | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXTERNALID | bigint |  | YES | ((0)) |
| SENTREMINDEREMAILPROVIDER | bit |  | YES | ((0)) |
| ONLINEMEMBERSHIPSALEID | int |  | YES | (NULL) |
| SENTREMINDERPUSHUPCOMINGAPPT | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## BookingCancellation
**Physical table:** `OSUSR_591_BOOKINGCANCELLATION`  
**Description:** Entity to store booking cancellation info  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| BOOKINGID | bigint |  | YES | (NULL) |
| INVOICEHEADERID | int |  | YES | (NULL) |
| ISLATECANCELLATION | bit |  | YES | ((0)) |
| CANCELLEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CANCELLEDBY | int |  | YES | (NULL) |
| HASLOSSOFSESSION | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## BookingDefaultConfiguration
**Physical table:** `OSUSR_591_BOOKINGDEFAULTCONFIGURATION`  
**Description:** Entity that stores the services booking configuration by Customer. These values will populate the ServiceBooking record when creating a new service.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| BOOKINGOPEN | int |  | YES | ((0)) |
| BOOKINGOPENUNITOFTIMEID | int |  | YES | (NULL) |
| BOOKINGCLOSE | int |  | YES | ((0)) |
| BOOKINGCLOSEUNITOFTIMEID | int |  | YES | (NULL) |
| HASCANCELLATIONPOLICY | bit |  | YES | ((0)) |
| CANCELLATIONTIMEWINDOW | int |  | YES | ((0)) |
| CANCELLATIONUNITOFTIMEID | int |  | YES | (NULL) |
| CANCELLATIONISLOSSOFSESSION | bit |  | YES | ((0)) |
| CANCELLATIONHASFLATFEE | bit |  | YES | ((0)) |
| CANCELLATIONTAXID | int |  | YES | (NULL) |
| CANCELLATIONFLATFEEVALUE | decimal |  | YES | ((0)) |
| HASNOSHOWPENALTY | bit |  | YES | ((0)) |
| NOSHOWISLOSSOFSESSION | bit |  | YES | ((0)) |
| NOSHOWHASFLATFEE | bit |  | YES | ((0)) |
| NOSHOWSTAXID | int |  | YES | (NULL) |
| NOSHOWFLATFEEVALUE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| EXTERNALID | bigint |  | YES | ((0)) |
| SENDMISSINGSIGNINSEMAIL | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| NOSHOWTIMEWINDOW | int |  | YES | ((0)) |
| NOSHOWUNITOFTIMEID | int |  | YES | (NULL) |
| CANCLIENTSBOOK | bit |  | YES | ((0)) |
| ALLOWPROVIDERDOUBLEBOOKING | bit |  | YES | ((0)) |

## BookingPenalty
**Physical table:** `OSUSR_MJX_BOOKINGPENALTY`  
**Description:** Booking Penalty record, which will give the state that the penalties are in for a Booking and the date/time if they were updated (fee waived/session forgiven/refunded).  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| BOOKINGID | bigint |  | NO |  |
| ISPENALTYFEEREFUNDED | bit |  | YES | ((0)) |
| ISPENALTYFEEWAIVED | bit |  | YES | ((0)) |
| ISPENALTYSESSIONFORGIVEN | bit |  | YES | ((0)) |
| PENALTYFEEREFUNDEDBY | int |  | YES | (NULL) |
| PENALTYFEEREFUNDEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PENALTYFEEWAIVEDBY | int |  | YES | (NULL) |
| PENALTYFEEWAIVEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PENALTYSESSIONFORGIVENBY | int |  | YES | (NULL) |
| PENALTYSESSIONFORGIVENON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## BookingStatus
**Physical table:** `OSUSR_591_BOOKINGSTATUS`  
**Description:** Status of the booking  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## CalendarEventType
**Physical table:** `OSUSR_591_CALENDAREVENTTYPE`  
**Description:** Defines all the events that can be created on calendar  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## CalendarView
**Physical table:** `OSUSR_591_CALENDARVIEW`  
**Description:** Table to hold the calendar view filter for a user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| USERID | int |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| PROVIDERID | int |  | YES | (NULL) |
| ISWEEKVIEW | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## CalendarViewService
**Physical table:** `OSUSR_591_CALENDARVIEWSERVICE`  
**Description:** Service that is associated with the default view  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| CALENDARVIEWID | int |  | YES | (NULL) |
| SERVICEID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## Color
**Physical table:** `OSUSR_591_COLOR`  
**Description:** Color to be displayed in the calendar  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| HEXCOLOR | nvarchar | 10 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## ProviderCalendarView
**Physical table:** `OSUSR_591_PROVIDERCALENDARVIEW`  
**Description:** Table to hold the calendar view filter for a user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| USERID | int |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| ISWEEKVIEW | bit |  | YES | ((0)) |
| ISSHOWCLASSESANDAPPOINTMENTS | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ProviderCalendarViewService
**Physical table:** `OSUSR_591_PROVIDERCALENDARVIEWSERVICE`  
**Description:** Service that is associated with the provider default view  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| PROVIDERCALENDARVIEWID | int |  | YES | (NULL) |
| SERVICEID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## RecurringAppointment
**Physical table:** `OSUSR_591_RECURRINGAPPOINTMENT`  
**Description:** Stores appointment data relating to a recurring appointment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| SERVICEID | bigint |  | YES | (NULL) |
| PROVIDERID | int |  | YES | (NULL) |
| REPETITIONID | bigint |  | YES | (NULL) |
| SERVICEDURATIONID | bigint |  | YES | (NULL) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| STARTTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| SIGNATURE | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXTERNALID | bigint |  | YES | ((0)) |
| PREVIOUSAPPOINTMENTSGENERATE | bigint |  | YES | ((0)) |
| PASTAPPOINTMENTSGENERATED | bigint |  | YES | ((0)) |
| LASTGENERATEDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| PAYRATEID | bigint |  | YES | (NULL) |

## RecurringAppointmentBooking
**Physical table:** `OSUSR_591_RECURRINGAPPOINTMENTBOOKINGS`  
**Description:** Entity that stores appointment bookings used for generating recurring appointments  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CLIENTID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| REPETITIONID | bigint |  | YES | (NULL) |
| ORIGINALREPETITIONID | bigint |  | YES | (NULL) |
| ISFREETRIAL | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXTERNALID | bigint |  | YES | ((0)) |

## Repetition
**Physical table:** `OSUSR_591_REPETITION`  
**Description:** Event repetition configurations  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| REPETITIONTYPEID | int |  | YES | (NULL) |
| REPETITIONENDTYPEID | int |  | YES | (NULL) |
| REPETITIONCATEGORYID | int |  | YES | (NULL) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDAFTER | int |  | YES | ((0)) |
| REPEATEVERY | int |  | YES | ((0)) |
| REPEATSONMONDAY | bit |  | YES | ((0)) |
| REPEATSONTUESDAY | bit |  | YES | ((0)) |
| REPEATSONWEDNESDAY | bit |  | YES | ((0)) |
| REPEATSONTHURSDAY | bit |  | YES | ((0)) |
| REPEATSONFRIDAY | bit |  | YES | ((0)) |
| REPEATSONSATURDAY | bit |  | YES | ((0)) |
| REPEATSONSUNDAY | bit |  | YES | ((0)) |
| STARTTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| LOCATIONID | int |  | YES | (NULL) |
| PROVIDERID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLIENTID | int |  | YES | (NULL) |
| EXTERNALID | bigint |  | YES | ((0)) |
| REPETITIONSIGNATURE | nvarchar | 1024 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PAYRATEID | bigint |  | YES | (NULL) |

## RepetitionCategory
**Physical table:** `OSUSR_591_REPETITIONCATEGORY`  
**Description:** Repetition Category  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## RepetitionEndType
**Physical table:** `OSUSR_591_REPETITIONENDTYPE`  
**Description:** Repetition End Type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## RepetitionServices
**Physical table:** `OSUSR_591_REPETITIONSERVICES`  
**Description:** Services that are associated with a repetition  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| REPETITIONID | bigint |  | YES | (NULL) |
| SERVICEID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## RepetitionSyncQueue
**Physical table:** `OSUSR_591_REPETITIONSYNCQUEUE`  
**Description:** Queue of repetiton that need to be exported to Google Calendar.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| REPETITIONID | bigint |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## RepetitionType
**Physical table:** `OSUSR_591_REPETITIONTYPE`  
**Description:** Repetition Type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_MJX_REQUEST`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

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

## RequestAppointmentForUpdate
**Physical table:** `OSUSR_MJX_CHANGEREPETITION_APPOINTMENT`  
**Description:** Entity that stores request details for updating appointment and changing repetition  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| APPOINTMENTID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| LOCATIONID | bigint |  | YES | ((0)) |
| SERVICEID | bigint |  | YES | ((0)) |
| PROVIDERID | bigint |  | YES | ((0)) |
| SERVICEDURATIONID | bigint |  | YES | ((0)) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| STARTDATETIMESERVER | datetime |  | YES | ('1900-01-01 00:00:00') |
| PROVIDERCHECKINAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| SIGNATURE | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| EXTERNALID | bigint |  | YES | ((0)) |
| REPETITIONID | bigint |  | YES | ((0)) |
| FLAGTODELETE | bit |  | YES | ((0)) |
| ISFREEINTROFULL | bit |  | YES | ((0)) |
| HASFREEINTROLIMIT | bit |  | YES | ((0)) |
| FREEINTROLIMIT | int |  | YES | ((0)) |
| REQUESTID | bigint |  | YES | (NULL) |
| PAYRATEID | bigint |  | YES | ((0)) |

## RequestBookingForUpdate
**Physical table:** `OSUSR_MJX_CHANGEREPETITION_BOOKING`  
**Description:** Entity that stores request details for updating appointment and changing repetition  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| BOOKINGID | bigint |  | YES | ((0)) |
| CLIENTID | bigint |  | YES | ((0)) |
| LEADID | bigint |  | YES | ((0)) |
| ISFREETRIAL | bit |  | YES | ((0)) |
| MEMBERSHIPID | bigint |  | YES | ((0)) |
| REPETITIONID | bigint |  | YES | ((0)) |
| PERSONID | nvarchar | 50 | YES | ('') |
| BOOKINGSTATUSID | bigint |  | YES | ((0)) |
| CHECKINON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ONLINEMEMBERSHIPSALEID | bigint |  | YES | ((0)) |
| REQUESTID | bigint |  | YES | (NULL) |

## RequestRepetitionForUpdate
**Physical table:** `OSUSR_MJX_CHANGEREPETITION_REPETITION`  
**Description:** Entity that stores request details for updating appointment and changing repetition  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REPETITIONID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| REPETITIONTYPEID | bigint |  | YES | ((0)) |
| REPETITIONENDTYPEID | bigint |  | YES | ((0)) |
| REPETITIONCATEGORYID | bigint |  | YES | ((0)) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDAFTER | int |  | YES | ((0)) |
| REPEATEVERY | int |  | YES | ((0)) |
| REPEATSONMONDAY | bit |  | YES | ((0)) |
| REPEATSONTUESDAY | bit |  | YES | ((0)) |
| REPEATSONWEDNESDAY | bit |  | YES | ((0)) |
| REPEATSONTHURSDAY | bit |  | YES | ((0)) |
| REPEATSONFRIDAY | bit |  | YES | ((0)) |
| REPEATSONSATURDAY | bit |  | YES | ((0)) |
| REPEATSONSUNDAY | bit |  | YES | ((0)) |
| STARTTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| LOCATIONID | bigint |  | YES | ((0)) |
| PROVIDERID | bigint |  | YES | ((0)) |
| CLIENTID | bigint |  | YES | ((0)) |
| REPETITIONSIGNATURE | nvarchar | 1024 | YES | ('') |
| EXTERNALID | bigint |  | YES | ((0)) |
| REQUESTID | bigint |  | YES | (NULL) |
| PAYRATEID | bigint |  | YES | ((0)) |

## RequestType
**Physical table:** `OSUSR_MJX_REQUESTTYPE1`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Service
**Physical table:** `OSUSR_591_SERVICE`  
**Description:** Entity that stores the services provided by Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| NAME | nvarchar | 250 | YES | ('') |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| BUFFERTIME | int |  | YES | ((0)) |
| ATTENDANCELIMIT | int |  | YES | ((0)) |
| ISSTARTING_00 | bit |  | YES | ((0)) |
| ISSTARTING_05 | bit |  | YES | ((0)) |
| ISSTARTING_10 | bit |  | YES | ((0)) |
| ISSTARTING_15 | bit |  | YES | ((0)) |
| ISSTARTING_20 | bit |  | YES | ((0)) |
| ISSTARTING_25 | bit |  | YES | ((0)) |
| ISSTARTING_30 | bit |  | YES | ((0)) |
| ISSTARTING_35 | bit |  | YES | ((0)) |
| ISSTARTING_40 | bit |  | YES | ((0)) |
| ISSTARTING_45 | bit |  | YES | ((0)) |
| ISSTARTING_50 | bit |  | YES | ((0)) |
| ISSTARTING_55 | bit |  | YES | ((0)) |
| SERVICEICONID | int |  | YES | (NULL) |
| BOOKINGOPENTIME | int |  | YES | ((0)) |
| BOOKINGOPENUNITOFTIMEID | int |  | YES | (NULL) |
| BOOKINGCLOSETIME | int |  | YES | ((0)) |
| BOOKINGCLOSEUNITOFTIMEID | int |  | YES | (NULL) |
| HASCANCELLATIONPOLICY | bit |  | YES | ((0)) |
| CANCELLATIONTIMEWINDOW | int |  | YES | ((0)) |
| CANCELLATIONUNITOFTIMEID | int |  | YES | (NULL) |
| CANCELLATION_HASLOSSOFSESSIO | bit |  | YES | ((0)) |
| CANCELLATION_HASFLATFEE | bit |  | YES | ((0)) |
| CANCELLATION_FLATFEEVALUE | decimal |  | YES | ((0)) |
| NOSHOW_HASPENALTY | bit |  | YES | ((0)) |
| NOSHOW_HASLOSSOFSESSION | bit |  | YES | ((0)) |
| NOSHOW_HASFLATFEE | bit |  | YES | ((0)) |
| NOSHOW_FLATFEEVALUE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| EXTERNALID | bigint |  | YES | ((0)) |
| CURRENTSTEP | int |  | YES | ((0)) |
| HEXCOLOR | nvarchar | 10 | YES | ('') |
| CANCELLATIONTAXID | int |  | YES | (NULL) |
| NOSHOWSTAXID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| FREEINTROLIMIT | int |  | YES | ((0)) |
| HASFREEINTROLIMIT | bit |  | YES | ((0)) |
| SSI_ENABLED | bit |  | YES | ((0)) |
| SSI_STARTSPRIORTOLENGTH | int |  | YES | ((0)) |
| SSI_STARTSPRIORTOTYPE | int |  | YES | (NULL) |
| SSI_ENDSAFTERLENGTH | int |  | YES | ((0)) |
| SSI_ENDSAFTERTYPE | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| ICON | nvarchar | 50 | YES | ('') |
| NOSHOWTIMEWINDOW | int |  | YES | ((0)) |
| NOSHOWUNITOFTIMEID | int |  | YES | (NULL) |
| SSI_ISENDSBEFORE | bit |  | YES | ((0)) |
| SSI_ISENDSSTARTTIME | bit |  | YES | ((0)) |

## ServiceDuration
**Physical table:** `OSUSR_591_SERVICEDURATION`  
**Description:** Store all the durations that a service can have  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SERVICEID | bigint |  | YES | (NULL) |
| DURATIONHOUR | int |  | YES | ((0)) |
| DURATIONMINUTES | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ServiceLocation
**Physical table:** `OSUSR_591_SERVICELOCATION`  
**Description:** Locations where the service will be provided  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SERVICEID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| EXTERNALID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SHOWINSIMPLESIGNIN | bit |  | YES | ((0)) |

## ServiceMembership
**Physical table:** `OSUSR_591_SERVICEMEMBERSHIP`  
**Description:** Stores the relatioships between services and member plan templates  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SERVICEID | bigint |  | YES | (NULL) |
| MEMBERPLANTEMPLATEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXTERNALID | bigint |  | YES | ((0)) |
| SERVICEDURATIONID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ServiceProvider
**Physical table:** `OSUSR_591_SERVICEPROVIDER`  
**Description:** Provider of a service in a location  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SERVICELOCATIONID | bigint |  | YES | (NULL) |
| PROVIDERID | int |  | YES | (NULL) |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| EXTERNALID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ServiceProviderEmail
**Physical table:** `OSUSR_591_SERVICEPROVIDEREMAIL`  
**Description:** Table to hold information about the sent emails  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SERVICEID | bigint |  | YES | (NULL) |
| CLIENTID | int |  | YES | (NULL) |
| SERVICEPROVIDERID | bigint |  | YES | (NULL) |
| MEMBERPLANID | int |  | YES | (NULL) |
| HASSENTFOLLOWUPEMAIL | bit |  | YES | ((0)) |
| LOCATIONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| LEADID | int |  | YES | (NULL) |
| EXTERNALID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ServiceWaiver
**Physical table:** `OSUSR_591_SERVICEWAIVER`  
**Description:** Stores the waivers associated with the service  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| SERVICEID | bigint |  | YES | (NULL) |
| WAIVERID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| EXTERNALID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
