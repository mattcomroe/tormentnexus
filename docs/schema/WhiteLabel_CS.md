# WhiteLabel_CS

## Tables

- [WhiteLabel](#whitelabel)
- [WhiteLabelImage](#whitelabelimage)

## WhiteLabel
**Physical table:** `OSUSR_2mp_WhiteLabel`  
**Description:** Contains the Full CSS for each customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CUSTOMERID | bigint |  | NO |  |
| CSS | nvarchar | -1 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| WODTABICONLABEL | nvarchar | 50 | YES | ('') |
| SHOWDEFAULTIMAGEHEADER | bit |  | YES | ((0)) |
| SHOWDEFAULTIMAGELOADING | bit |  | YES | ((0)) |
| WODTABICONSTYLE | nvarchar | 20 | YES | ('') |
| HEADERIMAGEURI | nvarchar | 500 | YES | ('') |
| HEADERBGCOLOR | nvarchar | 10 | YES | ('') |
| LOADINGIMAGEURI | nvarchar | 500 | YES | ('') |
| LOADINGSCREENBGCOLOR | nvarchar | 10 | YES | ('') |
| APPBGCOLOR | nvarchar | 10 | YES | ('') |
| BUTTONLINKCOLOR | nvarchar | 10 | YES | ('') |
| WODTABICONNAME | nvarchar | 50 | YES | ('') |
| PRIMARYCOLOR | nvarchar | 10 | YES | ('') |
| PRIMARYCOLORLIGHT | nvarchar | 10 | YES | ('') |
| PRIMARYCOLORLIGHTER | nvarchar | 10 | YES | ('') |
| PRIMARYCOLORLIGHTEST | nvarchar | 10 | YES | ('') |
| PRIMARYCOLORDARK | nvarchar | 10 | YES | ('') |
| PRIMARYCOLORDARKER | nvarchar | 10 | YES | ('') |
| PRIMARYCOLORDARKEST | nvarchar | 10 | YES | ('') |
| MAINTEXTCOLOR | nvarchar | 10 | YES | ('') |
| SECUNDARYTEXTCOLOR | nvarchar | 10 | YES | ('') |
| SHOWDEFAULTLOADING | bit |  | YES | ((0)) |
| PRIMARYCOLOR2 | nvarchar | 10 | YES | ('') |
| BUTTONCOLORLIGHT | nvarchar | 10 | YES | ('') |
| BUTTONCOLORDARK | nvarchar | 10 | YES | ('') |
| LOADINGANDHEADERBGCOLOR | nvarchar | 10 | YES | ('') |

## WhiteLabelImage
**Physical table:** `OSUSR_2mp_WhiteLabelImage`  
**Description:** Contains all image types that can be uploaded for white labeling  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
