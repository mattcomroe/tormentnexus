# Product_CS

## Tables

- [CustomerSettingShopify](#customersettingshopify)
- [FeaturedProduct](#featuredproduct)
- [Product](#product)
- [ProductLocationAvailability](#productlocationavailability)
- [ProductLocationTaxRate](#productlocationtaxrate)
- [ProductOption](#productoption)
- [ProductOptionTitle](#productoptiontitle)
- [ProductOptionValue](#productoptionvalue)
- [ProductProductVariantLocation](#productproductvariantlocation)
- [ProductStarred](#productstarred)
- [ProductType](#producttype)
- [ProductVariant](#productvariant)
- [ProductVariantProductOptionValue](#productvariantproductoptionvalue)
- [RequiredShopifyWebhook](#requiredshopifywebhook)
- [ShopifyRegisteredWebhook](#shopifyregisteredwebhook)
- [Vendor](#vendor)

## CustomerSettingShopify
**Physical table:** `OSUSR_72O_TENANTSETTINGSHOPIFY`  
**Description:** Contains Customer Shopify data and settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ISSHOPIFYENABLED | bit |  | YES | ((0)) |
| SHOPIFYAPIKEY | nvarchar | 50 | YES | ('') |
| SHOPIFYPASSWORD | nvarchar | 50 | YES | ('') |
| SHOPIFYSTORENAME | nvarchar | 50 | YES | ('') |
| INVENTORYCONTROLLOCATIONID | int |  | YES | (NULL) |
| SHOPIFYDEFAULTTAXRATEID | int |  | YES | (NULL) |
| SHOPIFYDEFAULTREVENUECATEGOR | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| SHOPIFYLOCATIONID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | NO | ((0)) |

## FeaturedProduct
**Physical table:** `OSUSR_6MF_FEATUREDPRODUCTS`  
**Description:** Contains which products are shown at the top on POS and Mobile app  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| PRODUCTID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| ISMOBILE | bit |  | YES | ((0)) |
| ISMOBILEPOS | bit |  | YES | ((0)) |
| ISPOS | bit |  | YES | ((0)) |
| POSORDER | int |  | YES | ((0)) |
| MOBILEPOSORDER | int |  | YES | ((0)) |

## Product
**Physical table:** `OSUSR_72O_PRODUCT`  
**Description:** Retail product.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PRODUCTTYPEID | int |  | YES | (NULL) |
| TITLE | nvarchar | 255 | YES | ('') |
| DESCRIPTION | nvarchar | -1 | YES | ('') |
| REVENUECATEGORYPICKLISTVALUE | int |  | YES | (NULL) |
| VENDORID | int |  | YES | (NULL) |
| PRICE | decimal |  | YES | ((0)) |
| COMPAREATPRICE | decimal |  | YES | ((0)) |
| SKU | nvarchar | 50 | YES | ('') |
| BARCODE | nvarchar | 50 | YES | ('') |
| ISSHIPPINGADDRESSNEEDED | bit |  | YES | ((0)) |
| INVENTORYPOLICYID | int |  | YES | (NULL) |
| ALLOWPURCHASEWHENOUTOFSTOCK | bit |  | YES | ((0)) |
| SALESTAXID | int |  | YES | (NULL) |
| TOTALINVENTORY | int |  | YES | ((0)) |
| ISSYSTEMPRODUCT | bit |  | YES | ((0)) |
| ISCUSTOMPRODUCT | bit |  | YES | ((0)) |
| ISLINKEDTOSHOPIFY | bit |  | YES | ((0)) |
| SHOPIFYID | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ISTRACKINVENTORY | bit |  | YES | ((0)) |
| HASOPTIONS | bit |  | YES | ((0)) |
| ISVISIBLETOPOS | bit |  | YES | ((0)) |
| SHOPIFYPRODUCTVARIANTID | nvarchar | 50 | YES | ('') |
| SALESCOUNT | int |  | YES | ((0)) |
| CLOUDINARYFILEID | int |  | YES | (NULL) |
| COSTPERUNIT | decimal |  | YES | ((0)) |
| EXTERNALIMAGEID | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SALEPRICE | decimal |  | YES | ((0)) |
| ISONSALE | bit |  | YES | ((0)) |

## ProductLocationAvailability
**Physical table:** `OSUSR_6MF_PRODUCTLOCATIONAVAILABILITY`  
**Description:** Indicates for each location of the product, what is its availability  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ISSELFSERVICEPOS | bit |  | YES | ((1)) |
| ISACTIVEFORMOBILEAPP | bit |  | YES | ((0)) |
| ISSELFSERVICEFORMOBILEAPP | bit |  | YES | ((0)) |

## ProductLocationTaxRate
**Physical table:** `OSUSR_72O_PRODUCTLOCATIONTAXRATE`  
**Description:** Contains the tax rate for each product in each location  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| TAXRATEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ProductOption
**Physical table:** `OSUSR_72O_PRODUCTOPTION`  
**Description:** An option, that will generate a product variant.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| TITLE | nvarchar | 255 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| PRODUCTOPTIONTITLEID | int |  | YES | (NULL) |
| ISLINKEDTOSHOPIFY | bit |  | YES | ((0)) |
| SHOPIFYID | nvarchar | 50 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ProductOptionTitle
**Physical table:** `OSUSR_72O_PRODUCTOPTIONTITLE`  
**Description:** Types of Product Option  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| TITLE | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ProductOptionValue
**Physical table:** `OSUSR_72O_PRODUCTOPTIONVALUE`  
**Description:** Contains possible values for each product option  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PRODUCTOPTIONID | int |  | YES | (NULL) |
| NAME | nvarchar | 255 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ProductProductVariantLocation
**Physical table:** `OSUSR_72O_PRODUCTPRODUCTVARIANTLOCATION`  
**Description:** Associates the product with its variant in the location  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| PRODUCTVARIANTID | int |  | YES | (NULL) |
| QUANTITY | decimal |  | NO | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ProductStarred
**Physical table:** `OSUSR_6MF_PRODUCTSTARRED`  
**Description:** Indicates for each location if the product is starred.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISSTARRED | bit |  | YES | ((0)) |

## ProductType
**Physical table:** `OSUSR_72O_PRODUCTTYPE`  
**Description:** Categorizes the type of product, if its a custom, store credit, Wodify Billing, etc  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ProductVariant
**Physical table:** `OSUSR_72O_PRODUCTVARIANT`  
**Description:** A product variant, such as "Small / Black" for a T-shirt. A variant is the result of instancing an item from product options.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| PRODUCTOPTIONID | int |  | YES | (NULL) |
| PRODUCTOPTIONVALUEID | int |  | YES | (NULL) |
| TITLE | nvarchar | 250 | YES | ('') |
| PRICE | decimal |  | YES | ((0)) |
| COMPAREATPRICE | decimal |  | YES | ((0)) |
| SKU | nvarchar | 50 | YES | ('') |
| BARCODE | nvarchar | 50 | YES | ('') |
| ISLINKEDTOSHOPIFY | bit |  | YES | ((0)) |
| SHOPIFYID | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| LOCATIONID | int |  | YES | (NULL) |
| COSTPERUNIT | decimal |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SALEPRICE | decimal |  | YES | ((0)) |
| ISONSALE | bit |  | YES | ((0)) |

## ProductVariantProductOptionValue
**Physical table:** `OSUSR_72O_PRODUCTVARIANTPRODUCTOPTIONVALUE`  
**Description:** Associates the product option value to the variant  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PRODUCTVARIANTID | int |  | YES | (NULL) |
| PRODUCTOPTIONVALUEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## RequiredShopifyWebhook
**Physical table:** `OSUSR_72O_REQUIREDSHOPIFYWEBHOOK`  
**Description:** Defines required data for all Shopify webhooks  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FORMAT | nvarchar | 50 | YES | ('') |
| TOPIC | nvarchar | 50 | YES | ('') |
| URLPATH | nvarchar | 2000 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| ISAPI | bit |  | YES | ((0)) |

## ShopifyRegisteredWebhook
**Physical table:** `OSUSR_72O_SHOPIFYREGISTEREDWEBHOOK`  
**Description:** This is NOT for public use, and does NOT have any Upserts/Removes/etc. associated with it  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| REQUIREDSHOPIFYWEBHOOKID | int |  | YES | (NULL) |
| SHOPIFYID | nvarchar | 50 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## Vendor
**Physical table:** `OSUSR_72O_VENDOR`  
**Description:** Contains all product vendors  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
