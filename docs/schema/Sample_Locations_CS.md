# Sample_Locations_CS

## Tables

- [DayOfWeek](#dayofweek)
- [Location](#location)
- [LocationContact](#locationcontact)
- [LocationOpeningHours](#locationopeninghours)
- [LocationPictures](#locationpictures)
- [LocationType](#locationtype)

## DayOfWeek
**Physical table:** `OSUSR_0qa_DayOfWeek`  
**Description:** Entity that holds the records of type DayOfWeek.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| NAME | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |

## Location
**Physical table:** `OSUSR_0qa_Location`  
**Description:** Entity that holds the records of type Location.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LOCATIONTYPE | nvarchar | 50 | YES | (NULL) |
| NAME | nvarchar | 150 | YES | ('') |
| ADDRESS | nvarchar | 250 | YES | ('') |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| LAT | decimal |  | YES | ((0)) |
| LNG | decimal |  | YES | ((0)) |
| COUNTRYID | int |  | YES | (NULL) |
| COUNTRYSTATEID | int |  | YES | (NULL) |
| LOCATIONCONTACTID | bigint |  | YES | (NULL) |
| RATING | decimal |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## LocationContact
**Physical table:** `OSUSR_0qa_LocationContact`  
**Description:** Entity that holds the records of type LocationContact.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PHONE | nvarchar | 20 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| WEBSITE | nvarchar | 250 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## LocationOpeningHours
**Physical table:** `OSUSR_0qa_LocationOpeningHours`  
**Description:** Entity that holds the records of type LocationOpeningHours.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| OPENINGHOUR | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLOSINGHOUR | datetime |  | YES | ('1900-01-01 00:00:00') |
| DAYOFWEEKID | nvarchar | 50 | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## LocationPictures
**Physical table:** `OSUSR_0qa_LocationPictures`  
**Description:** Entity that holds the records of type LocationPicture.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| FILENAME | nvarchar | 500 | YES | ('') |
| FILETYPE | nvarchar | 250 | YES | ('') |
| FILE | varbinary | -1 | YES | (NULL) |
| ISCOVER | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## LocationType
**Physical table:** `OSUSR_0qa_LocationType`  
**Description:** Entity that holds the records of type LocationType.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TYPE | nvarchar | 50 | NO |  |
