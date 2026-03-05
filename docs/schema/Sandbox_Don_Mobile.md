# Sandbox_Don_Mobile

## Tables

- [ConfigurationRecord](#configurationrecord)
- [DataType](#datatype)
- [EmailMessageJSONType](#emailmessagejsontype)
- [FirebaseStructureType](#firebasestructuretype)

## ConfigurationRecord
**Physical table:** `OSUSR_wxu_ConfigurationRecord1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| IS_ACTIVE | bit |  | YES | ((0)) |
| DATATYPEID | int |  | YES | (NULL) |
| LABEL | nvarchar | 50 | YES | ('') |
| STRUCTURENAME | nvarchar | 50 | YES | ('') |

## DataType
**Physical table:** `OSUSR_wxu_DataType1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## EmailMessageJSONType
**Physical table:** `OSUSR_wxu_EmailMessageJSONType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## FirebaseStructureType
**Physical table:** `OSUSR_wxu_FirebaseStructureType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
