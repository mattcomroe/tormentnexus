# zSandboxDon_CustomAttributes

## Tables

- [AttributeAccessibility](#attributeaccessibility)
- [AttributeDefinition](#attributedefinition)
- [CustomAttribute](#customattribute)
- [CustomAttributeAccess](#customattributeaccess)
- [CustomAttributeUsage](#customattributeusage)
- [CustomFieldType](#customfieldtype)
- [SaleForceAttribute](#saleforceattribute)
- [UserAnswer](#useranswer)

## AttributeAccessibility
**Physical table:** `OSUSR_8cd_ObjectAccessibility`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## AttributeDefinition
**Physical table:** `OSUSR_8cd_ObjectKeySpecificationJSONList6`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| CUSTOMFIELDJSONLIST | nvarchar | 1999 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| USERPROMPT | nvarchar | 50 | YES | ('') |

## CustomAttribute
**Physical table:** `OSUSR_8cd_CustomObject_Json6`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| OBJECTNAME | nvarchar | 100 | YES | ('') |
| CUSTOMOBJECTACCESSID | int |  | YES | (NULL) |
| OBJECTCATEGORYID | bigint |  | YES | (NULL) |
| OBJECTACCESSIBILITYID | int |  | YES | (NULL) |
| ISAPIENABLED | bit |  | YES | ((0)) |
| ISPERMISSION | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMOBJECTUSAGEID | int |  | YES | (NULL) |
| ATTRIBUTENAME | nvarchar | 100 | YES | ('') |
| CUSTOMATTRIBUTEACCESSID | int |  | YES | (NULL) |
| CUSTOMATTRIBUTEUSAGEID | int |  | YES | (NULL) |
| ATTRIBUTEACCESSIBILITYID | int |  | YES | (NULL) |

## CustomAttributeAccess
**Physical table:** `OSUSR_8cd_CustomObjectAccess`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CustomAttributeUsage
**Physical table:** `OSUSR_8cd_CustomObjectUsage`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## CustomFieldType
**Physical table:** `OSUSR_8cd_CustomFieldType1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## SaleForceAttribute
**Physical table:** `OSUSR_8cd_SaleForceObject`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ATTRIBUTE1 | nvarchar | 50 | YES | ('') |

## UserAnswer
**Physical table:** `OSUSR_8cd_UserSelectionJsonListCustomFields5`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CUSTOMOBJECTJSONID | int |  | YES | (NULL) |
| USERSOBJECT | int |  | YES | (NULL) |
| GUID | nvarchar | 50 | YES | ('') |
| CUSTOMFIELDJSONLIST | nvarchar | 1999 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| USERSID | int |  | YES | (NULL) |
| OBJECTDEFINITIONID | int |  | YES | (NULL) |
| ATTRIBUTEDEFINITIONID | int |  | YES | (NULL) |
