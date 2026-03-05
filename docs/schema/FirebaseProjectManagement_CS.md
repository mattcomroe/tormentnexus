# FirebaseProjectManagement_CS

## Tables

- [BinaryType](#binarytype)
- [FirebaseServiceAccount](#firebaseserviceaccount)
- [FirebaseServiceAccount_Extension](#firebaseserviceaccount-extension)

## BinaryType
**Physical table:** `OSUSR_9WL_PROJECTTYPE`  
**Description:** Type of the binary, service account for example is used for the firebase service account  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## FirebaseServiceAccount
**Physical table:** `OSUSR_9WL_FIREBASESERVICEACCOUNT`  
**Description:** This holds the firebase project/binaryfk and sender id which is used to connect with firebase  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PROJECTID | nvarchar | 50 | YES | ('') |
| PROJECTTYPEID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| BINARYTYPEID | int |  | YES | (NULL) |
| SENDERID | nvarchar | 50 | YES | ('') |

## FirebaseServiceAccount_Extension
**Physical table:** `OSUSR_9WL_FIREBASESERVICEACCOUNT_EXTENSION`  
**Description:** Extension meant to hold the binary separate from the main query table  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| FIREBASESERVICEACCOUNTID | int |  | NO |  |
| BINARY | varbinary | -1 | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
