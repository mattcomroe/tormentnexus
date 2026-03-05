# Sample_Healthcare_CS

## Tables

- [Appointment](#appointment)
- [AppointmentStatus](#appointmentstatus)
- [BloodType](#bloodtype)
- [Doctor](#doctor)
- [DoctorLocation](#doctorlocation)
- [DoctorThumbnail](#doctorthumbnail)
- [HealthcareNews](#healthcarenews)
- [HealthcareNewsPicture](#healthcarenewspicture)
- [HealthCareOnboarding](#healthcareonboarding)
- [PatientDetail](#patientdetail)
- [Prescription](#prescription)
- [Speciality](#speciality)
- [SpecialityLocation](#specialitylocation)

## Appointment
**Physical table:** `OSUSR_pfn_Appointment`  
**Description:** Entity that holds the appointment records.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DOCTORID | bigint |  | YES | (NULL) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| STARTTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| APPOINTMENTSTATUSID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| SPECIALITYID | bigint |  | YES | (NULL) |
| DIAGNOSIS | nvarchar | 800 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## AppointmentStatus
**Physical table:** `OSUSR_pfn_AppointmentStatus`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| COLORID | nvarchar | 50 | YES | ('') |

## BloodType
**Physical table:** `OSUSR_pfn_BloodType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Doctor
**Physical table:** `OSUSR_pfn_Doctor`  
**Description:** Entity that holds the doctors records.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| SPECIALITY | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| RATING | decimal |  | YES | ((0)) |

## DoctorLocation
**Physical table:** `OSUSR_pfn_DoctorLocation`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DOCTORID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |

## DoctorThumbnail
**Physical table:** `OSUSR_pfn_DoctorThumbnail`  
**Description:** Entity that holds the records of Doctors thumbnails.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FILENAME | nvarchar | 50 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## HealthcareNews
**Physical table:** `OSUSR_pfn_HealthcareNews`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TITLE | nvarchar | 100 | YES | ('') |
| DESCRIPTION | nvarchar | -1 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## HealthcareNewsPicture
**Physical table:** `OSUSR_pfn_HealthcareNewsPicture`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FILENAME | nvarchar | 50 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## HealthCareOnboarding
**Physical table:** `OSUSR_pfn_HealthCareOnboarding`  
**Description:** Entity that holds the records of customer health care onboardings.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SOCIALSECURITYNUMBER | nvarchar | 25 | YES | ('') |
| INSURANCEMEMBERID | nvarchar | 25 | YES | ('') |
| HASMEDICALAID | bit |  | YES | ((0)) |
| ISEMPLOYED | bit |  | YES | ((0)) |
| HASPATIENTCONSENT | bit |  | YES | ((0)) |
| AGREEDTOTERMSANDCONDITIONS | bit |  | YES | ((0)) |
| AGREEDTOTELEMEDICINE | bit |  | YES | ((0)) |
| AGREEDTOPERSONALDATAUSAGE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PatientDetail
**Physical table:** `OSUSR_pfn_PatientDetail`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WEIGHT | int |  | YES | ((0)) |
| BLOODTYPEID | int |  | YES | (NULL) |
| ISBLOODDONOR | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Prescription
**Physical table:** `OSUSR_pfn_Prescription`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TEXT | nvarchar | 125 | YES | ('') |
| DOSAGE | int |  | YES | ((0)) |
| DURATION | int |  | YES | ((0)) |
| APPOINTMENTID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Speciality
**Physical table:** `OSUSR_pfn_Speciality`  
**Description:** Entity that holds the specialities records.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## SpecialityLocation
**Physical table:** `OSUSR_pfn_SpecialityLocation`  
**Description:** Entity that holds the speciality and the location records.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SPECIALITYID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
