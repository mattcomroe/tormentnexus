# Sample_Opportunity_CS

## Tables

- [Opportunity](#opportunity)
- [OpportunityStage](#opportunitystage)
- [OpportunityType](#opportunitytype)
- [Order](#order)
- [OrderItem](#orderitem)
- [OrderStatus](#orderstatus)

## Opportunity
**Physical table:** `OSUSR_yc7_Opportunity`  
**Description:** Represents an opportunity associated with a company.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ACCOUNTID | bigint |  | YES | (NULL) |
| CODE | nvarchar | 50 | YES | ('') |
| NAME | nvarchar | 100 | YES | ('') |
| DESCRIPTION | nvarchar | 1500 | YES | ('') |
| ASSIGNEDTO | bigint |  | YES | (NULL) |
| OPPORTUNITYTYPEID | int |  | YES | (NULL) |
| OPPORTUNITYSTAGEID | int |  | YES | (NULL) |
| AMOUNT | decimal |  | YES | ((0)) |
| PROBABILITY | decimal |  | YES | ((0)) |
| EXPECTEDREVENUE | decimal |  | YES | ((0)) |
| CLOSEON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## OpportunityStage
**Physical table:** `OSUSR_yc7_OpportunityStage`  
**Description:** Stage of the Opportunity.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| TEXTCOLOR | nvarchar | 50 | YES | ('') |

## OpportunityType
**Physical table:** `OSUSR_yc7_OpportunityType`  
**Description:** Type of Opportunity.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Order
**Physical table:** `OSUSR_yc7_Order`  
**Description:** Represents an order associated with a company, possibly originated from an opportunity.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CODE | nvarchar | 50 | YES | ('') |
| ACCOUNTID | bigint |  | YES | (NULL) |
| OPPORTUNITYID | bigint |  | YES | (NULL) |
| TOTALAMOUNT | decimal |  | YES | ((0)) |
| STATUSID | int |  | YES | (NULL) |
| ORDERDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| REQUIREDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SHIPPEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ASSIGNEDTO | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## OrderItem
**Physical table:** `OSUSR_yc7_OrderItem`  
**Description:** Each record represents one item (product) inside the order.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ORDERID | bigint |  | YES | (NULL) |
| PRODUCTID | int |  | YES | (NULL) |
| QUANTITY | int |  | YES | ((0)) |
| DISCOUNT | decimal |  | YES | ((0)) |
| AMOUNT | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## OrderStatus
**Physical table:** `OSUSR_yc7_OrderStatus`  
**Description:** Status of the Order.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| TEXTCOLOR | nvarchar | 50 | YES | ('') |
