# CoreAccountEmailConfirm_CS(deleted0)

## Tables

- [EmailConfirmation](#emailconfirmation)
- [EmailConfirmationStatus](#emailconfirmationstatus)
- [WelcomeEmailQueue](#welcomeemailqueue)

## EmailConfirmation
**Physical table:** `OSUSR_BG5_EMAILCONFIRMATION`  
**Description:** Auxiliary information for an email confirmation process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |
| TENANTID | int |  | YES |  |
| EMAILTOCONFIRM | nvarchar | 250 | YES | ('') |
| SENDEMAIL | bit |  | YES | ((0)) |
| CONFIRMATIONSCREENTOKEN | nvarchar | 30 | YES | ('') |
| EMAILCONFIRMATIONSTATUSID | int |  | YES | (NULL) |
| ISFORNEWUSER | bit |  | YES | ((0)) |
| ISFORPASSWORDRECOVERY | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLOSEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISFROMBLUEPRINTLOGIN | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| EPAPPLICATIONSOURCEID | bigint |  | YES | ((0)) |

## EmailConfirmationStatus
**Physical table:** `OSUSR_BG5_EMAILCONFIRMATIONSTATUS`  
**Description:** Status of an email confirmation  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## WelcomeEmailQueue
**Physical table:** `OSUSR_BG5_WELCOMEEMAILQUEUE`  
**Description:** Creating a record on this table will launch a BPT that sends a welcome email. The only reason the mail isn't send directly from this eSpace is because it would cause circular references.  We do this in the (very uncommon) situation where a welcome email for a Customer is sent while the confirmation process for a different Customer is still running. This allows us to send a differnet Welcome Email contianing the existing ConfirmationToken.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| CONFIRMATIONSCREENTOKEN | nvarchar | 30 | YES | ('') |
| EMAILADDRESS | nvarchar | 250 | YES | ('') |
| ISCOMPLETE | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
