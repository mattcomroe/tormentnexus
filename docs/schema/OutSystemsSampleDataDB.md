# OutSystemsSampleDataDB

## Tables

- [Sample_Accounts](#sample-accounts)
- [Sample_Budget](#sample-budget)
- [Sample_Color](#sample-color)
- [Sample_DeliveryType](#sample-deliverytype)
- [Sample_Department](#sample-department)
- [Sample_Employee](#sample-employee)
- [Sample_Location](#sample-location)
- [Sample_LocationMainPicture](#sample-locationmainpicture)
- [Sample_LocationPictures](#sample-locationpictures)
- [Sample_LocationReviews](#sample-locationreviews)
- [Sample_LocationType](#sample-locationtype)
- [Sample_Notification](#sample-notification)
- [Sample_Office](#sample-office)
- [Sample_OfficePictures](#sample-officepictures)
- [Sample_OfficeReviews](#sample-officereviews)
- [Sample_Priority](#sample-priority)
- [Sample_Product](#sample-product)
- [Sample_ProductCategory](#sample-productcategory)
- [Sample_ProductImage](#sample-productimage)
- [Sample_ProductInventory](#sample-productinventory)
- [Sample_ProductMainImage](#sample-productmainimage)
- [Sample_ProductReviews](#sample-productreviews)
- [Sample_ProductSales](#sample-productsales)
- [Sample_ProductType](#sample-producttype)
- [Sample_Request](#sample-request)
- [Sample_RequestFile](#sample-requestfile)
- [Sample_RequestStatus](#sample-requeststatus)
- [Sample_Reviews](#sample-reviews)
- [Sample_Shipping](#sample-shipping)
- [Sample_Size](#sample-size)
- [Sample_Transaction](#sample-transaction)
- [Sample_TransactionType](#sample-transactiontype)

## Sample_Accounts
**Physical table:** `OSUSR_MLE_SAMPLE_ACCOUNTS1`  
**Description:** Entity that holds the records of accounts.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 250 | YES | ('') |
| ACCOUNTNUMBER | int |  | YES | ((0)) |
| BALANCE | decimal |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| OVERDRAFT | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| MANAGER | int |  | YES | (NULL) |
| OWNER | int |  | YES | (NULL) |
| ISPERSONAL | bit |  | YES | ((0)) |

## Sample_Budget
**Physical table:** `OSUSR_MLE_SAMPLE_BUDGET1`  
**Description:** Entity that holds the records of budgets.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| BUDGET | decimal |  | YES | ((0)) |
| CURRENTAMOUNT | decimal |  | YES | ((0)) |
| ACCOUNT | bigint |  | YES | (NULL) |
| TYPE | int |  | YES | (NULL) |

## Sample_Color
**Physical table:** `OSUSR_MLE_SAMPLE_COLOR`  
**Description:** Static Entity with the available colors for a product.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## Sample_DeliveryType
**Physical table:** `OSUSR_MLE_SAMPLE_DELIVERYTYPE`  
**Description:** Static Entity with the available delivery types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Sample_Department
**Physical table:** `OSUSR_MLE_SAMPLE_DEPARTMENT1`  
**Description:** Entity that holds the records of departments.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |

## Sample_Employee
**Physical table:** `OSUSR_MLE_SAMPLE_EMPLOYEE1`  
**Description:** Entity that holds the records of employees.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| BIRTHDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAIL | nvarchar | 250 | YES | ('') |
| PHONE | nvarchar | 20 | YES | ('') |
| BIO | nvarchar | 500 | YES | ('') |
| HIRINGDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| OFFICE | int |  | YES | (NULL) |
| PICTURE | varbinary | -1 | YES | (NULL) |
| FILENAME | nvarchar | 150 | YES | ('') |
| JOBPOSITION | nvarchar | 50 | YES | ('') |
| DEPARTMENT | bigint |  | YES | (NULL) |
| MANAGER | int |  | YES | (NULL) |
| ADDRESS | nvarchar | 250 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |

## Sample_Location
**Physical table:** `OSUSR_MLE_SAMPLE_LOCATION`  
**Description:** Entity that holds the records of locations.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 150 | YES | ('') |
| ADDRESS | nvarchar | 250 | YES | ('') |
| LATITUDE | nvarchar | 50 | YES | ('') |
| LONGITUDE | nvarchar | 50 | YES | ('') |
| LOCATIONTYPE | int |  | YES | (NULL) |
| PHONE | nvarchar | 20 | YES | ('') |
| WEBSITE | nvarchar | 250 | YES | ('') |
| SERVICES | nvarchar | -1 | YES | ('') |
| OPENINGHOUR | nvarchar | 50 | YES | ('') |
| CLOSINGHOUR | nvarchar | 50 | YES | ('') |
| BUSINESSHOURS | nvarchar | -1 | YES | ('') |
| WEEKDAYSBUSINESSHOURS | nvarchar | 50 | YES | ('') |
| SATURDAYBUSINESSHOURS | nvarchar | 50 | YES | ('') |
| SUNDAYBUSINESSHOURS | nvarchar | 50 | YES | ('') |
| HOLIDAYSBUSINESSHOURS | nvarchar | 50 | YES | ('') |

## Sample_LocationMainPicture
**Physical table:** `OSUSR_MLE_SAMPLE_LOCATIONMAINPICTURE`  
**Description:** Entity that holds the records of location main pictures.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LOCATIONID | int |  | NO |  |
| FILENAME | nvarchar | 500 | YES | ('') |
| FILETYPE | nvarchar | 250 | YES | ('') |
| FILE | varbinary | -1 | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Sample_LocationPictures
**Physical table:** `OSUSR_MLE_SAMPLE_LOCATIONPICTURES`  
**Description:** Entity that holds the records of location pictures.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| FILENAME | nvarchar | 500 | YES | ('') |
| FILETYPE | nvarchar | 250 | YES | ('') |
| FILE | varbinary | -1 | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISCOVERIMAGE | bit |  | YES | ((0)) |

## Sample_LocationReviews
**Physical table:** `OSUSR_MLE_SAMPLE_LOCATIONREVIEWS`  
**Description:** Entity that holds the records of location reviews.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| REVIEWID | bigint |  | YES | (NULL) |

## Sample_LocationType
**Physical table:** `OSUSR_MLE_SAMPLE_LOCATIONTYPE`  
**Description:** Static Entity with the available location types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Sample_Notification
**Physical table:** `OSUSR_MLE_SAMPLE_NOTIFICATION1`  
**Description:** Entity that holds the records of notifications.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |

## Sample_Office
**Physical table:** `OSUSR_MLE_SAMPLE_OFFICE1`  
**Description:** Entity that holds the records of offices.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| ADDRESS | nvarchar | 150 | YES | ('') |
| LATITUDE | nvarchar | 50 | YES | ('') |
| LONGITUDE | nvarchar | 50 | YES | ('') |

## Sample_OfficePictures
**Physical table:** `OSUSR_MLE_SAMPLE_OFFICEPICTURES`  
**Description:** Entity that holds the records of office pictures.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| OFFICEID | int |  | YES | (NULL) |
| FILENAME | nvarchar | 500 | YES | ('') |
| FILETYPE | nvarchar | 250 | YES | ('') |
| FILE | varbinary | -1 | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Sample_OfficeReviews
**Physical table:** `OSUSR_MLE_SAMPLE_OFFICEREVIEWS`  
**Description:** Entity that holds the records of office reviews.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| OFFICEID | int |  | YES | (NULL) |
| REVIEWID | bigint |  | YES | (NULL) |

## Sample_Priority
**Physical table:** `OSUSR_MLE_SAMPLE_PRIORITY1`  
**Description:** Static Entity with the available priorities.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## Sample_Product
**Physical table:** `OSUSR_MLE_SAMPLE_PRODUCT2`  
**Description:** Entity that holds the records of products.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 150 | YES | ('') |
| DESCRIPTION | nvarchar | -1 | YES | ('') |
| PRICE | decimal |  | YES | ((0)) |
| STOCK | decimal |  | YES | ((0)) |
| MAXSTOCK | decimal |  | YES | ((0)) |
| STOCKTHRESHOLD | decimal |  | YES | ((0)) |
| CATEGORY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISFAVOURITE | bit |  | YES | ((0)) |
| RATING | decimal |  | YES | ((0)) |
| LIKES | int |  | YES | ((0)) |
| REFERENCE | nvarchar | 50 | YES | ('') |
| EAN | nvarchar | 50 | YES | ('') |
| BRAND | nvarchar | 150 | YES | ('') |
| MODEL | nvarchar | 150 | YES | ('') |
| WEIGHT | nvarchar | 50 | YES | ('') |
| DIMENSIONS | nvarchar | 150 | YES | ('') |
| SAMPLE_COLOR | int |  | YES | (NULL) |
| SAMPLE_SIZE | int |  | YES | (NULL) |

## Sample_ProductCategory
**Physical table:** `OSUSR_MLE_SAMPLE_PRODUCTCATEGORY1`  
**Description:** Static Entity with the available product categories.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 150 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| PRODUCTTYPE | int |  | YES | (NULL) |

## Sample_ProductImage
**Physical table:** `OSUSR_MLE_SAMPLE_PRODUCTIMAGE1`  
**Description:** Entity that holds the records of product images.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 150 | YES | ('') |
| FILE | varbinary | -1 | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISCOVERIMAGE | bit |  | YES | ((0)) |

## Sample_ProductInventory
**Physical table:** `OSUSR_MLE_SAMPLE_PRODUCTINVENTORY2`  
**Description:** Entity that holds the records of product inventories.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INVENTORY | decimal |  | YES | ((0)) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| PRODUCT | int |  | YES | (NULL) |
| WAREHOUSELOCATION | int |  | YES | (NULL) |

## Sample_ProductMainImage
**Physical table:** `OSUSR_MLE_SAMPLE_PRODUCTMAINIMAGE`  
**Description:** Entity that holds the records of product main images.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| PRODUCTID | int |  | NO |  |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 150 | YES | ('') |
| FILE | varbinary | -1 | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Sample_ProductReviews
**Physical table:** `OSUSR_MLE_SAMPLE_PRODUCTREVIEWS1`  
**Description:** Entity that holds the records of product reviews.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PRODUCTID | int |  | YES | (NULL) |
| REVIEWID | bigint |  | YES | (NULL) |

## Sample_ProductSales
**Physical table:** `OSUSR_MLE_SAMPLE_PRODUCTSALES2`  
**Description:** Entity that holds the records of product sales.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| COST | decimal |  | YES | ((0)) |
| QUANTITY | int |  | YES | ((0)) |
| PRODUCT | int |  | YES | (NULL) |

## Sample_ProductType
**Physical table:** `OSUSR_MLE_SAMPLE_PRODUCTTYPE`  
**Description:** Static Entity with the available product types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Sample_Request
**Physical table:** `OSUSR_MLE_SAMPLE_REQUEST1`  
**Description:** Entity that holds the records of requests.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| REQUESTNAME | nvarchar | 150 | YES | ('') |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| DUEDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| COMPLETEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PRIORITY | int |  | YES | (NULL) |
| ASSIGNEDTO | int |  | YES | (NULL) |
| REVIEWEDBY | int |  | YES | (NULL) |
| STATUS | int |  | YES | (NULL) |
| REQUESTEDBY | int |  | YES | (NULL) |

## Sample_RequestFile
**Physical table:** `OSUSR_MLE_SAMPLE_REQUESTFILE1`  
**Description:** Entity that holds the records of request files.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SAMPLE_REQUESTID | int |  | YES | (NULL) |
| FILE | varbinary | -1 | YES | (NULL) |
| FILENAME | nvarchar | 150 | YES | ('') |
| FILETYPE | nvarchar | 150 | YES | ('') |

## Sample_RequestStatus
**Physical table:** `OSUSR_MLE_SAMPLE_REQUESTSTATUS1`  
**Description:** Static Entity with the available request statuses.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## Sample_Reviews
**Physical table:** `OSUSR_MLE_SAMPLE_REVIEWS`  
**Description:** Entity that holds the records of reviews.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REVIEW | nvarchar | 2000 | YES | ('') |
| RATING | decimal |  | YES | ((0)) |
| REVIEWEDBY | nvarchar | 50 | YES | ('') |
| REVIEWEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Sample_Shipping
**Physical table:** `OSUSR_MLE_SAMPLE_SHIPPING`  
**Description:** Entity that holds the records of shipping options.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DELIVERYTYPE | int |  | YES | (NULL) |
| INFO | nvarchar | 500 | YES | ('') |
| PRICE | decimal |  | YES | ((0)) |
| TIMETODELIVER | nvarchar | 50 | YES | ('') |

## Sample_Size
**Physical table:** `OSUSR_MLE_SAMPLE_SIZE`  
**Description:** Static Entity with the available sizes for a product.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## Sample_Transaction
**Physical table:** `OSUSR_MLE_SAMPLE_TRANSACTION1`  
**Description:** Entity that holds the records of transactions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SOURCEACCOUNT | bigint |  | YES | (NULL) |
| DESTINATIONACCOUNT | bigint |  | YES | (NULL) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| DESCRIPTION | nvarchar | 250 | YES | ('') |
| AMOUNT | decimal |  | YES | ((0)) |
| BALANCE | decimal |  | YES | ((0)) |
| TYPE | int |  | YES | (NULL) |

## Sample_TransactionType
**Physical table:** `OSUSR_MLE_SAMPLE_TRANSACTIONTYPE1`  
**Description:** Static Entity with the available transaction types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
