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
**Physical table:** `OSUSR_EDM_ACCORDIONVARIATIONS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Styleguide_Alert
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_ALERT`  
**Description:** Different types of alert messages  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ALERT | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_AnimationType
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_ANIMATIONTYPE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ANIMATIONTYPE | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_Autoplay
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_AUTOPLAY`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| AUTOPLAY | nvarchar | 50 | NO |  |

## Styleguide_BreakColumns
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_BREAKCOLUMNS`  
**Description:** Different ways of breaking the columns.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| BREAKCOLUMNS | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_Color
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_COLOR`  
**Description:** Different colors available.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| COLOR | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Styleguide_GutterSize
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_GUTTERSIZE`  
**Description:** Different sizes of gutter.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| GUTTERSIZE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_MessageStatus
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_MESSAGESTATUS`  
**Description:** Identify if the message was Received, Sent or Read.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Styleguide_Position
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_POSITION`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| POSITION | nvarchar | 50 | NO |  |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_Shape
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_SHAPE`  
**Description:** Different shapes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SHAPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Styleguide_Size
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_SIZE`  
**Description:** Different sizes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SIZE | nvarchar | 50 | NO |  |

## Styleguide_Space
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_SPACE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SPACE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IMAGENAME | nvarchar | 50 | YES | ('') |

## Styleguide_Speed
**Physical table:** `OSUSR_8Y1_STYLEGUIDE_SPEED`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SPEED | nvarchar | 50 | NO |  |
