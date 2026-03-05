# Sample_Employee_CS

## Tables

- [Department](#department)
- [Document](#document)
- [DocumentBinary](#documentbinary)
- [ELearningCourse](#elearningcourse)
- [ELearningCourseImage](#elearningcourseimage)
- [ELearningCourseStatus](#elearningcoursestatus)
- [ELearningCourseVideo](#elearningcoursevideo)
- [Employee](#employee)
- [EmployeeDocument](#employeedocument)
- [EmployeeDocumentSignatureStatus](#employeedocumentsignaturestatus)
- [EmployeeELearningCourse](#employeeelearningcourse)
- [EmployeeELearningCourseVideo](#employeeelearningcoursevideo)
- [EmployeeEquipment](#employeeequipment)
- [EmployeeOnboarding](#employeeonboarding)
- [EmployeeOnboardingStatus](#employeeonboardingstatus)
- [EmployeeThumbnail](#employeethumbnail)
- [Equipment](#equipment)
- [EquipmentImage](#equipmentimage)
- [JobPosition](#jobposition)

## Department
**Physical table:** `OSUSR_ije_Department`  
**Description:** Entity that holds the records of departments.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## Document
**Physical table:** `OSUSR_ije_Document`  
**Description:** Entity that holds the records of Documents  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 250 | YES | ('') |
| ISMANDATORYSIGNATURE | bit |  | YES | ((0)) |
| CANBEEDITED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## DocumentBinary
**Physical table:** `OSUSR_ije_DocumentBinary`  
**Description:** Entity that holds the records of Document binary  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| DOCUMENTID | bigint |  | NO |  |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 250 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ELearningCourse
**Physical table:** `OSUSR_ije_ELearningCourse`  
**Description:** Entity that holds the records of E-Learning Courses  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CODE | nvarchar | 50 | YES | ('') |
| NAME | nvarchar | 250 | YES | ('') |
| DESCRIPTION | nvarchar | 250 | YES | ('') |
| DURATION | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## ELearningCourseImage
**Physical table:** `OSUSR_ije_ELearningCourseImage`  
**Description:** Entity that holds the records of E-Learning Courses Images  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ELEARNINGCOURSEID | bigint |  | NO |  |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 50 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ELearningCourseStatus
**Physical table:** `OSUSR_ije_ELearningCourseStatus`  
**Description:** Entity that holds the records of E-Learning Courses Status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ELearningCourseVideo
**Physical table:** `OSUSR_ije_ELearningCourseVideo`  
**Description:** Entity that holds the records of E-Learning Courses Binary video  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ELEARNINGCOURSEID | bigint |  | YES | (NULL) |
| VIDEONAME | nvarchar | 250 | YES | ('') |
| VIDEOPATH | nvarchar | 200 | YES | ('') |
| DURATION | int |  | YES | ((0)) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Employee
**Physical table:** `OSUSR_ije_Employee`  
**Description:** Entity that holds the records of employees.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| BIRTHDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAIL | nvarchar | 250 | YES | ('') |
| PHONE | nvarchar | 20 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| JOBPOSITIONID | bigint |  | YES | (NULL) |
| BIO | nvarchar | 2000 | YES | ('') |
| HIRINGDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISPROVISIONING | bit |  | YES | ((0)) |
| MANAGERID | bigint |  | YES | (NULL) |
| DEPARTMENTID | bigint |  | YES | (NULL) |
| OFFICEID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ONBOARDINGSTATUSID | int |  | YES | (NULL) |
| EMPLOYEENUMBER | nvarchar | 50 | YES | ('') |

## EmployeeDocument
**Physical table:** `OSUSR_ije_EmployeeDocument`  
**Description:** Entity that holds the Employees Documents  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EMPLOYEEID | bigint |  | YES | (NULL) |
| DOCUMENTID | bigint |  | YES | (NULL) |
| SIGNATURESTATUSID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SIGNATURE | varbinary | -1 | YES | (NULL) |

## EmployeeDocumentSignatureStatus
**Physical table:** `OSUSR_ije_EmployeeDocumentSignatureStatus`  
**Description:** Entity that holds the Employees Signature status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## EmployeeELearningCourse
**Physical table:** `OSUSR_ije_EmployeeELearningCourse`  
**Description:** Entity that holds the records of E-Learning Courses of an Employee  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EMPLOYEEID | bigint |  | YES | (NULL) |
| ELEARNINGCOURSEID | bigint |  | YES | (NULL) |
| STATUSID | int |  | YES | (NULL) |
| VIDEOISWATCHED | bit |  | YES | ((0)) |
| STATUSPERCENTAGE | int |  | YES | ((0)) |

## EmployeeELearningCourseVideo
**Physical table:** `OSUSR_ije_EmployeeELearningCourseVideo`  
**Description:** Entity that holds the records of E-Learning Courses videos of an Employee  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| ELEARNINGCOURSEVIDEOID | bigint |  | YES | (NULL) |
| EMPLOYEEELEARNINGCOURSEID | bigint |  | YES | (NULL) |
| ISWATCHED | bit |  | YES | ((0)) |

## EmployeeEquipment
**Physical table:** `OSUSR_ije_EmployeeEquipment`  
**Description:** Entity that holds the records of Equipments of an Employee  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EMPLOYEEID | bigint |  | YES | (NULL) |
| EQUIPMENTID | bigint |  | YES | (NULL) |

## EmployeeOnboarding
**Physical table:** `OSUSR_ije_EmployeeOnboarding`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| BANKACCOUNTNUMBER | int |  | YES | ((0)) |
| SOCIALSECURITYNUMBER | int |  | YES | ((0)) |
| ADDRESS | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| STARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ONBOARDING_DAYZERO | datetime |  | YES | ('1900-01-01 00:00:00') |
| ONBOARDING_AFTERDAYONESTART | datetime |  | YES | ('1900-01-01 00:00:00') |
| ONBOARDING_AFTERDAYONEEND | datetime |  | YES | ('1900-01-01 00:00:00') |
| ONBOARDING_WEEKTWOSTART | datetime |  | YES | ('1900-01-01 00:00:00') |
| ONBOARDING_WEEKTWOEND | datetime |  | YES | ('1900-01-01 00:00:00') |
| ONBOARDING_WEEKTHREESTART | datetime |  | YES | ('1900-01-01 00:00:00') |
| ONBOARDING_WEEKTHREEEND | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## EmployeeOnboardingStatus
**Physical table:** `OSUSR_ije_EmployeeOnboardingStatus`  
**Description:** Employee Onboarding Status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## EmployeeThumbnail
**Physical table:** `OSUSR_ije_EmployeeThumbnail`  
**Description:** Entity that holds the records of Employees thumbnails.  

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

## Equipment
**Physical table:** `OSUSR_ije_Equipment`  
**Description:** Equipment available to onboard the employee  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CODE | nvarchar | 250 | YES | ('') |
| NAME | nvarchar | 250 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |

## EquipmentImage
**Physical table:** `OSUSR_ije_EquipmentImage`  
**Description:** Entity that holds the images of equipments.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| EQUIPMENTID | bigint |  | NO |  |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 250 | YES | ('') |
| BINARY | varbinary | -1 | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## JobPosition
**Physical table:** `OSUSR_ije_JobPosition`  
**Description:** Entity that holds the records of job positions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 100 | YES | ('') |
| ISHIRINGMANAGER | bit |  | YES | ((0)) |
| ISRECRUITER | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
