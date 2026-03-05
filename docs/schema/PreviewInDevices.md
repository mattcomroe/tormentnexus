# PreviewInDevices

## Tables

- [ActivationParameter](#activationparameter)
- [Background](#background)
- [ButtonShare](#buttonshare)
- [ConfigurationParameter](#configurationparameter)
- [Device](#device)
- [DeviceColor](#devicecolor)
- [DeviceType](#devicetype)
- [FeatureToggle](#featuretoggle)

## ActivationParameter
**Physical table:** `OSUSR_UTN_ACTIVATIONPARAMETER`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INFONAME | nvarchar | 75 | YES | ('') |

## Background
**Physical table:** `OSUSR_UTN_BACKGROUND`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## ButtonShare
**Physical table:** `OSUSR_UTN_BUTTONSHARE`  
**Description:** Identifiers of the buttons to share (useful to validate and prevent manipulations)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | nvarchar | 50 | NO |  |

## ConfigurationParameter
**Physical table:** `OSUSR_UTN_CONFIGURATIONPARAMETER`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PARAMETERNAME | nvarchar | 75 | YES | ('') |
| PARAMETERDEFAULTVALUE | nvarchar | 100 | YES | ('') |
| PARAMETERDESCRIPTION | nvarchar | 255 | YES | ('') |
| ISFEATURETOGGLE | bit |  | YES | ((0)) |
| FEATURETOGGLENAME | nvarchar | 50 | YES | ('') |

## Device
**Physical table:** `OSUSR_UTN_DEVICE1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| WIDTH | int |  | YES | ((0)) |
| HEIGHT | int |  | YES | ((0)) |
| DEVICETYPEID | int |  | YES | (NULL) |
| DEVICECSSCLASS | nvarchar | 50 | YES | ('') |
| BORDERWIDTH | int |  | YES | ((0)) |
| OUTERBORDERRADIUS | int |  | YES | ((0)) |
| INNERBORDERRADIUS | int |  | YES | ((0)) |
| SYSTEM | nvarchar | 50 | YES | ('') |

## DeviceColor
**Physical table:** `OSUSR_UTN_DEVICECOLOR`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## DeviceType
**Physical table:** `OSUSR_UTN_DEVICE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CSSCLASS | nvarchar | 50 | YES | ('') |

## FeatureToggle
**Physical table:** `OSUSR_UTN_FEATURETOGGLE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| KEY | nvarchar | 75 | YES | ('') |
| VALUE | nvarchar | 255 | YES | ('') |
