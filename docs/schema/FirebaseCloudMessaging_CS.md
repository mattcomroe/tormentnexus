# FirebaseCloudMessaging_CS

## Tables

- [FirebaseUserTokens](#firebaseusertokens)

## FirebaseUserTokens
**Physical table:** `OSUSR_5c8_FirebaseUserTokens`  
**Description:** The FirebaseUserTokens table is specifically designed to manage Firebase Cloud Messaging (FCM) registration tokens, which are crucial for sending notifications to user devices efficiently. This table not only stores the FCM tokens but also tracks their validity and relevance over time, aligning with best practices for token management to ensure effective communication and resource utilization.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| FCMTOKEN | nvarchar | 1024 | YES | ('') |
| TOKENTIMESTAMP | datetime |  | YES | ('1900-01-01 00:00:00') |
| HARDWAREID | nvarchar | 50 | YES | ('') |
| PLATFORMID | nvarchar | 50 | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| APPLICATIONID | bigint |  | YES | ((0)) |
| APPLICATIONNAME | nvarchar | 256 | YES | ('') |
