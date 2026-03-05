# TemplateManager

## Tables

- [ApplicationTemplateIcon](#applicationtemplateicon)
- [Lock](#lock)
- [TemplateKind](#templatekind)
- [TemplateModule](#templatemodule)

## ApplicationTemplateIcon
**Physical table:** `OSUSR_RTV_APPLICATIONTEMPLATEICON`  
**Description:** Application template button icon binary. Internal use only, until we define a proper API.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CONTENT | varbinary | -1 | YES | (NULL) |

## Lock
**Physical table:** `OSUSR_RTV_LOCK`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCK | nvarchar | 50 | YES | ('') |

## TemplateKind
**Physical table:** `OSUSR_RTV_TEMPLATEKIND`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TemplateModule
**Physical table:** `OSUSR_RTV_TEMPLATEMODULE`  
**Description:** Custom application templates for ServiceStudio. Internal use only, until we define a proper API.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| KEY | nvarchar | 50 | YES | ('') |
| LABEL | nvarchar | 50 | YES | ('') |
| DEFAULTTHEMEISMOBILE | bit |  | YES | ((0)) |
| TEMPLATEMODULEFILE | varbinary | -1 | YES | (NULL) |
| OWNERESPACEID | int |  | YES | (NULL) |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| RUNTIMEKIND | nvarchar | 50 | YES | (NULL) |
| TEMPLATEKIND | int |  | YES | (NULL) |
| CONTENTHASH | nvarchar | 50 | YES | ('') |
| USECASE | nvarchar | 1000 | YES | ('') |
