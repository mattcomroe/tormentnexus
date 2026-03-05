# FileStorage_CS2

## Tables

- [File](#file)
- [File_Archive](#file-archive)
- [FileMetadata_2](#filemetadata-2)
- [FileMetadata_Archive](#filemetadata-archive)
- [FileType](#filetype)
- [Folder](#folder)
- [FolderOrCategory](#folderorcategory)
- [FolderPermission](#folderpermission)
- [FolderPermissionsType](#folderpermissionstype)
- [Image](#image)
- [Image_Archive](#image-archive)
- [MediaFolder](#mediafolder)
- [MediaLibraryWorkspace](#medialibraryworkspace)
- [MIMEType](#mimetype)
- [NameIdentifier](#nameidentifier)
- [Source](#source)

## File
**Physical table:** `OSUSR_8E7_FILE`  
**Description:** Stores information related to a file  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TITLE | nvarchar | 250 | YES | ('') |
| NAME | nvarchar | 250 | YES | ('') |
| MIMETYPEID | bigint |  | YES | (NULL) |
| SIZE | int |  | YES | ((0)) |
| URI | nvarchar | 2000 | YES | ('') |
| EXTERNALID | nvarchar | 300 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## File_Archive
**Physical table:** `OSUSR_8E7_ARCHIVEFILE`  
**Description:** Stores information related to an archive file  

_Column definitions not found in schema export._

## FileMetadata_2
**Physical table:** `OSUSR_8E7_FILEMETADATA_2`  
**Description:** Holds metadata about a file stored  

_Column definitions not found in schema export._

## FileMetadata_Archive
**Physical table:** `OSUSR_8E7_ARCHIVEFILEMETADATA`  
**Description:** Holds metadata about a archive file stored  

_Column definitions not found in schema export._

## FileType
**Physical table:** `OSUSR_8E7_FILETYPE`  
**Description:** Type of files supported  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 100 | YES | ('') |

## Folder
**Physical table:** `OSUSR_8E7_FOLDER`  
**Description:** Contains information about a folder created to hold files  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LABEL | nvarchar | 100 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## FolderOrCategory
**Physical table:** `OSUSR_8E7_FOLDERORCATEGORY1`  
**Description:** contains Folder or Category values  

_Column definitions not found in schema export._

## FolderPermission
**Physical table:** `OSUSR_8E7_FOLDERPERMISSION1`  
**Description:** Stores the different permissions assigned to  folder in MediaFolder  

_Column definitions not found in schema export._

## FolderPermissionsType
**Physical table:** `OSUSR_8E7_FOLDERPERMISSIONSTYPE1`  
**Description:** Type of folder permissions for media library  

_Column definitions not found in schema export._

## Image
**Physical table:** `OSUSR_8E7_IMAGE`  
**Description:** If the entity File is an image, it will have a record here with the external properties for images  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| FILEID | bigint |  | NO |  |
| HEIGHT | int |  | YES | ((0)) |
| WIDTH | int |  | YES | ((0)) |
| FORMAT | nvarchar | 4 | YES | ('') |
| ISDEFAULT | bit |  | YES | ((0)) |

## Image_Archive
**Physical table:** `OSUSR_8E7_ARCHIVEIMAGE`  
**Description:** If the entity ArchiveFile is an image, it will have a record here with the external properties for images  

_Column definitions not found in schema export._

## MediaFolder
**Physical table:** `OSUSR_8E7_MEDIAFOLDER`  
**Description:** Stores the folder/category for a permission for CkBox  

_Column definitions not found in schema export._

## MediaLibraryWorkspace
**Physical table:** `OSUSR_8E7_MEDIALIBRARYWORKSPACE1`  
**Description:** Stores the Customer/Tenant's WorkspaceId for CkBox  

_Column definitions not found in schema export._

## MIMEType
**Physical table:** `OSUSR_8E7_MIMETYPE`  
**Description:** Store information about supported MIME Types.  The Multipurpose Internet Mail Extensions (MIME) type is a standardized way to indicate the nature and format of a document. It is defined and standardized in IETF RFC 6838. The Internet Assigned Numbers Authority (IANA) is the official body responsible for keeping track of all official MIME types, and you can find the most up-to-date and complete list at the Media Types page  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LABEL | nvarchar | 100 | YES | ('') |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| EXTENSIONS | nvarchar | 1000 | YES | ('') |
| FILETYPEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## NameIdentifier
**Physical table:** `OSUSR_8E7_NAMEIDENTIFIER`  
**Description:** Name identifier used to identify a file. Used with Identifier.  

_Column definitions not found in schema export._

## Source
**Physical table:** `OSUSR_8E7_SOURCE`  
**Description:** From where the request is done.  

_Column definitions not found in schema export._
