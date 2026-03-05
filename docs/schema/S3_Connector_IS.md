# S3_Connector_IS

## Tables

- [BucketType](#buckettype)
- [S3_Action](#s3-action)
- [UrlType](#urltype)

## BucketType
**Physical table:** `OSUSR_166_BUCKETTYPE`  
**Description:** S3 Buckets available  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| SITEPROPERTYBUCKETNAME | nvarchar | 50 | YES | ('') |
| ISGLOBAL | bit |  | YES | ((0)) |

## S3_Action
**Physical table:** `OSUSR_166_S3_ACTION`  
**Description:** The available actions to be performed on the S3 API.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |

## UrlType
**Physical table:** `OSUSR_166_URLTYPE`  
**Description:** Defines the type of bucket we want to access  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
