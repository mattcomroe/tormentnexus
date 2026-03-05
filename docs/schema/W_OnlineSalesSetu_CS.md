# W_OnlineSalesSetu_CS

## Tables

- [OnlineSalesAnalyticsCode](#onlinesalesanalyticscode)
- [OnlineSalesFacebookPixel](#onlinesalesfacebookpixel)

## OnlineSalesAnalyticsCode
**Physical table:** `OSUSR_VQQ_ONLINESALESANALYTICSCODE`  
**Description:** Codes provided by the Customer for analytic/tracking purposes on the online sales portal.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANTID | int |  | YES | ((0)) |
| ISGOOGLEANALYTICSENABLED | bit |  | YES | ((0)) |
| GOOGLEANALYTICSTRACKINGID | nvarchar | 50 | YES | ('') |
| CUSTOMERID | bigint |  | NO | ((0)) |

## OnlineSalesFacebookPixel
**Physical table:** `OSUSR_VQQ_ONLINESALESFACEBOOKPIXEL`  
**Description:** Codes provided by the Customer for analytic/tracking purposes on the online sales portal.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANTID | int |  | YES | ((0)) |
| ISFACEBOOKPIXELENABLED | bit |  | YES | ((0)) |
| FACEBOOKPIXELID | nvarchar | 50 | YES | ('') |
| CUSTOMERID | bigint |  | NO | ((0)) |
