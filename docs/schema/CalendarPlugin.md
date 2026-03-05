# CalendarPlugin

## Tables

- [Recurrence](#recurrence)

## Recurrence
**Physical table:** `OSUSR_95v_Recurrence`  
**Description:** Defines the available recurrence periods for calendar events.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
