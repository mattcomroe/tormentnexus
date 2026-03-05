# Sandbox_Paulo

## Tables

- [DatePickerProvider](#datepickerprovider)
- [LogType](#logtype)
- [RegisteredCallbackEvents](#registeredcallbackevents)

## DatePickerProvider
**Physical table:** `OSUSR_NZX_DATEPICKERPROVIDER`  
**Description:** Used to store the provider name.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| PROVIDER | nvarchar | 50 | NO |  |

## LogType
**Physical table:** `OSUSR_NZX_LOGTYPE`  
**Description:** Type of the log being recorded.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## RegisteredCallbackEvents
**Physical table:** `OSUSR_NZX_REGISTEREDCALLBACKEVENTS`  
**Description:** Define all the registered callback event names.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| NAME | nvarchar | 100 | NO |  |
