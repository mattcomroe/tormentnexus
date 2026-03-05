# PlatformCenter

## Tables

- [Environment](#environment)
- [IntegrationType](#integrationtype)
- [MenuItem](#menuitem)

## Environment
**Physical table:** `OSUSR_29q_Environment1`  
**Description:** Contains a record per needed environment  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## IntegrationType
**Physical table:** `OSUSR_29q_IntegrationType`  
**Description:** Used to distinguish Web Services from Rests  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## MenuItem
**Physical table:** `OSUSR_29q_MenuItem1`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CAPTION | nvarchar | 50 | YES | ('') |
