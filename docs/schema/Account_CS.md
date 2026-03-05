# Account_CS

## Tables

- [AsyncProcess](#asyncprocess)
- [ClientAppSettings](#clientappsettings)
- [CoachViewSettings](#coachviewsettings)
- [CustomPanelTemplate](#custompaneltemplate)
- [CustomPanelType](#custompaneltype)
- [Gender](#gender)
- [GlobalUser](#globaluser)
- [GlobalUserCustomer](#globalusercustomer)
- [GlobalUserCustomerRole](#globalusercustomerrole)
- [GlobalUserHistory](#globaluserhistory)
- [GlobalUserStatus](#globaluserstatus)
- [GlobalUserTermsConditions](#globalusertermsconditions)
- [GlobalUserTrustedDevice](#globalusertrusteddevice)
- [LeaderboardAgeFilters](#leaderboardagefilters)
- [LeaderboardGroupFilters](#leaderboardgroupfilters)
- [Product](#product)
- [Request](#request)
- [RequestRetainClientInitial](#requestretainclientinitial)
- [RequestType](#requesttype)
- [SocialLoginProviderType](#socialloginprovidertype)
- [TermsConditions](#termsconditions)
- [TVDisplay](#tvdisplay)
- [TVSettings](#tvsettings)
- [TVSettingsColumn](#tvsettingscolumn)
- [TVSettingsColumnAppointments](#tvsettingscolumnappointments)
- [TVSettingsColumnAppointmentsServices](#tvsettingscolumnappointmentsservices)
- [TVSettingsColumnCustom](#tvsettingscolumncustom)
- [TVSettingsColumnLeaderboard](#tvsettingscolumnleaderboard)
- [TVSettingsColumnLeaderboardAges](#tvsettingscolumnleaderboardages)
- [TVSettingsColumnLeaderboardLocation](#tvsettingscolumnleaderboardlocation)
- [TVSettingsColumnPerformance](#tvsettingscolumnperformance)
- [TVSettingsColumnPulse](#tvsettingscolumnpulse)
- [TVSettingsColumnResults](#tvsettingscolumnresults)
- [TVSettingsColumnResultsProgram](#tvsettingscolumnresultsprogram)
- [TVSettingsColumnSignIn](#tvsettingscolumnsignin)
- [TVSettingsColumnSignInProgram](#tvsettingscolumnsigninprogram)
- [TVSettingsColumnWorkout](#tvsettingscolumnworkout)
- [WeekStreaksForAppointmentsMap](#weekstreaksforappointmentsmap)

## AsyncProcess
**Physical table:** `OSUSR_8xw_AsyncProcess`  
**Description:** Auxiliar entity that contains all asynchronous processes, which will run through the AP module in BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ClientAppSettings
**Physical table:** `OSUSR_8xw_ClientAppSettings`  
**Description:** Contains persistent settings to be used exclusively for Wodify Client App  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HASDEBUGMODEACTIVE | bit |  | YES | ((0)) |
| ISDEBUGMODEACTIVE | bit |  | YES | ((0)) |
| ACTIONCOUNT_CALENDARSYNCMODA | int |  | YES | ((0)) |
| FIRSTDAYOFWEEK | int |  | YES | ((1)) |
| SENDICSEMAILS | bit |  | YES | ((1)) |
| ICSALTERNATEEMAIL | nvarchar | 250 | YES | ('') |
| HASSHOWNICSMODAL | bit |  | YES | ((0)) |
| APPAPPEARANCE | int |  | YES | ((0)) |
| CLIENTAPPANNOUNCEMENTGROUPID | bigint |  | YES | ((0)) |

## CoachViewSettings
**Physical table:** `OSUSR_8xw_CoachViewSettings`  
**Description:** Contains persistent settings to be used exclusively for Coach View in Wodify Client App  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| HASCOACHVIEWENABLED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| USEPRIORITYSORT | bit |  | YES | ((0)) |
| SENDCOACHICSEMAILS | bit |  | YES | ((1)) |
| COACHICSALTERNATEEMAIL | nvarchar | 250 | YES | ('') |
| SORTCLASSDETAIL | int |  | YES | ((1)) |
| SORTWORKOUTRESULTS | bit |  | YES | ((1)) |
| SORTAPPOINTMENTDETAIL | int |  | YES | ((1)) |

## CustomPanelTemplate
**Physical table:** `OSUSR_8xw_TVSettingsColumnCustomTemplate`  
**Description:** template for Custom Panels  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| URLOREMBEDCODE | nvarchar | 1000 | YES | ('') |
| ISURL | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LASTUPDATED | datetime |  | YES | (CONVERT([datetime],'1900-01-01 00:00:00',(120))) |
| CUSTOMPANELTYPEID | int |  | YES | (NULL) |
| MEDIALIBRARYURL | nvarchar | 500 | YES | ('') |
| MEDIALIBRARYNAME | nvarchar | 500 | YES | ('') |
| MEDIALIBRARYASSETID | nvarchar | 50 | YES | ('') |
| MEDIALIBRARYEXTENSION | nvarchar | 50 | YES | ('') |

## CustomPanelType
**Physical table:** `OSUSR_8xw_CustomPanelType`  
**Description:** Custom panel type - can be URL, embed code, or media library  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Gender
**Physical table:** `OSUSR_8xw_Gender2`  
**Description:** Gender entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## GlobalUser
**Physical table:** `OSUSR_fti_GlobalUser`  
**Description:** Entity to represent the aggregator Wodify Global User  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EMAIL | nvarchar | 250 | YES | ('') |
| PASSWORD | nvarchar | 256 | YES | ('') |
| FIRSTNAME | nvarchar | 50 | YES | ('') |
| LASTNAME | nvarchar | 50 | YES | ('') |
| GENDERID | int |  | YES | (NULL) |
| DATEOFBIRTH | datetime |  | YES | ('1900-01-01 00:00:00') |
| AGE | int |  | YES | ((0)) |
| PIN | nvarchar | 50 | YES | ('') |
| CLOUDINARYFILEID | int |  | YES |  |
| STREETADDRESS1 | nvarchar | 200 | YES | ('') |
| STREETADDRESS2 | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| PROVINCE | nvarchar | 50 | YES | ('') |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| INTERNATIONALMOBILEPHONE | nvarchar | 20 | YES | ('') |
| EMERGENCYCONTACTNAME | nvarchar | 100 | YES | ('') |
| EMERGENCYCONTACTPHONENUMBER | nvarchar | 20 | YES | ('') |
| TIMEZONEID | int |  | YES | (NULL) |
| WATERBOTTLESIZE | decimal |  | YES | ((0)) |
| WEIGHT | decimal |  | YES | ((0)) |
| BILLINGCCEMAIL | nvarchar | 250 | YES | ('') |
| MOBILEPHONE | nvarchar | 20 | YES | ('') |
| GLOBALUSERSTATUSID | int |  | YES | (NULL) |
| WEIGHTSYSTEMOFMEASURE | int |  | YES | (NULL) |
| DISTANCESYSTEMOFMEASURE | int |  | YES | (NULL) |
| HEIGHTMEASUREMENT1 | int |  | YES | ((0)) |
| HEIGHTMEASUREMENT2 | int |  | YES | ((0)) |
| ISNONGENDER | bit |  | YES | ((0)) |
| USERGUID | nvarchar | 36 | YES | ('') |
| IANATIMEZONEID | bigint |  | YES | (NULL) |
| GOOGLEAUTHENTICATORKEY | nvarchar | 50 | YES | ('') |
| EXTERNALLOGINPROVIDERUSERID | nvarchar | 50 | YES | ('') |
| EXTERNALLOGINPROVIDERID | int |  | YES | (NULL) |
| EXTERNALLOGINPROVIDERTYPEID | int |  | YES | (NULL) |
| SOCIALLOGINUSERID | nvarchar | 50 | YES | ('') |
| SOCIALLOGINPROVIDERTYPEID | int |  | YES | (NULL) |

## GlobalUserCustomer
**Physical table:** `OSUSR_fti_GlobalUserTenant`  
**Description:** Entity to associate a Global User with a Customer, i.e. represents a Wodify's account on a gym.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| GLOBALUSERID | int |  | YES | (NULL) |
| TENANTID | int |  | YES |  |
| ISDEFAULT | bit |  | YES | ((0)) |
| PRODUCTID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| CURRENTWEEKSTREAK | int |  | YES | ((0)) |
| HIGHESTWEEKSTREAK | int |  | YES | ((0)) |
| CURRENTWEEKSTREAKUPDATEDON | datetime |  | YES |  |
| ISACTIVE | bit |  | YES | ((0)) |
| NUMBEROFROWSINLISTS | int |  | YES | ((0)) |

## GlobalUserCustomerRole
**Physical table:** `OSUSR_8xw_GlobalUserCustomerRole`  
**Description:** Contains all roles each user is associated to  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERCUSTOMERID | int |  | YES | (NULL) |
| ROLEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## GlobalUserHistory
**Physical table:** `OSUSR_8xw_GlobalUserHistory`  
**Description:** Contains what was changed when GlobalUser was updated  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |
| HISTORY | nvarchar | -1 | YES | ('') |

## GlobalUserStatus
**Physical table:** `OSUSR_fti_GlobalUserStatus`  
**Description:** Entity to define the possible status where a Global User can be. Active - Global User migrated without needing confirmation. Confirmed - Global User that confirmed the account. Requires Confirmation - Global User that has a confirmation process pending. Blocked - Global User with some conflicts to be resolved.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## GlobalUserTermsConditions
**Physical table:** `OSUSR_fti_GlobalUserTermsConditions`  
**Description:** Entity to associate a Global User with the terms and conditions that he already accepted.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |
| TERMSCONDITIONSID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |

## GlobalUserTrustedDevice
**Physical table:** `OSUSR_8xw_GlobalUserTrustedDevice`  
**Description:** Entity to store trusted devices (cookie guid and device/browser info) for a global users two-factor authenticaion  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |
| TRUSTEDDEVICEGUID | nvarchar | 500 | YES | ('') |
| TRUSTEDDEVICEEXPIRESAT | datetime |  | YES | ('1900-01-01 00:00:00') |
| DEVICEUSERAGENTINFO | nvarchar | 500 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| DEVICELABEL | nvarchar | 50 | YES | ('') |

## LeaderboardAgeFilters
**Physical table:** `OSUSR_8xw_LeaderboardAgeFilters`  
**Description:** Age filter options for KioskPlus Leaderboard  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## LeaderboardGroupFilters
**Physical table:** `OSUSR_8xw_LeaderboardGroupFilters`  
**Description:** Group filter options for KioskPlus Leaderboard  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Product
**Physical table:** `OSUSR_8xw_Product`  
**Description:** Contains all Wodify Products. This will distinguish the Users that were created for specified Products (currently Gym and Arena)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| HASUSERACCOUNTS | bit |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_8xw_Request`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| REQUESTTYPEID | int |  | YES | (NULL) |
| ISRUNNINGSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISMANUALLYRETRIED | bit |  | YES | ((0)) |
| RETRIEDBY | int |  | YES | (NULL) |
| NUMBEROFTRIES | int |  | YES | ((0)) |
| ERRORMESSAGE | nvarchar | 500 | YES | ('') |
| HASFINISHED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |

## RequestRetainClientInitial
**Physical table:** `OSUSR_8xw_RequestRetainClientInitial`  
**Description:** Table to temporarily store the initial state of Clients and their At Risk values for a given Customer. Used for async purposes to compare against current state of Client's At Risk values once a customer changes their retain settings.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| ATRISKINITIAL | bit |  | YES | ((0)) |
| RETAINID | bigint |  | YES | ((0)) |

## RequestType
**Physical table:** `OSUSR_8xw_RequestType`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## SocialLoginProviderType
**Physical table:** `OSUSR_8xw_ExternalLoginProvider`  
**Description:** Supported providers for logging into Wodify through an external account/provider  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TermsConditions
**Physical table:** `OSUSR_fti_TermsConditions`  
**Description:** Entity to define the available versions of Terms and Conditions for the Client mobile application.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| TERMSANDCONDITIONS | nvarchar | -1 | YES | ('') |
| PUBLISHEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| PRODUCTID | int |  | YES | (NULL) |

## TVDisplay
**Physical table:** `OSUSR_8xw_TVDisplay`  
**Description:** Contains all Features that can be displayed in the Kiosk TV  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TVSettings
**Physical table:** `OSUSR_8xw_TVSettings`  
**Description:** Contains persistent settings to be used exclusively for Wodify TV  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ISBACKGROUNDDARK | bit |  | YES | ((0)) |
| LAYOUTNUMBEROFCOLUMNS | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| DEFAULTLOCATIONID | bigint |  | YES | ((0)) |
| DEFAULTPROGRAMID | bigint |  | YES | ((0)) |
| ADDSCREENMARGIN | bit |  | YES | ((0)) |
| ISVERTICALDISPLAY | bit |  | YES | ((0)) |
| BROWSERTABUNIQUEID | nvarchar | 150 | YES | ('') |
| GLOBALUSERCUSTOMERID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| NAME | nvarchar | 150 | YES | ('') |
| ISBOOTSTRAP | bit |  | YES | ((0)) |
| ORIGINALTEMPLATEID | bigint |  | YES | (NULL) |
| GRIDTEMPLATE | nvarchar | 500 | YES | ('') |

## TVSettingsColumn
**Physical table:** `OSUSR_8xw_TVSettingsColumn`  
**Description:** Contains persistent settings to be used exclusively for Wodify TV. Saves what kind of information it saves for each column  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COLUMNNUMBER | int |  | YES | ((0)) |
| TVDISPLAYID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| TVSETTINGSID | bigint |  | YES | (NULL) |
| ISMINIMIZED | bit |  | YES | ((0)) |
| COLUMNZOOM | int |  | YES | ((0)) |
| COLUMNSIZEPERCENTAGE | decimal |  | YES | ((0)) |
| COLUMNSIZEFR | nvarchar | 50 | YES | ('') |

## TVSettingsColumnAppointments
**Physical table:** `OSUSR_8xw_TVSettingsColumnAppointments`  
**Description:** Extends the TVSettingsColumn for Results Settings and Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| LOCATIONID | bigint |  | YES | ((0)) |

## TVSettingsColumnAppointmentsServices
**Physical table:** `OSUSR_8xw_TVSettingsColumnAppointmentsServices`  
**Description:** Extends the TVSettingsColumn for Results Settings and Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SERVICEID | bigint |  | YES | ((0)) |
| TVSETTINGSCOLUMNAPPTSID | bigint |  | YES | (NULL) |

## TVSettingsColumnCustom
**Physical table:** `OSUSR_8xw_TVSettingsColumnCustom`  
**Description:** Extends the TVSettingsColumn for Custom panel Settings and Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| URLOREMBEDCODE | nvarchar | 1000 | YES | ('') |
| ISURL | bit |  | YES | ((0)) |
| TEMPLATEID | bigint |  | YES | ((0)) |
| CUSTOMPANELTEMPLATEID | bigint |  | YES | ((0)) |
| CUSTOMPANELTYPEID | int |  | YES | (NULL) |
| MEDIALIBRARYURL | nvarchar | 500 | YES | ('') |
| MEDIALIBRARYNAME | nvarchar | 500 | YES | ('') |
| MEDIALIBRARYASSETID | nvarchar | 50 | YES | ('') |
| MEDIALIBRARYEXTENSION | nvarchar | 50 | YES | ('') |

## TVSettingsColumnLeaderboard
**Physical table:** `OSUSR_8xw_TVSettingsColumnLeaderboard`  
**Description:** Extends the TVSettingsColumn for Leaderboard Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | bigint |  | YES | ((0)) |
| PROGRAMID | bigint |  | YES | ((0)) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| UOMWEIGHTID | bigint |  | YES | ((0)) |
| GENDERID | int |  | YES | ((0)) |
| MINAGE | decimal |  | YES | ((0)) |
| MAXAGE | decimal |  | YES | ((0)) |
| DATEISTODAY | bit |  | YES | ((0)) |
| DATEISYESTERDAY | bit |  | YES | ((0)) |
| ISALLLOCATIONS | bit |  | YES | ((0)) |
| GROUPBYID | int |  | YES | (NULL) |
| LEADERBOARDUOMWEIGHTID | int |  | YES | (NULL) |
| LEADERBOARDUOMDISTANCEID | int |  | YES | (NULL) |
| ISGROUPBYALL | bit |  | YES | ((0)) |
| ISAUTOMATICSCROLLENABLED | bit |  | YES | ((0)) |

## TVSettingsColumnLeaderboardAges
**Physical table:** `OSUSR_8xw_TVSettingsColumnLeaderboardAges`  
**Description:** Extends the TVSettingsColumnLeaderboard so the saved Age filters  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TVSETTINGSCOLUMNLDID | bigint |  | YES | (NULL) |
| LEADERBOARDAGEFILTERID | int |  | YES | (NULL) |

## TVSettingsColumnLeaderboardLocation
**Physical table:** `OSUSR_8xw_TVSettingsColumnLeaderboardLocation`  
**Description:** Extends the TVSettingsColumnLeaderboard so the saved Age filters  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TVSETTINGSCOLUMNLDID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | ((0)) |

## TVSettingsColumnPerformance
**Physical table:** `OSUSR_8xw_TVSettingsColumnPerformance`  
**Description:** Extends the TVSettingsColumn for Performance Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TABID | bigint |  | YES | ((0)) |
| GLOBALUSERID | bigint |  | YES | ((0)) |
| COMPONENTTYPEID | bigint |  | YES | ((0)) |
| COMPONENTID | bigint |  | YES | ((0)) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TIMEID | bigint |  | YES | ((0)) |
| ISPRSSELECTED | bit |  | YES | ((0)) |
| ISNONBENCHMARKMETCON | bit |  | YES | ((0)) |
| RESULTTYPEID | int |  | YES | ((0)) |
| EACHROUNDTYPEID | int |  | YES | ((0)) |
| SCALINGID | int |  | YES | ((0)) |
| COMPONENTNAME | nvarchar | 300 | YES | ('') |
| DESCRIPTION | nvarchar | -1 | YES | ('') |

## TVSettingsColumnPulse
**Physical table:** `OSUSR_8xw_TVSettingsColumnPulse`  
**Description:** Extends the TVSettingsColumn for Pulse Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | bigint |  | YES | ((0)) |
| PROGRAMID | bigint |  | YES | ((0)) |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLASSID | bigint |  | YES | ((0)) |
| DATEISTODAY | bit |  | YES | ((0)) |
| DATEISYESTERDAY | bit |  | YES | ((0)) |

## TVSettingsColumnResults
**Physical table:** `OSUSR_8xw_TVSettingsColumnResults`  
**Description:** Extends the TVSettingsColumn for Results Settings and Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLASSID | bigint |  | YES | ((0)) |
| LOCATIONID | bigint |  | YES | ((0)) |
| DATEISTODAY | bit |  | YES | ((0)) |
| DATEISYESTERDAY | bit |  | YES | ((0)) |
| ISAUTOMATICALLYADVANCECLASS | bit |  | YES | ((0)) |

## TVSettingsColumnResultsProgram
**Physical table:** `OSUSR_8xw_TVSettingsColumnResultsProgram`  
**Description:** Extends the TVSettingsColumnPerform so the saved Programs  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROGRAMID | bigint |  | YES | ((0)) |
| TVSETTINGSCOLUMNRESULTSID | bigint |  | YES | (NULL) |

## TVSettingsColumnSignIn
**Physical table:** `OSUSR_8xw_TVSettingsColumnSignIn1`  
**Description:** Extends the TVSettingsColumn for Sign In Settings and Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CLASSID | bigint |  | YES | ((0)) |
| LOCATIONID | bigint |  | YES | ((0)) |
| ISALLCLASSESSELECTED | bit |  | YES | ((0)) |
| DATEISTODAY | bit |  | YES | ((0)) |
| DATEISYESTERDAY | bit |  | YES | ((0)) |
| CLASSLISTSORT | nvarchar | 50 | YES | ('') |

## TVSettingsColumnSignInProgram
**Physical table:** `OSUSR_8xw_TVSettingsColumnSignInProgram`  
**Description:** Extends the TVSettingsColumnPerform so the saved Programs  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROGRAMID | bigint |  | YES | ((0)) |
| TVSETTINGSCOLUMNSIGNINID | bigint |  | YES | (NULL) |

## TVSettingsColumnWorkout
**Physical table:** `OSUSR_8xw_TVSettingsColumnWorkout`  
**Description:** Extends the TVSettingsColumn for Workout Display  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | bigint |  | YES | ((0)) |
| PROGRAMID | bigint |  | YES | ((0)) |
| SHOWFULLWORKOUT | bit |  | YES | ((0)) |
| COMPONENTIDS | nvarchar | 300 | YES | ('') |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| SHOWANNOUNCEMENTS | bit |  | YES | ((0)) |
| DATEISTODAY | bit |  | YES | ((0)) |
| DATEISYESTERDAY | bit |  | YES | ((0)) |
| WORKOUTISANNOUNCEMENTSSELECT | bit |  | YES | ((0)) |
| ISANNOUNCEMENTSSELECTED | bit |  | YES | ((0)) |

## WeekStreaksForAppointmentsMap
**Physical table:** `OSUSR_8xw_WeekStreaksForAppointmentsMap`  
**Description:** Map containing GlobalUserCustomer's Weekstreak data before appointment checkin's are factored in, and after.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| GLOBALUSERCUSTOMERID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CURRENTWEEKSTREAK | int |  | YES | ((0)) |
| HIGHESTWEEKSTREAK | int |  | YES | ((0)) |
| CURRENTWEEKSTREAKUPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| NEW_CURRENTWEEKSTREAK | int |  | YES | ((0)) |
| NEW_HIGHESTWEEKSTREAK | int |  | YES | ((0)) |
| NEW_CURRENTWEEKSTREAKUPDATED | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| WASPROCESSED | bit |  | YES | ((0)) |
