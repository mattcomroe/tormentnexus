# FirebaseMiddleware

## Tables

- [Device](#device)
- [DevicePlatform](#deviceplatform)

## Device
**Physical table:** `OSUSR_VBW_DEVICE1`  
**Description:** Holds information about all registered devices that are capable of received notifications.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| HARDWAREID | nvarchar | 50 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| REGISTRATIONID | nvarchar | 1024 | YES | ('') |
| DEVICEPLATFORMID | int |  | YES | (NULL) |
| APPLICATIONID | nvarchar | 256 | YES | ('') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## DevicePlatform
**Physical table:** `OSUSR_VBW_DEVICEPLATFORM1`  
**Description:** Device platform  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 10 | YES | ('') |
