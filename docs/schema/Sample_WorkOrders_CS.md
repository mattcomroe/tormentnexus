# Sample_WorkOrders_CS

## Tables

- [CustomerFeedback](#customerfeedback)
- [CustomerNote](#customernote)
- [WorkOrder](#workorder)
- [WorkOrderStatus](#workorderstatus)
- [WorkOrderTask](#workordertask)
- [WorkOrderType](#workordertype)
- [WorkTask](#worktask)
- [WorkTaskServiceType](#worktaskservicetype)
- [WorkTaskType](#worktasktype)

## CustomerFeedback
**Physical table:** `OSUSR_2m7_CustomerFeedback`  
**Description:** Entity that holds the records of Customer Feedbacks.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| WORKORDERID | bigint |  | NO |  |
| SCORE | int |  | YES | ((0)) |
| FEEDBACK | nvarchar | 1000 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerNote
**Physical table:** `OSUSR_2m7_CustomerNote`  
**Description:** Entity that holds the records of Customer Notes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WORKORDERID | bigint |  | YES | (NULL) |
| NOTE | nvarchar | 2000 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## WorkOrder
**Physical table:** `OSUSR_2m7_WorkOrder`  
**Description:** Entity that holds the records of Work Orders.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WORKORDERCODE | nvarchar | 50 | YES | ('') |
| TITLE | nvarchar | 100 | YES | ('') |
| DESCRIPTION | nvarchar | 1000 | YES | ('') |
| TECHNICIANID | bigint |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| WORKORDERTYPEID | int |  | YES | (NULL) |
| WORKORDERSTATUSID | int |  | YES | (NULL) |
| STARTDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| DURATION | int |  | YES | ((0)) |
| ENDDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## WorkOrderStatus
**Physical table:** `OSUSR_2m7_WorkOrderStatus`  
**Description:** Status of the Work Order  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| TEXTCOLOR | nvarchar | 50 | YES | ('') |

## WorkOrderTask
**Physical table:** `OSUSR_2m7_WorkOrderTask`  
**Description:** Entity that holds the records of Work Order Tasks.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WORKORDERID | bigint |  | YES | (NULL) |
| TASKID | bigint |  | YES | (NULL) |
| ISDONE | bit |  | YES | ((0)) |

## WorkOrderType
**Physical table:** `OSUSR_2m7_WorkOrderType`  
**Description:** Type of Work Order  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| DURATION | int |  | YES | ((0)) |

## WorkTask
**Physical table:** `OSUSR_2m7_WorkTask`  
**Description:** Entity that holds the records of Work Tasks.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TASKCODE | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| TASKSERVICETYPEID | int |  | YES | (NULL) |
| TASKTYPEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## WorkTaskServiceType
**Physical table:** `OSUSR_2m7_WorkTaskServiceType`  
**Description:** Type of Service  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## WorkTaskType
**Physical table:** `OSUSR_2m7_WorkTaskType`  
**Description:** Type of Task  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
