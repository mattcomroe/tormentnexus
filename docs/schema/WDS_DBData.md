# WDS_DBData

## Tables

- [RUI_ComponentLibrary](#rui-componentlibrary)
- [RUI_Components](#rui-components)
- [RUI_Components_Categories](#rui-components-categories)
- [RUI_Components_Device](#rui-components-device)
- [RUI_Components_Status](#rui-components-status)
- [RUI_Components_Tags](#rui-components-tags)
- [RUI_Versions](#rui-versions)
- [RUI_Versions_Status](#rui-versions-status)

## RUI_ComponentLibrary
**Physical table:** `OSUSR_3R8_RUI_COMPONENTLIBRARY`  
**Description:** Records that represents the source of the components.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LIBRARYNAME | nvarchar | 50 | YES | ('') |

## RUI_Components
**Physical table:** `OSUSR_3R8_RUI_COMPONENTS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| URL_IDENTIFIER | nvarchar | 150 | YES | ('') |
| NAME | nvarchar | 40 | YES | ('') |
| OVERVIEW | nvarchar | -1 | YES | ('') |
| DO1 | nvarchar | 300 | YES | ('') |
| DO2 | nvarchar | 300 | YES | ('') |
| DO3 | nvarchar | 300 | YES | ('') |
| DO4 | nvarchar | 300 | YES | ('') |
| NOT1 | nvarchar | 300 | YES | ('') |
| NOT2 | nvarchar | 300 | YES | ('') |
| NOT3 | nvarchar | 300 | YES | ('') |
| NOT4 | nvarchar | 300 | YES | ('') |
| HOWTOUSECOMPONENT | nvarchar | -1 | YES | ('') |
| WHENTOUSE | nvarchar | -1 | YES | ('') |
| ACCESSIBILITY | nvarchar | 2000 | YES | ('') |
| LIBRARYID | int |  | YES | (NULL) |
| COMPONENT_CATEGORY_ID | int |  | YES | (NULL) |
| COMPONENTS_STATUS_ID | int |  | YES | (NULL) |
| COMPONENTS_DEVICE_ID | nvarchar | 50 | YES | (NULL) |
| COMPONENTS_TAGID | int |  | YES | (NULL) |
| EXTERNALLINK | nvarchar | 150 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ISINUSE | bit |  | YES | ((0)) |

## RUI_Components_Categories
**Physical table:** `OSUSR_3R8_RUI_COMPONENTS_CATEGORIES`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CAPTION | nvarchar | 50 | YES | ('') |
| ICON | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## RUI_Components_Device
**Physical table:** `OSUSR_3R8_RUI_COMPONENTS_DEVICE`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## RUI_Components_Status
**Physical table:** `OSUSR_3R8_RUI_COMPONENTS_STATUS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| COLOR | nvarchar | 50 | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |

## RUI_Components_Tags
**Physical table:** `OSUSR_3R8_RUI_COMPONENTS_TAGS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## RUI_Versions
**Physical table:** `OSUSR_3R8_RUI_VERSIONS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| VERSIONNUMBER | nvarchar | 50 | YES | ('') |
| VERSIONSTATUSID | int |  | YES | (NULL) |
| NEWFEATURES | nvarchar | 2000 | YES | ('') |
| FIXEDISSUES | nvarchar | 2000 | YES | ('') |
| BREAKINGCHANGES | nvarchar | 2000 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## RUI_Versions_Status
**Physical table:** `OSUSR_3R8_RUI_VERSIONS_STATUS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
