# WDS_DBDocOptions

## Tables

- [DOC_AnimationTypes](#doc-animationtypes)
- [DOC_BreakColumns](#doc-breakcolumns)
- [DOC_Color](#doc-color)
- [DOC_GutterSize](#doc-guttersize)
- [DOC_MessageStatus](#doc-messagestatus)
- [DOC_Position](#doc-position)
- [DOC_RibbonPosition](#doc-ribbonposition)
- [DOC_Shape](#doc-shape)
- [DOC_Size](#doc-size)
- [DOC_Space](#doc-space)

## DOC_AnimationTypes
**Physical table:** `OSUSR_RNK_DOC_ANIMATIONTYPES`  
**Description:** Used only for documentation, because can't fetch data from Library Modules  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ANIMATIONTYPE | nvarchar | 50 | NO |  |

## DOC_BreakColumns
**Physical table:** `OSUSR_RNK_DOC_BREAKCOLUMNS`  
**Description:** Different ways of breaking the columns.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| BREAKCOLUMNS | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## DOC_Color
**Physical table:** `OSUSR_RNK_DOC_COLOR`  
**Description:** Used only for documentation, because can't fetch data from Library Modules  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| COLOR | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## DOC_GutterSize
**Physical table:** `OSUSR_RNK_DOC_GUTTERSIZE`  
**Description:** Different sizes of gutter.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| GUTTERSIZE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## DOC_MessageStatus
**Physical table:** `OSUSR_RNK_DOC_MESSAGESTATUS`  
**Description:** Identify if the message was Received, Sent or Read.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## DOC_Position
**Physical table:** `OSUSR_RNK_DOC_POSITION`  
**Description:** Used only for documentation, because can't fetch data from Library Modules  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| POSITION | nvarchar | 50 | NO |  |

## DOC_RibbonPosition
**Physical table:** `OSUSR_RNK_DOC_RIBBONPOSITION`  
**Description:** Used only for documentation, because can't fetch data from Library Modules  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| POSITION | nvarchar | 50 | NO |  |

## DOC_Shape
**Physical table:** `OSUSR_RNK_DOC_SHAPE`  
**Description:** Different shapes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SHAPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## DOC_Size
**Physical table:** `OSUSR_RNK_DOC_SIZE`  
**Description:** Different sizes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SIZE | nvarchar | 50 | NO |  |

## DOC_Space
**Physical table:** `OSUSR_RNK_DOC_SPACE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SPACE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| NAME | nvarchar | 50 | YES | ('') |
