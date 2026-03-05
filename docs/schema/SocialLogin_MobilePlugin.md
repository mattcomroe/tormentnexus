# SocialLogin_MobilePlugin

## Tables

- [Authentication](#authentication)
- [Provider](#provider)

## Authentication
**Physical table:** `OSUSR_7p2_Authentication1`  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## Provider
**Physical table:** `OSUSR_7p2_Provider1`  
**Description:** Holds static information about the available social login providers.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
