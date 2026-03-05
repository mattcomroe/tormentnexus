# Sandbox_Nick_WebTraditional

## Tables

- [BinaryOr](#binaryor)
- [ClassDates](#classdates)
- [SomeNonesense](#somenonesense)
- [TestTable](#testtable)

## BinaryOr
**Physical table:** `OSUSR_fz2_BinaryOr`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| BATCH | nvarchar | 250 | YES | ('') |

## ClassDates
**Physical table:** `OSUSR_fz2_ClassDates`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| RECURRINGCLASSID | bigint |  | YES | ((0)) |

## SomeNonesense
**Physical table:** `OSUSR_yjq_SomeNonesense`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |

## TestTable
**Physical table:** `OSUSR_yjq_TestTable`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TEXTDATA | nvarchar | 4000 | YES | ('') |
