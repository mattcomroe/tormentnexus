# SocialLoginMobilePlugin

## Tables

- [Authentication](#authentication)
- [Provider](#provider)

## Authentication
**Physical table:** `OSUSR_dpt_Authentication2`  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## Provider
**Physical table:** `OSUSR_dpt_Provider2`  
**Description:** Holds static information about the available social login providers.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
