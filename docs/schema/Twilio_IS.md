# Twilio_IS

## Tables

- [PhoneNumberVerificationStatus](#phonenumberverificationstatus)
- [TwilioBlacklistWords](#twilioblacklistwords)

## PhoneNumberVerificationStatus
**Physical table:** `OSUSR_366_PhoneNumberVerificationStatus`  
**Description:** Static record of different status states during the SMS Toll free phone number verification process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TwilioBlacklistWords
**Physical table:** `OSUSR_366_TwilioBlacklistWords`  
**Description:** Twilio Blacklisted Words  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WORD | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
