# Pendo_CS

## Tables

- [PendoTimerValues](#pendotimervalues)

## PendoTimerValues
**Physical table:** `OSUSR_pdn_PendoTimerValues`  
**Description:** This table will contain some values that will be used in pendo  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NUMPERFORMANCESLASTMONTH | bigint |  | YES | ((0)) |
| REVENUELASTMONTH | decimal |  | YES | ((0)) |
| VALUELASTMONTH | decimal |  | YES | ((0)) |
| LIFETIMEVALUE | decimal |  | YES | ((0)) |
| AVGWODSPERDAYLASTMONTH | decimal |  | YES | ((0)) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
