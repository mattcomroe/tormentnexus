# ZXingServices

## Tables

- [AuthenticationType](#authenticationtype)
- [CardType](#cardtype)
- [Code](#code)
- [Encoding](#encoding)
- [ErrorCorrectionLevel](#errorcorrectionlevel)
- [ImageFormat](#imageformat)
- [PhoneType](#phonetype)

## AuthenticationType
**Physical table:** `OSUSR_89Z_AUTHENTICATIONTYPE`  
**Description:** Type of encryption used for password  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 10 | NO |  |
| LABEL | nvarchar | 10 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CardType
**Physical table:** `OSUSR_89Z_CARDTYPE`  
**Description:** Contact Card format  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Code
**Physical table:** `OSUSR_89Z_CODE`  
**Description:** Barcode code for encoding (e.g. QR_CODE)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| SAMPLE | nvarchar | 50 | YES | ('') |
| MARGIN | int |  | YES | ((0)) |
| GEOMETRY | nvarchar | 2 | YES | ('') |

## Encoding
**Physical table:** `OSUSR_89Z_ENCODING`  
**Description:** Character encoding  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ErrorCorrectionLevel
**Physical table:** `OSUSR_89Z_ERRORCORRECTIONLEVEL`  
**Description:** QR_Code error correction level: H, Q, M, L PDF_417 error correction level: L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, AUTO  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CODEID | int |  | YES | (NULL) |

## ImageFormat
**Physical table:** `OSUSR_89Z_IMAGEFORMAT`  
**Description:** Image format (e.g. jpg)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PhoneType
**Physical table:** `OSUSR_89Z_PHONETYPE`  
**Description:** Indicates how to share phone number for call or for facetime  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
