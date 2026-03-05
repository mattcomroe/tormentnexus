# Timers_CS

## Tables

- [CustomerTimer](#customertimer)
- [Timer](#timer)
- [TimerScheduleType](#timerscheduletype)

## CustomerTimer
**Physical table:** `OSUSR_vhb_TenantTimer`  
**Description:** This table holds a reference to a timer for a given customer. It tells the date/time that the timer last ran for the customer.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TIMERID | int |  | YES | (NULL) |
| LASTRUNDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ERRORMESSAGE | nvarchar | 1500 | YES | ('') |
| CUSTOMERID | bigint |  | YES | ((0)) |
| LASTFINISHEDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |

## Timer
**Physical table:** `OSUSR_vhb_Timer`  
**Description:** A static entity that holds timer records.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| HOUROFDAY | int |  | YES | ((0)) |
| TIMERSCHEDULETYPEID | int |  | YES | (NULL) |

## TimerScheduleType
**Physical table:** `OSUSR_vhb_TimerScheduleType`  
**Description:** The type of schedule that a timer can have.  If a timer should run only once a day, every day, for a given Customer, choose "Hourly".  If a timer should run once a day, in a specific day of the week or month, choose "Daily".  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
