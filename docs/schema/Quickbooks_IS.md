# Quickbooks_IS

## Tables

- [OAuth2](#oauth2)

## OAuth2
**Physical table:** `OSUSR_azf_OAuth2`  
**Description:** Contains data to integrate the customer with quickbooks  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| AUTHORIZATIONCODE | nvarchar | 50 | YES | ('') |
| REALMID | nvarchar | 50 | YES | ('') |
| STATE | nvarchar | 50 | YES | ('') |
| TOKEN_TYPE | nvarchar | 50 | YES | ('') |
| EXPIRESIN | bigint |  | YES | ((0)) |
| EXPIRATIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| REFRESHTOKEN | nvarchar | 150 | YES | ('') |
| XREFRESHTOKENEXPIRESIN | bigint |  | YES | ((0)) |
| REFRESHEXPIRATIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ACCESSTOKEN | nvarchar | 1000 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
