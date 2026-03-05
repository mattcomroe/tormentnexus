# WorldTimezone_LS

## Tables

- [TIMEZONE](#timezone)
- [TZ_Database_Mapping](#tz-database-mapping)

## TIMEZONE
**Physical table:** `OSUSR_9ke_TIMEZONE`  
**Description:** Contains all timezones provided by Windows servers that are in the windows registry. check the list here: https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones?view=windows-11  Abbreviation list here: https://www.ge.com/digital/documentation/workflow/r_wf_time_zone_abbreviations_for_date_and_time_functions.html  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CODE | nvarchar | 50 | YES | ('') |
| NAME | nvarchar | 100 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| WORKATO | nvarchar | 50 | YES | ('') |
| ABBREVIATION | nvarchar | 50 | YES | ('') |

## TZ_Database_Mapping
**Physical table:** `OSUSR_9ke_TZ_Database_Mapping`  
**Description:** Entity that has the mapping between the timezone from tz database in format area/location and the Id in Wodify  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TZ_NAME | nvarchar | 100 | YES | ('') |
| TIMEZONEID | int |  | YES | (NULL) |
