# W_Widgets_UI

## Tables

- [ButtonColor](#buttoncolor)
- [ButtonSize](#buttonsize)
- [InputTextAlign](#inputtextalign)
- [Tabs](#tabs)

## ButtonColor
**Physical table:** `OSUSR_UCF_BUTTONCOLOR`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| COLOR | nvarchar | 50 | NO |  |

## ButtonSize
**Physical table:** `OSUSR_UCF_BUTTONSIZE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |

## InputTextAlign
**Physical table:** `OSUSR_UCF_INPUTTEXTALIGN`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Tabs
**Physical table:** `OSUSR_UCF_TABS`  
**Description:** Defines which tab should be active.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
