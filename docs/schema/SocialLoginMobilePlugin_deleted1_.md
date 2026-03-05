# SocialLoginMobilePlugin(deleted1)

## Tables

- [Authentication](#authentication)
- [Provider](#provider)

## Authentication
**Physical table:** `OSUSR_DPT_AUTHENTICATION1`  

_Column definitions not found in schema export._

## Provider
**Physical table:** `OSUSR_DPT_PROVIDER1`  
**Description:** Holds static information about the available social login providers.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
