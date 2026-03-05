# Client_CS

## Tables

- [ClientAppReview](#clientappreview)
- [ClientAppReviewBlacklist](#clientappreviewblacklist)
- [ClientAppSyncSettings](#clientappsyncsettings)
- [ClientScheduledDeactivation](#clientscheduleddeactivation)
- [CustomQuickNavLink](#customquicknavlink)
- [DefaultQuickNavLink](#defaultquicknavlink)
- [Group](#group)
- [GroupParticipant](#groupparticipant)
- [GroupParticipantType](#groupparticipanttype)
- [MemberDeactivationReason](#memberdeactivationreason)
- [MemberRelationship](#memberrelationship)
- [MemberRelationshipStatus](#memberrelationshipstatus)
- [MemberRelationshipType](#memberrelationshiptype)
- [MemberSettings](#membersettings)
- [MemberSettingsHistory](#membersettingshistory)
- [ReviewType](#reviewtype)
- [TriggerType](#triggertype)
- [UserEmployeeBiography](#useremployeebiography)
- [UserEmployeeBiographyLink](#useremployeebiographylink)
- [UserFileStorage](#userfilestorage)
- [UserGoogleAccount](#usergoogleaccount)
- [UserGoogleAccountServiceCalendar](#usergoogleaccountservicecalendar)
- [UserGoogleCalendar](#usergooglecalendar)
- [UserGoogleCalendarType](#usergooglecalendartype)
- [UserNylasAccount](#usernylasaccount)
- [UserNylasCalendar](#usernylascalendar)
- [UserQuickNavSettings](#userquicknavsettings)
- [UserSuspendedRoles](#usersuspendedroles)

## ClientAppReview
**Physical table:** `OSUSR_M0Z_CLIENTAPPREVIEW`  
**Description:** Tracks review and feedback left by clients in the app review popup  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REVIEWTYPEID | int |  | YES | (NULL) |
| TRIGGERTYPEID | int |  | YES | (NULL) |
| GLOBALUSERID | int |  | YES | (NULL) |
| LEFTFEEDBACK | bit |  | YES | ((0)) |
| USERID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PROMPTEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ClientAppReviewBlacklist
**Physical table:** `OSUSR_M0Z_CLIENTAPPREVIEWBLACKLIST`  
**Description:** Holds list of clients that will never see app review prompts  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| GLOBALUSERID | int |  | YES | (NULL) |

## ClientAppSyncSettings
**Physical table:** `OSUSR_HWC_CLIENTAPPSETTINGS`  
**Description:** Contains persistent settings to be used exclusively for Wodify Client App  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CALENDARSYNCAPPLE | bit |  | YES | ((0)) |
| CALENDARSYNCGOOGLE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| GOOGLECALENDARID | int |  | YES | ((0)) |

## ClientScheduledDeactivation
**Physical table:** `OSUSR_M0Z_CLIENTSCHEDULEDDEACTIVATION`  
**Description:** Request and status data for async scheduled client deactivation process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DEACTIVATIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| MEMBERPLANID | bigint |  | YES | ((0)) |

## CustomQuickNavLink
**Physical table:** `OSUSR_M0Z_CUSTOMQUICKNAVLINK`  
**Description:** Custom links for Quick Nav  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| NAME | nvarchar | 30 | YES | ('') |
| ICON | nvarchar | 50 | YES | ('') |
| URL | nvarchar | -1 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |

## DefaultQuickNavLink
**Physical table:** `OSUSR_M0Z_DEFAULTQUICKNAVLINK`  
**Description:** Default links for Quick Nav  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 30 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| ICON | nvarchar | 50 | YES | ('') |
| SHORTCUTTEXT | nvarchar | 50 | YES | ('') |

## Group
**Physical table:** `OSUSR_H1I_GROUP`  
**Description:** The group of participants  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| IS_ACTIVE | bit |  | YES | ((0)) |
| TENANT_ID2 | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## GroupParticipant
**Physical table:** `OSUSR_H1I_GROUPPARTICIPANT`  
**Description:** Contains a group of clients with types within a group  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| GROUPID | bigint |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| GROUPPARTICIPANTTYPEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LEADGROUPPARTICIPANTID | bigint |  | YES | (NULL) |

## GroupParticipantType
**Physical table:** `OSUSR_H1I_GROUPPARTICIPANTTYPE`  
**Description:** Group participant type (for instance guardians, members, dependents)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## MemberDeactivationReason
**Physical table:** `OSUSR_HWC_MEMBERDEACTIVATIONREASON`  
**Description:** Indicates why a Members was deactivated  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## MemberRelationship
**Physical table:** `OSUSR_72O_MEMBERRELATIONSHIP`  
**Description:** Entity for a relationship between a ParentUser and a ChildUser  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PARENTUSERID | int |  | YES | (NULL) |
| CHILDUSERID | int |  | YES | (NULL) |
| MEMBERRELATIONSHIPTYPEID | int |  | YES | (NULL) |
| MEMBERRELATIONSHIPSTATUSID | int |  | YES | (NULL) |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MemberRelationshipStatus
**Physical table:** `OSUSR_72O_MEMBERRELATIONSHIPSTATUS`  
**Description:** Entity for the status of a relationship. Can be Current or Past  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## MemberRelationshipType
**Physical table:** `OSUSR_72O_MEMBERRELATIONSHIPTYPE`  
**Description:** Entity for the Type of a relationship (Family, Coworker, Friend, Acquantaince, or Other)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## MemberSettings
**Physical table:** `OSUSR_HWC_MEMBERSETTINGS`  
**Description:** Contains all Settings for a specific Member (Client)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| HASLOGGEDINBEFORE | bit |  | YES | ((0)) |
| LOCATIONID | int |  | YES | (NULL) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| ISINITIALWELCOMEEMAILSENT | bit |  | YES | ((0)) |
| ISSUSPENDED | bit |  | YES | ((0)) |
| ATHLETESTATUSPICKLISTVALUEID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| LEADSOURCEPICKLISTVALUEID | int |  | YES | (NULL) |
| REFERRINGUSER | int |  | YES | (NULL) |
| CONVERTEDFROMLEAD | bit |  | YES | ((0)) |
| MEMBERDEACTIVATIONREASONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| NUTRITIONCOACHID | int |  | YES | (NULL) |
| UOMWEIGHTID | int |  | YES | (NULL) |
| UOMDISTANCEID | int |  | YES | (NULL) |
| BALANCEDUE | decimal |  | YES | ((0)) |
| UNIQUEKEY | nvarchar | 25 | YES | ('') |
| YUBICOSECURITYKEY | nvarchar | 12 | YES | ('') |
| MASSEMAILSUBSCRIBED | bit |  | YES | ((0)) |
| MEMBERSINCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TAXIDENTIFICATIONNUMBER | nvarchar | 20 | YES | ('') |
| LASTATTENDANCE | datetime |  | YES | ('1900-01-01 00:00:00') |
| HIDENAMEINCLASSLIST | bit |  | YES | ((0)) |
| HIDEPRSINLEADERBOARD | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ISBIRTHDAYPRIVATE | bit |  | YES | ((0)) |
| LASTCONTACTED | datetime |  | YES | ('1900-01-01 00:00:00') |
| RETAINSNOOZEUNTILDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| DEFAULTTAB | int |  | YES | ((1)) |
| CLIENTOWNERID | int |  | YES | (NULL) |
| TOTALCLASSSIGNINS | int |  | YES | ((0)) |
| TOTALBOOKINGCHECKINS | int |  | YES | ((0)) |
| TOTALBOOKINGSIGNINS | int |  | YES | ((0)) |
| LASTCLASSSIGNIN | datetime |  | YES | ('1900-01-01 00:00:00') |
| LASTBOOKINGSIGNIN | datetime |  | YES | ('1900-01-01 00:00:00') |
| PRSTARTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISCORENAVDARK | bit |  | YES | ((0)) |

## MemberSettingsHistory
**Physical table:** `OSUSR_HWC_MEMBERSETTINGSHISTORY`  
**Description:** Contains what was changed when Member was updated  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| MEMBERSETTINGSID | int |  | YES | (NULL) |
| HISTORY | nvarchar | -1 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## ReviewType
**Physical table:** `OSUSR_M0Z_REVIEWTYPE`  
**Description:** Dictionary holding values for tyoes of appstore review (negative/neutral/positive)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TriggerType
**Physical table:** `OSUSR_M0Z_TRIGGERTYPE`  
**Description:** Holds possible values on when the user was prompted for app review  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## UserEmployeeBiography
**Physical table:** `OSUSR_M0Z_USEREMPLOYEEBIOGRAPHY`  
**Description:** Stores information related to an employee's bio.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| TITLE | nvarchar | 250 | YES | ('') |
| BIOGRAPHY | nvarchar | -1 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## UserEmployeeBiographyLink
**Physical table:** `OSUSR_M0Z_USEREMPLOYEEBIOGRAPHYLINK`  
**Description:** Stores links for Employee Bio  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USEREMPLOYEEBIOGRAPHYID | bigint |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| ICON | nvarchar | 50 | YES | ('') |
| URL | nvarchar | -1 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| USERID | int |  | YES | (NULL) |

## UserFileStorage
**Physical table:** `OSUSR_H1I_USERRACKSPACEFILE`  
**Description:** Contains all the files associated with the User  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| FILESTORAGEID | int |  | YES | (NULL) |

## UserGoogleAccount
**Physical table:** `OSUSR_H1I_USERGOOGLEACCOUNT`  
**Description:** Relationship between GoogleAccounts and users. This model assumes an account may be shared by several users.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| GOOGLEACCOUNTID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| SYNCTYPE | int |  | YES | ((0)) |
| ISSETUPCOMPLETE | bit |  | YES | ((0)) |
| ISSETUPONNEWAPPOINTMENTS | bit |  | YES | ((0)) |

## UserGoogleAccountServiceCalendar
**Physical table:** `OSUSR_H1I_USERGOOGLEACCOUNTSERVICECALENDAR`  
**Description:** Table to hold configuration for the service calendar for the google account  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| USERGOOGLEACCOUNTID | bigint |  | NO |  |
| HEXCOLOR | nvarchar | 8 | YES | ('') |

## UserGoogleCalendar
**Physical table:** `OSUSR_H1I_USERGOOGLECALENDAR`  
**Description:** Relation between a user and a Google Calendar, indicating the the user has chosen to synchronize their appointments with the calendar.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| GOOGLECALENDARID | bigint |  | YES | (NULL) |
| SYNCTYPE | int |  | YES | ((0)) |
| USERGOOGLECALENDARTYPEID | int |  | YES | (NULL) |

## UserGoogleCalendarType
**Physical table:** `OSUSR_HWC_USERGOOGLECALENDARTYPE`  
**Description:** Stores the type of google calendars  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## UserNylasAccount
**Physical table:** `OSUSR_M0Z_USERNYLASACCOUNT`  
**Description:** Associates a NylasAccount with a user  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| NYLASACCOUNTID | bigint |  | YES | (NULL) |

## UserNylasCalendar
**Physical table:** `OSUSR_M0Z_USERNYLASCALENDAR`  
**Description:** Associates a NylasCalendar with a user and contains user-specific settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERID | int |  | YES | (NULL) |
| NYLASCALENDARID | bigint |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| ENABLEIMPORT | bit |  | YES | ((0)) |
| ENABLEEXPORT | bit |  | YES | ((0)) |
| NICKNAME | nvarchar | 50 | YES | ('') |
| ISCUSTOMERCALENDAR | bit |  | YES | ((0)) |

## UserQuickNavSettings
**Physical table:** `OSUSR_M0Z_USERQUICKNAVSETTINGS`  
**Description:** User Quick Nav settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LINK1_LINKID | bigint |  | YES | ((0)) |
| LINK1_ISDEFAULT | bit |  | YES | ((0)) |
| LINK2_LINKID | bigint |  | YES | ((0)) |
| LINK2_ISDEFAULT | bit |  | YES | ((0)) |
| LINK3_LINKID | bigint |  | YES | ((0)) |
| LINK3_ISDEFAULT | bit |  | YES | ((0)) |
| LINK4_LINKID | bigint |  | YES | ((0)) |
| LINK4_ISDEFAULT | bit |  | YES | ((0)) |
| LINK5_LINKID | bigint |  | YES | ((0)) |
| LINK5_ISDEFAULT | bit |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| ISEDITNAVBAROPEN | bit |  | YES | ((0)) |

## UserSuspendedRoles
**Physical table:** `OSUSR_72O_USERSUSPENDEDROLES`  
**Description:** Holds the roles that a user has while they or their Customer is suspended. These roles are not active until the user/Customer are reinstated.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| HASADMIN | bit |  | YES | ((0)) |
| HASMANAGER | bit |  | YES | ((0)) |
| HASCOACH | bit |  | YES | ((0)) |
| HASSTAFF | bit |  | YES | ((0)) |
| HASATHLETE | bit |  | YES | ((0)) |
| HASBILLINGADMIN | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
