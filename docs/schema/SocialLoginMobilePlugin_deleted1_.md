# SocialLoginMobilePlugin(deleted1)

## Tables

- [Authentication](#authentication)
- [Provider](#provider)

## Authentication
**Physical table:** `OSUSR_dpt_Authentication1`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Provider
**Physical table:** `OSUSR_dpt_Provider1`  
**Description:** Holds static information about the available social login providers.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
