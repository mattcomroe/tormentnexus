# TagsAndNotes_CS

## Tables

- [ObjectNote](#objectnote)
- [ObjectTag](#objecttag)
- [Tag](#tag)
- [TextObjectTag](#textobjecttag)

## ObjectNote
**Physical table:** `OSUSR_UWR_OBJECTNOTE`  
**Description:** Contains all the Notes for all the Objects. ObjectId is the identifier of the entity (Lead.Id, Invoice.Id, LocationId etc) ObjectTypeId is the definition of the Object (Lead, Invoice, Location, etc)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| OBJECTID | int |  | YES | ((0)) |
| OBJECTTYPEID | int |  | YES | (NULL) |
| NOTE | nvarchar | -1 | YES | ('') |
| OBJECTNODEOLDID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ObjectTag
**Physical table:** `OSUSR_UWR_OBJECTTAG`  
**Description:** Contains all the Tags for all the Objects. ObjectId is the identifier of the entity (Lead.Id, Invoice.Id, LocationId etc) ObjectTypeId is the definition of the Object (Lead, Invoice, Location, etc)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| OBJECTID | int |  | YES | ((0)) |
| OBJECTTYPEID | int |  | YES | (NULL) |
| TAGID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## Tag
**Physical table:** `OSUSR_UWR_TAG`  
**Description:** Contains all the tags for the entire application. Can be reused for several modules  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| LABEL | nvarchar | 500 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| TAGOLDID | int |  | YES | (NULL) |
| OBJECTTYPEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| COLORID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |

## TextObjectTag
**Physical table:** `OSUSR_EAB_TEXTOBJECTTAG`  
**Description:** Contains all the Tags for all the Objects with Text as the ObjectId ObjectId is the identifier of the entity (CkBox AssetId) ObjectTypeId is the definition of the Object (Lead, Invoice, Location, etc)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| OBJECTID | nvarchar | 100 | YES | ('') |
| OBJECTTYPEID | int |  | YES | (NULL) |
| TAGID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
