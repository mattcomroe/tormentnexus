# NativeAppBuilder

## Tables

- [DismissedErrorsOrInfo](#dismissederrorsorinfo)
- [ErrorInfoType](#errorinfotype)
- [ErrorsAndInfo](#errorsandinfo)

## DismissedErrorsOrInfo
**Physical table:** `OSUSR_jce_DismissedErrorsOrInfo`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ERRORSANDINFOID | bigint |  | YES | (NULL) |
| USERNAME | nvarchar | 50 | YES | ('') |

## ErrorInfoType
**Physical table:** `OSUSR_jce_ErrorInfoType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ErrorsAndInfo
**Physical table:** `OSUSR_jce_ErrorsAndInfo`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ERRORINFOTYPE | int |  | YES | (NULL) |
| ERRORMESSAGE | nvarchar | 512 | YES | ('') |
| APPKEY | nvarchar | 50 | YES | ('') |
| BUILDID | int |  | YES | ((0)) |
| CODE | nvarchar | 50 | YES | ('') |
