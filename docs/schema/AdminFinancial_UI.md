# AdminFinancial_UI

## Tables

- [FinancialSettings_TertiaryMenuItem](#financialsettings-tertiarymenuitem)

## FinancialSettings_TertiaryMenuItem
**Physical table:** `OSUSR_7w4_FinancialSettings_TertiaryMenuItem`  
**Description:** Static entity with the available options on the Financial Settings screen.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
