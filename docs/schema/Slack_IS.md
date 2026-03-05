# Slack_IS

## Tables

- [SlackAccessTokens](#slackaccesstokens)

## SlackAccessTokens
**Physical table:** `OSUSR_9V3_SLACKACCESSTOKENS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TENANTID | int |  | YES | (NULL) |
| ACCESSTOKEN | nvarchar | 100 | YES | ('') |
| CREATEDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | ((0)) |
