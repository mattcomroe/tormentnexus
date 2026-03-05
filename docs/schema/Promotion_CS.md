# Promotion_CS

## Tables

- [PromoCode](#promocode)
- [PromoCodeInvoiceDetailExtraDiscount](#promocodeinvoicedetailextradiscount)
- [PromoCodeLocation](#promocodelocation)
- [PromoCodeMembership](#promocodemembership)
- [PromoCodeProduct](#promocodeproduct)

## PromoCode
**Physical table:** `OSUSR_roc_PromoCode`  
**Description:** Promotion code that enables discounts when input on purchases.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| DISCOUNTID | int |  | NO |  |
| CODE | nvarchar | 20 | YES | ('') |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| NUMBEROFUSES | int |  | YES | ((0)) |
| ISAPPLICABLETOMEMBERSHIPS | bit |  | YES | ((0)) |
| ISAPPLICABLETOPRODUCTS | bit |  | YES | ((0)) |
| ISAPPLICABLETOSERVICES | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| ISAPPLICABLETODROPINS | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## PromoCodeInvoiceDetailExtraDiscount
**Physical table:** `OSUSR_roc_PromoCodeInvoiceDetailExtraDiscount`  
**Description:** References invoice detail extra discount records that were created when applying a promo code to an invoice.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROMOCODEID | int |  | YES | (NULL) |
| INVOICEHEADERID | int |  | YES | (NULL) |
| INVOICEDETAILEXTRADISCOUNTID | bigint |  | YES | (NULL) |
| ISDROPIN | bit |  | YES | ((0)) |

## PromoCodeLocation
**Physical table:** `OSUSR_roc_PromoCodeLocation`  
**Description:** Locations where a promo code is applicable.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROMOCODEID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |

## PromoCodeMembership
**Physical table:** `OSUSR_roc_PromoCodeClassMembership`  
**Description:** Memberships that are eligible for a discount using a promo code.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROMOCODEID | int |  | YES | (NULL) |
| MEMBERPLANTEMPLATEID | int |  | YES | (NULL) |
| PAYMENTSCHEDULETEMPLATEID | int |  | YES | (NULL) |
| CLASSMEMBERSHIPTYPE | int |  | YES | ((0)) |
| HASINITIALAPPLICATION | bit |  | YES | ((0)) |
| HASSETUPAPPLICATION | bit |  | YES | ((0)) |
| HASRENEWALAPPLICATION | bit |  | YES | ((0)) |

## PromoCodeProduct
**Physical table:** `OSUSR_roc_PromoCodeProduct`  
**Description:** Products that are eligible for a discount using a promo code.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROMOCODEID | int |  | YES | (NULL) |
| PRODUCTID | int |  | YES | (NULL) |
