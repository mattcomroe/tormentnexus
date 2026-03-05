# SocialLoginConfigurator

## Tables

- [AppleUserInfo](#appleuserinfo)
- [ApplicationConfiguration](#applicationconfiguration)
- [ApplicationType](#applicationtype)
- [AuthenticationConfiguration](#authenticationconfiguration)
- [AuthenticationDetail](#authenticationdetail)
- [Provider](#provider)

## AppleUserInfo
**Physical table:** `OSUSR_QGT_APPLEUSERINFO`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 250 | NO |  |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |

## ApplicationConfiguration
**Physical table:** `OSUSR_QGT_APPLICATIONCONFIGURATION`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| APPLICATIONID | int |  | YES | (NULL) |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| HASAPPLE | bit |  | YES | ((0)) |
| HASFACEBOOK | bit |  | YES | ((0)) |
| HASGOOGLE | bit |  | YES | ((0)) |
| HASLINKEDIN | bit |  | YES | ((0)) |

## ApplicationType
**Physical table:** `OSUSR_QGT_APPLICATIONTYPE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## AuthenticationConfiguration
**Physical table:** `OSUSR_QGT_AUTHENTICATIONCONFIGURATION`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROVIDERID | int |  | YES | (NULL) |
| CLIENTID | nvarchar | 100 | YES | ('') |
| CLIENTSECRET | nvarchar | 500 | YES | ('') |
| TEAMID | nvarchar | 50 | YES | ('') |
| KEYID | nvarchar | 50 | YES | ('') |
| APPLICATIONNAME | nvarchar | 50 | YES | ('') |
| APPLICATIONTYPEID | int |  | YES | (NULL) |
| CLIENTTOKEN | nvarchar | 100 | YES | ('') |
| URLSCHEME | nvarchar | 100 | YES | ('') |
| APPLICATIONCONFIGURATIONID | bigint |  | YES | (NULL) |
| ISIOSCONFIGURED | bit |  | YES | ((0)) |
| ISWEBCONFIGURED | bit |  | YES | ((0)) |
| ISENABLED | bit |  | YES | ((0)) |

## AuthenticationDetail
**Physical table:** `OSUSR_QGT_AUTHENTICATIONDETAIL`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| PROVIDERID | int |  | YES | (NULL) |
| CLIENTID | nvarchar | 100 | YES | ('') |
| REDIRECTURI | nvarchar | 500 | YES | ('') |
| RETURNURI | nvarchar | 500 | YES | ('') |
| STATE | nvarchar | 500 | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Provider
**Physical table:** `OSUSR_QGT_PROVIDER`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
