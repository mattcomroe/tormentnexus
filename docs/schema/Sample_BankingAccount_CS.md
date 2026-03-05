# Sample_BankingAccount_CS

## Tables

- [Account](#account)
- [AccountType](#accounttype)
- [AccountTypeThumbnail](#accounttypethumbnail)
- [Transaction](#transaction)
- [TransactionSchedule](#transactionschedule)
- [TransactionType](#transactiontype)

## Account
**Physical table:** `OSUSR_57h_Account`  
**Description:** Entity that holds the records of accounts.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| ACCOUNTTYPEID | int |  | YES | (NULL) |
| ACCOUNTNUMBER | nvarchar | 50 | YES | ('') |
| SWIFT | nvarchar | 50 | YES | ('') |
| ELECTRONICROUTINGNUMBER | nvarchar | 50 | YES | ('') |
| WIRESROUTINGNUMBER | nvarchar | 50 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| MANAGER | bigint |  | YES | (NULL) |
| BALANCE | decimal |  | YES | ((0)) |
| OVERDRAFT | decimal |  | YES | ((0)) |
| ISPERSONAL | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## AccountType
**Physical table:** `OSUSR_57h_AccountType`  
**Description:** The different types of accounts.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## AccountTypeThumbnail
**Physical table:** `OSUSR_57h_AccountTypeThumbnail`  
**Description:** Entity that holds the records of thumbnails of account types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ACCOUNTTYPEID | int |  | NO |  |
| FILENAME | nvarchar | 50 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| THUMBNAIL | varbinary | -1 | YES | (NULL) |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Transaction
**Physical table:** `OSUSR_57h_Transaction`  
**Description:** Entity that holds the records of transactions of accounts.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ACCOUNTID | bigint |  | YES | (NULL) |
| TRANSACTIONTYPE | int |  | YES | (NULL) |
| SOURCEACCOUNT | bigint |  | YES | (NULL) |
| DESTINATIONACCOUNT | bigint |  | YES | (NULL) |
| POSTINGDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TRANSACTIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| DESCRIPTION | nvarchar | 250 | YES | ('') |
| AMOUNT | decimal |  | YES | ((0)) |
| BALANCE | decimal |  | YES | ((0)) |
| ISURGENT | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## TransactionSchedule
**Physical table:** `OSUSR_57h_TransactionSchedule`  
**Description:** The different options when scheduling a transaction.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TransactionType
**Physical table:** `OSUSR_57h_TransactionType`  
**Description:** The different types of transactions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| OPERATIONSIGN | nvarchar | 50 | YES | ('') |
| TEXTCLASSNAME | nvarchar | 50 | YES | ('') |
