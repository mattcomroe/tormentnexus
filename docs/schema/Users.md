# Users

## Tables

- [AuditType](#audittype)
- [AuditUserOperation](#audituseroperation)
- [AuthenticationMethod](#authenticationmethod)
- [Config_UserMappings](#config-usermappings)
- [ConfigFile](#configfile)
- [ConfigFileBinary](#configfilebinary)
- [ConfigIdP](#configidp)
- [ConfigInternal](#configinternal)
- [ConfigSP](#configsp)
- [HelpIdMapping](#helpidmapping)
- [LdapAuthenticationType](#ldapauthenticationtype)
- [LoginAttempt](#loginattempt)
- [LoginAttemptResult](#loginattemptresult)
- [MenuItem](#menuitem)
- [MobileToken](#mobiletoken)
- [NameIdFormat](#nameidformat)
- [SamlMessage_Log](#samlmessage-log)
- [SamlMessageBinding](#samlmessagebinding)
- [SamlMessageRawContent_Log](#samlmessagerawcontent-log)
- [SamlMessageType](#samlmessagetype)
- [SamlUser](#samluser)
- [UserSession](#usersession)
- [UserSessionClaims](#usersessionclaims)
- [XmlValueType](#xmlvaluetype)

## AuditType
**Physical table:** `OSUSR_6wd_AuditType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |

## AuditUserOperation
**Physical table:** `OSUSR_6wd_AuditUserOperation`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |

## AuthenticationMethod
**Physical table:** `OSUSR_6wd_AuthenticationMethod`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| SUPPORTEDINJ2EE | bit |  | YES | ((0)) |

## Config_UserMappings
**Physical table:** `OSUSR_6wd_Config_UserMappings`  
**Description:** Assertion Claims mapping  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | bigint |  | NO |  |
| NAME_ATTRIBUTE | nvarchar | 250 | YES | ('') |
| NAME_SPLITCHR | nvarchar | 1 | YES | ('') |
| NAME_INDEX | int |  | YES | ((0)) |
| SURNAME_ATTRIBUTE | nvarchar | 250 | YES | ('') |
| SURNAME_SPLITCHR | nvarchar | 1 | YES | ('') |
| SURNAME_INDEX | int |  | YES | ((0)) |
| EMAIL_ATTRIBUTE | nvarchar | 250 | YES | ('') |
| EMAIL_SPLITCHR | nvarchar | 1 | YES | ('') |
| EMAIL_INDEX | int |  | YES | ((0)) |
| USERNAME_ATTRIBUTE | nvarchar | 250 | YES | ('') |
| USERNAME_SPLITCHR | nvarchar | 1 | YES | ('') |
| USERNAME_INDEX | int |  | YES | ((0)) |
| MOBILENUMBER_ATTRIBUTE | nvarchar | 250 | YES | ('') |
| MOBILENUMBER_SPLITCHR | nvarchar | 1 | YES | ('') |
| MOBILENUMBER_INDEX | int |  | YES | ((0)) |
| EXTERNALID_ATTRIBUTE | nvarchar | 250 | YES | ('') |
| EXTERNALID_SPLITCHR | nvarchar | 1 | YES | ('') |
| EXTERNALID_INDEX | int |  | YES | ((0)) |
| IDP_ATTRIBUTEGROUPNAME | nvarchar | 500 | YES | ('') |
| GROUPNAMESPLITCHR | nvarchar | 1 | YES | ('') |

## ConfigFile
**Physical table:** `OSUSR_6wd_CfgFile`  
**Description:** Holds the KeyStore and Certificates files  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | int |  | NO |  |
| FILENAME | nvarchar | 128 | YES | ('') |
| MIMETYPE | nvarchar | 150 | YES | ('') |
| SIZE | int |  | YES | ((0)) |
| FILEPASSWD | nvarchar | 200 | YES | ('') |
| TYPE | nvarchar | 50 | YES | ('') |

## ConfigFileBinary
**Physical table:** `OSUSR_6wd_CfgFBin`  
**Description:** Binary data of each Config_File entry  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | int |  | NO |  |
| CONTENT | varbinary | -1 | YES | (NULL) |

## ConfigIdP
**Physical table:** `OSUSR_6wd_CfgIdP`  
**Description:** Holds the SSO server configuration  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | bigint |  | NO |  |
| IDPISSUER | nvarchar | 500 | YES | ('') |
| SSOURL | nvarchar | 512 | YES | ('') |
| SLOURL | nvarchar | 512 | YES | ('') |
| WANTSIGNAUTHN | bit |  | YES | ((0)) |
| SLORESPONSEURL | nvarchar | 512 | YES | ('') |
| SLOSOAPURL | nvarchar | 512 | YES | ('') |
| ISOSIDPSERVER | bit |  | YES | ((0)) |
| IDPCERTIFICATEID | int |  | YES | (NULL) |
| SSOURLBINDINGID | int |  | YES | (NULL) |
| SINGLELOGOUTBINDINGID | int |  | YES | (NULL) |
| HMAC | nvarchar | 150 | YES | ('') |
| HMACVERSION | nvarchar | 150 | YES | ('') |

## ConfigInternal
**Physical table:** `OSUSR_6wd_CfgIntrn`  
**Description:** Holds internal configurations of the IdP component  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | bigint |  | NO |  |
| LOGINDEFAULTRETURNURL | nvarchar | 500 | YES | ('') |
| LOGOUTDEFAULTRETURNURL | nvarchar | 500 | YES | ('') |
| SAML_MESSAGESALLOWREPEATEDID | bit |  | YES | ((0)) |
| PUBLICURL | nvarchar | 500 | YES | ('') |
| INTERNALURL | nvarchar | 500 | YES | ('') |
| AUTOUSERPROVISION | bit |  | YES | ((0)) |
| ALLOWIDPSRVINITIATEDLOGIN | bit |  | YES | ((0)) |
| ONBOARDINGGROUPID | int |  | YES | (NULL) |
| HMAC | nvarchar | 150 | YES | ('') |
| HMACVERSION | nvarchar | 150 | YES | ('') |

## ConfigSP
**Physical table:** `OSUSR_6wd_CfgSP`  
**Description:** Holds the configuration of the SP connector  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | bigint |  | NO |  |
| SPISSUER | nvarchar | 250 | YES | ('') |
| SPRELAYSTATE | nvarchar | 250 | YES | ('') |
| ONLYACCEPTENCRYPTEDASSERTION | bit |  | YES | ((0)) |
| ACCEPTUNSIGNEDLOGOUTRESPONSE | bit |  | YES | ((0)) |
| KEYSTOREAUTOGENERATED | bit |  | YES | ((0)) |
| REDIRECTRELAYSTATE | bit |  | YES | ((0)) |
| SERVICEDISPLAYNAME | nvarchar | 250 | YES | ('') |
| KEYSTOREID | int |  | YES | (NULL) |
| SETACSONAUTHNREQ | bit |  | YES | ((0)) |
| SETDESTINATIONONAUTHNREQ | bit |  | YES | ((0)) |
| CONTACT_COMPANY | nvarchar | 50 | YES | ('') |
| CONTACT_GIVENNAME | nvarchar | 50 | YES | ('') |
| CONTACT_SURNAME | nvarchar | 50 | YES | ('') |
| CONTACT_EMAILADDRESS | nvarchar | 250 | YES | ('') |
| CONTACT_TELEPHONENUMBER | nvarchar | 20 | YES | ('') |
| SPMETADATAENTRYID | nvarchar | 50 | YES | ('') |
| USERMAPPINGID | bigint |  | YES | (NULL) |
| PROVIDERID | int |  | YES | (NULL) |
| HMAC | nvarchar | 150 | YES | ('') |
| HMACVERSION | nvarchar | 150 | YES | ('') |
| ONLYACCEPTSIGNEDLOGINRESP | bit |  | YES | ((0)) |
| NAMEIDFORMATID | nvarchar | 150 | YES | (NULL) |

## HelpIdMapping
**Physical table:** `OSUSR_6wd_HelpIdMapping1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| HELPID | int |  | YES | ((0)) |
| LABEL | nvarchar | 50 | YES | ('') |

## LdapAuthenticationType
**Physical table:** `OSUSR_6wd_LdapAuthenticationType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## LoginAttempt
**Physical table:** `OSUSR_6wd_LoginAttempt`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | bigint |  | YES | ((0)) |
| USERNAME | nvarchar | 250 | YES | ('') |
| INSTANT | datetime |  | YES | ('1900-01-01 00:00:00') |
| SUCCESS | bit |  | YES | ((0)) |
| IPADDRESS | nvarchar | 45 | YES | ('') |
| USERNAMEFAILURECOUNT | int |  | YES | ((0)) |
| IPADDRESSFAILURECOUNT | int |  | YES | ((0)) |
| REQUESTKEY | nvarchar | 36 | YES | ('') |
| USERAGENT | nvarchar | 250 | YES | ('') |
| VISITOR | nvarchar | 36 | YES | ('') |
| RESULT | nvarchar | 50 | YES | (NULL) |

## LoginAttemptResult
**Physical table:** `OSUSR_6wd_LoginAttemptResult`  
**Description:** The alternative values that may appear in the LoginAttempt record Result column.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |

## MenuItem
**Physical table:** `OSUSR_6wd_MenuItem`  
**Description:** Menu item to be used in menu web block parameters.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## MobileToken
**Physical table:** `OSUSR_6wd_MobileToken`  
**Description:** Tokens for Mobile Logins  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | bigint |  | NO |  |
| TOKEN | nvarchar | 50 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SESSIONINDEX | nvarchar | 2000 | YES | ('') |
| NAMEID | nvarchar | 50 | YES | ('') |
| MODULE | nvarchar | 50 | YES | ('') |
| SCREEN | nvarchar | 50 | YES | ('') |

## NameIdFormat
**Physical table:** `OSUSR_6wd_NameIdFormat`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| URI | nvarchar | 150 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## SamlMessage_Log
**Physical table:** `OSUSR_6wd_SamlMessage_Log`  
**Description:** Holds all the messages sent from / to the IdP component  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | bigint |  | NO |  |
| MESSAGEID | nvarchar | 2000 | YES | ('') |
| RESPONSETOMESSAGEID | nvarchar | 2000 | YES | ('') |
| USERNAME | nvarchar | 250 | YES | ('') |
| SESSIONINDEX | nvarchar | 2000 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| IPADDRESS | nvarchar | 50 | YES | ('') |
| RELATEDURL | nvarchar | 500 | YES | ('') |
| IDPISSUER | nvarchar | 250 | YES | ('') |
| SPISSUER | nvarchar | 250 | YES | ('') |
| VALID | bit |  | YES | ((0)) |
| NOTVALIDERROR | nvarchar | -1 | YES | ('') |
| INCOMINGMSG | bit |  | YES | ((0)) |
| SAMLMESSAGETYPEID | int |  | YES | (NULL) |
| SAMLMESSAGEBINDINGID | int |  | YES | (NULL) |
| FROMMOBILE | bit |  | YES | ((0)) |
| METADATA | nvarchar | 1500 | YES | ('') |

## SamlMessageBinding
**Physical table:** `OSUSR_6wd_SamlMessageBinding`  
**Description:** SAML bindings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## SamlMessageRawContent_Log
**Physical table:** `OSUSR_6wd_SamlMessageRawContent_Log`  
**Description:** Holds the SAML xml message itself of each SamlMessage_Log  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| SAMLMESSAGE_LOGID | bigint |  | NO |  |
| RAWMESSAGE | varbinary | -1 | YES | (NULL) |

## SamlMessageType
**Physical table:** `OSUSR_6wd_SamlMessageType`  
**Description:** SAML message types  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## SamlUser
**Physical table:** `OSUSR_6wd_SamlUser`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| USERID | int |  | NO |  |
| SAMLEXTERNALID | nvarchar | 250 | YES | ('') |

## UserSession
**Physical table:** `OSUSR_6wd_UserSession`  
**Description:** Holds the list SAML sessions, ie, timestamp of each login on the IdP component  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| ID | bigint |  | NO |  |
| SESSIONKEY | nvarchar | 250 | YES | ('') |
| MOBILESESSIONKEY | nvarchar | 2000 | YES | ('') |
| SAMLSESSIONINDEX | nvarchar | 2000 | YES | ('') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| USERID | int |  | YES | (NULL) |
| ACTIVE | bit |  | YES | ((0)) |
| FROMMOBILE | bit |  | YES | ((0)) |
| MOBILESPKEY | nvarchar | 200 | YES | ('') |
| HASHEDSESSIONINDEX | nvarchar | 2000 | YES | ('') |
| HASHEDSESSIONKEY | nvarchar | 1000 | YES | ('') |

## UserSessionClaims
**Physical table:** `OSUSR_6wd_UserSessionClaims`  
**Description:** List os claims present in the SAML assertion for each UserSession  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | NO | ((0)) |
| USERSESSIONID | bigint |  | NO |  |
| CLAIMS | varbinary | -1 | YES | (NULL) |

## XmlValueType
**Physical table:** `OSUSR_6wd_XmlValueType`  
**Description:** List of XML types values  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
