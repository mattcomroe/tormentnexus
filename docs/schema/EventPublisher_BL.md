# EventPublisher_BL

## Tables

- [CUDAction_DeleteMe](#cudaction-deleteme)

## CUDAction_DeleteMe
**Physical table:** `OSUSR_78F_CUDACTION`  
**Description:** Create, Update, or Delete labels to be used when building Event JSON.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
