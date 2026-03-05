# Sample_Products_CS

## Tables

- [Brand](#brand)
- [Model](#model)
- [Product](#product)
- [ProductCategory](#productcategory)
- [ProductColor](#productcolor)
- [ProductFavorite](#productfavorite)
- [ProductFeature](#productfeature)
- [ProductImage](#productimage)
- [ProductInventory](#productinventory)
- [ProductSales](#productsales)
- [ProductSize](#productsize)
- [ProductSort](#productsort)
- [ProductType](#producttype)
- [ShoppingCart](#shoppingcart)

## Brand
**Physical table:** `OSUSR_0ei_Brand`  
**Description:** Entity that holds the records of type Brand.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Model
**Physical table:** `OSUSR_0ei_Model`  
**Description:** Entity that holds the records of type Model for products.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| BRANDID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Product
**Physical table:** `OSUSR_0ei_Product`  
**Description:** Entity that holds the records of type Product.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 150 | YES | ('') |
| DESCRIPTION | nvarchar | -1 | YES | ('') |
| PRICE | decimal |  | YES | ((0)) |
| DISCOUNT | decimal |  | YES | ((0)) |
| RATING | decimal |  | YES | ((0)) |
| LIKES | int |  | YES | ((0)) |
| REFERENCE | nvarchar | 50 | YES | ('') |
| EAN | nvarchar | 13 | YES | ('') |
| WEIGHT | nvarchar | 50 | YES | ('') |
| DIMENSIONS | nvarchar | 150 | YES | ('') |
| PRODUCTMODELID | bigint |  | YES | (NULL) |
| PRODUCTCATEGORYID | int |  | YES | (NULL) |
| PRODUCTCOLORID | nvarchar | 50 | YES | (NULL) |
| PRODUCTSIZEID | nvarchar | 50 | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ProductCategory
**Physical table:** `OSUSR_0ei_ProductCategory`  
**Description:** Static Entity with the available categories for products.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 150 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| PRODUCTTYPEID | int |  | YES | (NULL) |

## ProductColor
**Physical table:** `OSUSR_0ei_ProductColor`  
**Description:** Static Entity with the available colors for a product.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| COLOR | nvarchar | 50 | NO |  |

## ProductFavorite
**Physical table:** `OSUSR_0ei_ProductFavorite`  
**Description:** Entity that holds the value if product is favorite.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| PRODUCTID | int |  | YES | (NULL) |

## ProductFeature
**Physical table:** `OSUSR_0ei_ProductFeature`  
**Description:** Entity that holds the features for products  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| DESCRIPTION | nvarchar | 100 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ProductImage
**Physical table:** `OSUSR_0ei_ProductImage`  
**Description:** Entity that holds the sample images for Products.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 150 | YES | ('') |
| FILE | varbinary | -1 | YES | (NULL) |
| ISCOVER | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ProductInventory
**Physical table:** `OSUSR_0ei_ProductInventory`  
**Description:** Entity that holds the records of type ProductInventory.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INVENTORY | decimal |  | YES | ((0)) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| PRODUCTID | int |  | YES | (NULL) |
| WAREHOUSELOCATIONID | int |  | YES | (NULL) |
| ISLATESTINVENTORYRECORD | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ProductSales
**Physical table:** `OSUSR_0ei_ProductSales`  
**Description:** Entity that holds the records of type Product Sales.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| COST | decimal |  | YES | ((0)) |
| QUANTITY | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ProductSize
**Physical table:** `OSUSR_0ei_ProductSize`  
**Description:** Static Entity with the available sizes for a product.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SIZE | nvarchar | 50 | NO |  |

## ProductSort
**Physical table:** `OSUSR_0ei_ProductSort`  
**Description:** Product sort  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| VALUE | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## ProductType
**Physical table:** `OSUSR_0ei_ProductType`  
**Description:** Static Entity with the available types enclosing product categories.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |

## ShoppingCart
**Physical table:** `OSUSR_0ei_ShoppingCart`  
**Description:** Entity that holds the records defining the contents of the shopping cart.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| PRODUCTID | int |  | YES | (NULL) |
| QUANTITY | decimal |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
