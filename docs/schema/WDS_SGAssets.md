# WDS_SGAssets

## Tables

- [AccordionVariations](#accordionvariations)
- [Styleguide_Alert](#styleguide-alert)
- [Styleguide_AnimationType](#styleguide-animationtype)
- [Styleguide_Autoplay](#styleguide-autoplay)
- [Styleguide_BreakColumns](#styleguide-breakcolumns)
- [Styleguide_Color](#styleguide-color)
- [Styleguide_GutterSize](#styleguide-guttersize)
- [Styleguide_MessageStatus](#styleguide-messagestatus)
- [Styleguide_Position](#styleguide-position)
- [Styleguide_Shape](#styleguide-shape)
- [Styleguide_Size](#styleguide-size)
- [Styleguide_Space](#styleguide-space)
- [Styleguide_Speed](#styleguide-speed)

## AccordionVariations
**Physical table:** `OSUSR_edm_AccordionVariations`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Styleguide_Alert
**Physical table:** `OSUSR_8y1_Styleguide_Alert`  
**Description:** Different types of alert messages  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ALERT | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_AnimationType
**Physical table:** `OSUSR_8y1_Styleguide_AnimationType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ANIMATIONTYPE | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_Autoplay
**Physical table:** `OSUSR_8y1_Styleguide_Autoplay`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| AUTOPLAY | nvarchar | 50 | NO |  |

## Styleguide_BreakColumns
**Physical table:** `OSUSR_8y1_Styleguide_BreakColumns`  
**Description:** Different ways of breaking the columns.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| BREAKCOLUMNS | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_Color
**Physical table:** `OSUSR_8y1_Styleguide_Color`  
**Description:** Different colors available.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| COLOR | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Styleguide_GutterSize
**Physical table:** `OSUSR_8y1_Styleguide_GutterSize`  
**Description:** Different sizes of gutter.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| GUTTERSIZE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_MessageStatus
**Physical table:** `OSUSR_8y1_Styleguide_MessageStatus`  
**Description:** Identify if the message was Received, Sent or Read.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Styleguide_Position
**Physical table:** `OSUSR_8y1_Styleguide_Position`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| POSITION | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_Shape
**Physical table:** `OSUSR_8y1_Styleguide_Shape`  
**Description:** Different shapes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SHAPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Styleguide_Size
**Physical table:** `OSUSR_8y1_Styleguide_Size`  
**Description:** Different sizes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SIZE | nvarchar | 50 | NO |  |

## Styleguide_Space
**Physical table:** `OSUSR_8y1_Styleguide_Space`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SPACE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_Speed
**Physical table:** `OSUSR_8y1_Styleguide_Speed`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SPEED | nvarchar | 50 | NO |  |
