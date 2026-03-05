# OutSystemsUIWeb

## Tables

- [Alert](#alert)
- [BreakColumns](#breakcolumns)
- [Color](#color)
- [DeviceResponsive](#deviceresponsive)
- [EnterAnimation](#enteranimation)
- [GutterSize](#guttersize)
- [LeaveAnimation](#leaveanimation)
- [Orientation](#orientation)
- [PositionBase](#positionbase)
- [PositionExtended](#positionextended)
- [ProgressBarSize](#progressbarsize)
- [ResponsiveTableRecords](#responsivetablerecords)
- [Shape](#shape)
- [Size](#size)
- [Space](#space)
- [Speed](#speed)
- [Step](#step)
- [Trigger](#trigger)

## Alert
**Physical table:** `OSUSR_41o_Alert2`  
**Description:** Different types of alert messages.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ALERT | nvarchar | 50 | NO |  |

## BreakColumns
**Physical table:** `OSUSR_41o_BreakColumns1`  
**Description:** Different ways of breaking the columns.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| BREAKCOLUMNS | nvarchar | 50 | NO |  |

## Color
**Physical table:** `OSUSR_41o_Color1`  
**Description:** Different colors available.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| COLOR | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## DeviceResponsive
**Physical table:** `OSUSR_41o_DeviceResponsive1`  
**Description:** Defines the behavior response according to the device or group of devices types.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## EnterAnimation
**Physical table:** `OSUSR_41o_EnterAnimation1`  
**Description:** Different types of entering animations.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ENTERANIMATION | nvarchar | 50 | NO |  |

## GutterSize
**Physical table:** `OSUSR_41o_GutterSize2`  
**Description:** Different sizes of gutter.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| GUTTERSIZE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## LeaveAnimation
**Physical table:** `OSUSR_41o_LeaveAnimation1`  
**Description:** Different types of leaving animations.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LEAVEANIMATION | nvarchar | 50 | NO |  |

## Orientation
**Physical table:** `OSUSR_41o_Orientation1`  
**Description:** Different orientations.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ORIENTATION | nvarchar | 50 | NO |  |

## PositionBase
**Physical table:** `OSUSR_41o_PositionBase1`  
**Description:** Different positions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| POSITIONBASE | nvarchar | 50 | NO |  |

## PositionExtended
**Physical table:** `OSUSR_41o_PositionExtended1`  
**Description:** Added more options for positions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| POSITIONEXTENDED | nvarchar | 50 | NO |  |

## ProgressBarSize
**Physical table:** `OSUSR_41o_ProgressBarSize1`  
**Description:** Different sizes for the progress bar.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| PROGRESSBARSIZE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## ResponsiveTableRecords
**Physical table:** `OSUSR_41o_ResponsiveTableRecords2`  
**Description:** Different options for responsive for the responsive table.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| RESPONSIVETABLERECORDS | nvarchar | 50 | NO |  |

## Shape
**Physical table:** `OSUSR_41o_Shape1`  
**Description:** Different shapes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SHAPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Size
**Physical table:** `OSUSR_41o_Size1`  
**Description:** Different sizes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SIZE | nvarchar | 50 | NO |  |

## Space
**Physical table:** `OSUSR_41o_Space1`  
**Description:** Different spaces.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SPACE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Speed
**Physical table:** `OSUSR_41o_Speed1`  
**Description:** Different speed of animations.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SPEED | nvarchar | 50 | NO |  |

## Step
**Physical table:** `OSUSR_41o_Step2`  
**Description:** Different types of status.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| STEPS | nvarchar | 50 | NO |  |

## Trigger
**Physical table:** `OSUSR_41o_Trigger2`  
**Description:** Different types of triggers.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TRIGGERACTION | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
