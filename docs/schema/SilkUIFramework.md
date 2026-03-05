# SilkUIFramework

## Tables

- [AutoPlay](#autoplay)
- [Color](#color)
- [DeviceResponsive](#deviceresponsive)
- [DeviceType](#devicetype)
- [Gender](#gender)
- [Orientation](#orientation)
- [Position](#position)
- [ResponsiveBehavior](#responsivebehavior)
- [Sizes](#sizes)
- [Tabs](#tabs)
- [Trigger](#trigger)
- [WizardStep](#wizardstep)

## AutoPlay
**Physical table:** `OSUSR_zdl_AutoPlay`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| AUTOPLAYSPEED | nvarchar | 20 | YES | ('') |

## Color
**Physical table:** `OSUSR_zdl_Color`  
**Description:** Collection of curated colors which match with the respective CSS classes  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| BACKGROUND | nvarchar | 50 | NO |  |
| TEXT | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## DeviceResponsive
**Physical table:** `OSUSR_zdl_DeviceResponsive`  
**Description:** Defines the behavior response according to the device or group of devices types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## DeviceType
**Physical table:** `OSUSR_zdl_DeviceType`  
**Description:** Type of devices which can access the application  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CLASS | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Gender
**Physical table:** `OSUSR_zdl_Gender`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Orientation
**Physical table:** `OSUSR_zdl_Orientation`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Position
**Physical table:** `OSUSR_zdl_Position`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## ResponsiveBehavior
**Physical table:** `OSUSR_zdl_ResponsiveBehavior`  
**Description:** Defines the breaking behavior.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CLASS | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Sizes
**Physical table:** `OSUSR_zdl_Sizes`  
**Description:** Auto, Small, Medium, Large  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Tabs
**Physical table:** `OSUSR_zdl_Tabs`  
**Description:** Defines which tab should be active.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |

## Trigger
**Physical table:** `OSUSR_zdl_Trigger`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## WizardStep
**Physical table:** `OSUSR_zdl_WizardStep`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
| STEPORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
