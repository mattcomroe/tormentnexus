# LDAPAuthProvider

## Tables

- [LdapAuthenticationType](#ldapauthenticationtype)
- [LDAPSupportedProtocols](#ldapsupportedprotocols)
- [MenuItem](#menuitem)
- [MenuSubItem](#menusubitem)

## LdapAuthenticationType
**Physical table:** `OSUSR_i8y_LdapAuthenticationType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## LDAPSupportedProtocols
**Physical table:** `OSUSR_i8y_LDAPSupportedProtocols`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## MenuItem
**Physical table:** `OSUSR_i8y_MenuItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## MenuSubItem
**Physical table:** `OSUSR_i8y_MenuSubItem`  
**Description:** Records in this entity will be automatically created when dragging web screens to the Common\Menu web block. Their labels can later be changed.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |
| MENUITEMID | int |  | YES | (NULL) |
