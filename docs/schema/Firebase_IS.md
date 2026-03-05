# Firebase_IS

## Tables

- [FirestoreCollection](#firestorecollection)
- [FirestoreCUDType](#firestorecudtype)
- [FirestoreField](#firestorefield)

## FirestoreCollection
**Physical table:** `OSUSR_WCK_FIRESTORECOLLECTION`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## FirestoreCUDType
**Physical table:** `OSUSR_WCK_FIRESTORECUDTYPE`  
**Description:** Firestore write action types for Create, Update, and Delete  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## FirestoreField
**Physical table:** `OSUSR_WCK_FIRESTOREFIELD`  
**Description:** Contains names of fields in Firestore for use when specific attribute access is needed  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
