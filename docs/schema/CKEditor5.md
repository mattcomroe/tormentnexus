# CKEditor5

## Tables

- [CKFileType](#ckfiletype)
- [PasteType](#pastetype)

## CKFileType
**Physical table:** `OSUSR_a21_CKFileType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PasteType
**Physical table:** `OSUSR_a21_PasteType`  
**Description:** Defines the pasting type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
