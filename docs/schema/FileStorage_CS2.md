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
**Physical table:** `OSUSR_8e7_File`  
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
**Physical table:** `OSUSR_8e7_ArchiveFile`  
**Description:** Stores information related to an archive file  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## FileMetadata_2
**Physical table:** `OSUSR_8e7_FileMetadata_2`  
**Description:** Holds metadata about a file stored  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## FileMetadata_Archive
**Physical table:** `OSUSR_8e7_ArchiveFileMetadata`  
**Description:** Holds metadata about a archive file stored  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## FileType
**Physical table:** `OSUSR_8e7_FileType`  
**Description:** Type of files supported  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 100 | YES | ('') |

## Folder
**Physical table:** `OSUSR_8e7_Folder`  
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
**Physical table:** `OSUSR_8e7_FolderOrCategory1`  
**Description:** contains Folder or Category values  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## FolderPermission
**Physical table:** `OSUSR_8e7_FolderPermission1`  
**Description:** Stores the different permissions assigned to  folder in MediaFolder  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## FolderPermissionsType
**Physical table:** `OSUSR_8e7_FolderPermissionsType1`  
**Description:** Type of folder permissions for media library  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## Image
**Physical table:** `OSUSR_8e7_Image`  
**Description:** If the entity File is an image, it will have a record here with the external properties for images  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| FILEID | bigint |  | NO |  |
| HEIGHT | int |  | YES | ((0)) |
| WIDTH | int |  | YES | ((0)) |
| FORMAT | nvarchar | 4 | YES | ('') |
| ISDEFAULT | bit |  | YES | ((0)) |

## Image_Archive
**Physical table:** `OSUSR_8e7_ArchiveImage`  
**Description:** If the entity ArchiveFile is an image, it will have a record here with the external properties for images  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## MediaFolder
**Physical table:** `OSUSR_8e7_MediaFolder`  
**Description:** Stores the folder/category for a permission for CkBox  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## MediaLibraryWorkspace
**Physical table:** `OSUSR_8e7_MediaLibraryWorkspace1`  
**Description:** Stores the Customer/Tenant's WorkspaceId for CkBox  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## MIMEType
**Physical table:** `OSUSR_8e7_MIMEType`  
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
**Physical table:** `OSUSR_8e7_NameIdentifier`  
**Description:** Name identifier used to identify a file. Used with Identifier.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## Source
**Physical table:** `OSUSR_8e7_Source`  
**Description:** From where the request is done.  

_Table not present in the dev environment — schema unavailable. May exist in production only._
