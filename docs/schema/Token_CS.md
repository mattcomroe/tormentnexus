# Token_CS

## Tables

- [Token](#token)
- [TokenType](#tokentype)

## Token
**Physical table:** `OSUSR_063_TOKEN`  
**Description:** A token represents a signed piece of data used to verify it was sent by our servers  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 36 | NO |  |
| TOKENTYPEID | int |  | YES | (NULL) |
| PAYLOAD | nvarchar | 1000 | YES | ('') |
| CREATEDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXPIRATIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISONETIMEUSE | bit |  | YES | ((0)) |

## TokenType
**Physical table:** `OSUSR_063_TOKENTYPE`  
**Description:** A type of token that can be generated with this service  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
