# Sample_Ticket_CS

## Tables

- [Ticket](#ticket)
- [TicketAttachment](#ticketattachment)
- [TicketAttachmentBinary](#ticketattachmentbinary)
- [TicketCategory](#ticketcategory)
- [TicketFilterByPeriod](#ticketfilterbyperiod)
- [TicketMessage](#ticketmessage)
- [TicketPriority](#ticketpriority)
- [TicketStatus](#ticketstatus)

## Ticket
**Physical table:** `OSUSR_gdk_Ticket`  
**Description:** Entity to hold all information regarding the Tickets  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SUBJECT | nvarchar | 100 | YES | ('') |
| CATEGORYID | int |  | YES | (NULL) |
| PRIORITYID | int |  | YES | (NULL) |
| STATUSID | int |  | YES | (NULL) |
| REQUESTERID | bigint |  | YES | (NULL) |
| ASSIGNEEID | bigint |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## TicketAttachment
**Physical table:** `OSUSR_gdk_TicketAttachment`  
**Description:** Entity to hold all information regarding the Tickets attachments  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TICKETMESSAGEID | bigint |  | YES | (NULL) |
| FILENAME | nvarchar | 100 | YES | ('') |
| FILESIZE | bigint |  | YES | ((0)) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## TicketAttachmentBinary
**Physical table:** `OSUSR_gdk_TicketAttachmentBinary`  
**Description:** Entity to store TicketAttachmentsBinary on the database  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TICKETATTACHMENTID | bigint |  | NO |  |
| CONTENT | varbinary | -1 | YES | (NULL) |

## TicketCategory
**Physical table:** `OSUSR_gdk_TicketCategory`  
**Description:** Entity that holds the records of type TicketCategory.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| FILLCOLOR | nvarchar | 50 | YES | ('') |

## TicketFilterByPeriod
**Physical table:** `OSUSR_gdk_TicketFilterByPeriod`  
**Description:** Entity that holds the records of type TicketFilterByPeriod.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TicketMessage
**Physical table:** `OSUSR_gdk_TicketMessage`  
**Description:** Entity to hold Ticket messages  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TICKETID | bigint |  | YES | (NULL) |
| UNIQUEBOOTSTRAPIDENTIFIER | nvarchar | 50 | YES | ('') |
| MESSAGE | nvarchar | 2000 | YES | ('') |
| ISINTERNALNOTE | bit |  | YES | ((0)) |
| ISLASTMESSAGE | bit |  | YES | ((0)) |
| DURATION | int |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | bigint |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | bigint |  | YES | (NULL) |

## TicketPriority
**Physical table:** `OSUSR_gdk_TicketPriority`  
**Description:** Entity that holds the records of type TicketPriority.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| SLA_LABEL | nvarchar | 50 | YES | ('') |
| SLA_MINUTES | int |  | YES | ((0)) |
| SLA_SOONOVERDUE | decimal |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| TEXTCOLOR | nvarchar | 50 | YES | ('') |

## TicketStatus
**Physical table:** `OSUSR_gdk_TicketStatus`  
**Description:** Entity that holds the records of type TicketStatus.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
