# MicrosoftLoginConnectorCore(deleted0)

## Tables

- [B2CUser](#b2cuser)
- [OAuth2Application](#oauth2application)
- [OAuth2ApplicationAdvanced](#oauth2applicationadvanced)
- [OAuth2ApplicationB2C](#oauth2applicationb2c)
- [OAuth2ApplicationEspace](#oauth2applicationespace)
- [OAuth2ApplicationResources](#oauth2applicationresources)
- [OAuth2ApplicationRole](#oauth2applicationrole)
- [OAuth2Resource](#oauth2resource)
- [OAuthProvider](#oauthprovider)
- [TokenRequest](#tokenrequest)

## B2CUser
**Physical table:** `OSUSR_1R1_B2CUSER1`  
**Description:** The entitie will keep track of what OutSystems user is a Azure AD B2C user. It could be important to keep track of this. The entites events are also exposed so you could start an enrollment process or something like that if needed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| B2COID | nvarchar | 50 | YES | ('') |
| OAUTH2APPLICATIONID | bigint |  | YES | (NULL) |

## OAuth2Application
**Physical table:** `OSUSR_1R1_OAUTH2APPLICATION1`  
**Description:** Stores the Azure AD application data  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DESCRIPTION | nvarchar | 50 | YES | ('') |
| OAUTHPROVIDERID | int |  | YES | (NULL) |
| TENANTID | nvarchar | 50 | YES | ('') |
| CLIENTID | nvarchar | 50 | YES | ('') |
| CLIENTSECRET | nvarchar | 50 | YES | ('') |
| SCOPE | nvarchar | 50 | YES | ('') |
| ISAZUREADROLESYNC | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## OAuth2ApplicationAdvanced
**Physical table:** `OSUSR_1R1_OAUTH2APPLICATIONADVANCED1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| OAUTH2APPLICATIONID | bigint |  | YES | (NULL) |
| ISCREATEOSACCOUNTIFNOTEXIST | bit |  | YES | ((0)) |

## OAuth2ApplicationB2C
**Physical table:** `OSUSR_1R1_OAUTH2APPLICATIONB2C1`  
**Description:** Stores data needed to login to a Azure AD B2C tenant  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANTNAME | nvarchar | 27 | YES | ('') |
| POLICYNAME | nvarchar | 50 | YES | ('') |

## OAuth2ApplicationEspace
**Physical table:** `OSUSR_1R1_OAUTH2APPLICATIONESPACE1`  
**Description:** Reference table to link OAuth applications with Espace that are allowed to use these applications  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| OAUTH2APPLICATIONID | bigint |  | YES | (NULL) |
| ESPACEID | int |  | YES | (NULL) |

## OAuth2ApplicationResources
**Physical table:** `OSUSR_1R1_OAUTH2APPLICATIONRESOURCES1`  
**Description:** Reference table to link OAuth applications with Rersouces of which a token can be requested  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| OAUTH2APPLICATIONID | bigint |  | YES | (NULL) |
| OAUTH2RESOURCEID | bigint |  | YES | (NULL) |
| ISDEFAULT | bit |  | YES | ((0)) |

## OAuth2ApplicationRole
**Physical table:** `OSUSR_1R1_OAUTH2APPLICATIONROLE1`  
**Description:** Reference table to link OAuth applications with an OutSytems Role. This is used for token based assignment of Roles  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| OAUTH2APPLICATIONID | bigint |  | YES | (NULL) |
| ROLEID | int |  | YES | (NULL) |

## OAuth2Resource
**Physical table:** `OSUSR_1R1_OAUTH2RESOURCE1`  
**Description:** Stores an Azure AD Application resource of which tokens can be retrieved  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DESCRIPTION | nvarchar | 50 | YES | ('') |
| RESOURCE | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |

## OAuthProvider
**Physical table:** `OSUSR_1R1_OAUTHPROVIDER1`  
**Description:** Indicates what type of OAuth provider is used  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TokenRequest
**Physical table:** `OSUSR_1R1_TOKENREQUEST1`  
**Description:** Azure Token info for Azure Requests  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| EMAIL | nvarchar | 250 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| ENTRYURL | nvarchar | 1000 | YES | ('') |
| STATEGUID | nvarchar | 250 | YES | ('') |
| ACCESS_TOKEN | nvarchar | -1 | YES | ('') |
| TOKEN_TYPE | nvarchar | 1999 | YES | ('') |
| RESOURCE | nvarchar | 2000 | YES | ('') |
| SCOPE | nvarchar | -1 | YES | ('') |
| CLIENTID | nvarchar | 400 | YES | ('') |
| REFRESH_TOKEN | nvarchar | 1999 | YES | ('') |
| ID_TOKEN | nvarchar | 1999 | YES | ('') |
| EXPIRESON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXPIRESIN | int |  | YES | ((0)) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ROLES | nvarchar | 1000 | YES | ('') |
| SYNCROLES | bit |  | YES | ((0)) |
| CALLBACKURL | nvarchar | 1000 | YES | ('') |
