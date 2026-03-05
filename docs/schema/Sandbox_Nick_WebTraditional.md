# Sandbox_Nick_WebTraditional

## Tables

- [BinaryOr](#binaryor)
- [ClassDates](#classdates)
- [SomeNonesense](#somenonesense)
- [TestTable](#testtable)

## BinaryOr
**Physical table:** `OSUSR_FZ2_BINARYOR`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| BATCH | nvarchar | 250 | YES | ('') |

## ClassDates
**Physical table:** `OSUSR_FZ2_CLASSDATES`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| RECURRINGCLASSID | bigint |  | YES | ((0)) |

## SomeNonesense
**Physical table:** `OSUSR_YJQ_SOMENONESENSE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |

## TestTable
**Physical table:** `OSUSR_YJQ_TESTTABLE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TEXTDATA | nvarchar | 4000 | YES | ('') |
