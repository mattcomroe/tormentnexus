# Firestore_AP

## Tables

- [ComponentsUpdateCompleteInFirestore](#componentsupdatecompleteinfirestore)
- [DeltaComponentsUpdateCompleteInFirestore](#deltacomponentsupdatecompleteinfirestore)
- [FirestoreIsDeletedGlobalUserIdLastProcessed_DEV](#firestoreisdeletedglobaluseridlastprocessed-dev)

## ComponentsUpdateCompleteInFirestore
**Physical table:** `OSUSR_chm_GlobalUserComponentsUpdated_InFirestore`  
**Description:** Temp table used during the Component Update timer, used to update Component details for all GlobalUsers for a Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| GLOBALUSERID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDBYSYSTEM | nvarchar | 50 | YES | ('') |

## DeltaComponentsUpdateCompleteInFirestore
**Physical table:** `OSUSR_chm_DeltaComponentsUpdateCompleteInFirestore`  
**Description:** Temp table used during the Component Update timer, used to update Component details for all GlobalUsers for a Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | ((0)) |
| CREATEDBYSYSTEM | nvarchar | 50 | YES | ('') |

## FirestoreIsDeletedGlobalUserIdLastProcessed_DEV
**Physical table:** `OSUSR_chm_FirestorePerformanceResultIsDeleted_DEV`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID_LASTPROCESSED | bigint |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
