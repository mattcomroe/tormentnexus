# PointOfSale_CS

## Tables

- [Cart](#cart)

## Cart
**Physical table:** `OSUSR_72o_Cart`  
**Description:** Contains info of a cart in POS  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| INVOICEHEADERID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISCURRENT | bit |  | YES | ((0)) |
| ISSAVED | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| ISSELFSERVICE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
