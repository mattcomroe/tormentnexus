# WOD_CS

## Tables

- [Announcement](#announcement)
- [AsyncProcess](#asyncprocess)
- [BlogIntegration](#blogintegration)
- [BlogType](#blogtype)
- [ClientCalendarDefaultSetting](#clientcalendardefaultsetting)
- [Component](#component)
- [ComponentCategory](#componentcategory)
- [ComponentCopyHistory](#componentcopyhistory)
- [ComponentType](#componenttype)
- [ComponentVideo](#componentvideo)
- [ComponentVideoBlackList](#componentvideoblacklist)
- [CustomerHiddenComponentCategory](#customerhiddencomponentcategory)
- [EachRoundType](#eachroundtype)
- [MergeComponentsFirestore](#mergecomponentsfirestore)
- [MergeComponentsFirestoreStatus](#mergecomponentsfirestorestatus)
- [OwnershipLevel](#ownershiplevel)
- [Request](#request)
- [RequestType](#requesttype)
- [ResultType](#resulttype)
- [Scaling](#scaling)
- [TotalComponent](#totalcomponent)
- [WODComponent](#wodcomponent)
- [WODComponentMedia](#wodcomponentmedia)
- [WODComponentVariableReps](#wodcomponentvariablereps)
- [WODComponentVideo](#wodcomponentvideo)
- [WODComponentVideoBlackList](#wodcomponentvideoblacklist)
- [WODHeader](#wodheader)
- [WODHeaderLocation](#wodheaderlocation)
- [WODHeaderUserStar](#wodheaderuserstar)
- [WODImage](#wodimage)
- [WODSection](#wodsection)
- [WODSectionCopyHistory](#wodsectioncopyhistory)
- [WordPressPostStatus](#wordpresspoststatus)

## Announcement
**Physical table:** `OSUSR_3u1_Announcement`  
**Description:** Announcements to be used when a new workout is created  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| MESSAGE | nvarchar | -1 | YES | ('') |
| LINKIFIEDMESSAGE | nvarchar | -1 | YES | ('') |
| FROMDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| TODATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISEXTERNAL | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CONTENTID | bigint |  | YES | ((0)) |
| SENDPUSHNOTIFICATIONS | bit |  | YES | ((0)) |
| HASSENTPUSHNOTIFICATIONS | bit |  | YES | ((0)) |
| SENDNOTIFICATIONSDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |

## AsyncProcess
**Physical table:** `OSUSR_3u1_AsyncProcess`  
**Description:** Auxiliar entity that contains all asynchronous processes, which will run through the AP module in BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## BlogIntegration
**Physical table:** `OSUSR_72o_BlogIntegration`  
**Description:** Contains information about blogs using Wordpress  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ENABLEBLOGINTEGRATION | bit |  | YES | ((0)) |
| BLOGTYPEID | int |  | YES | (NULL) |
| RPCURL | nvarchar | 150 | YES | ('') |
| USERNAME | nvarchar | 50 | YES | ('') |
| PASSWORD | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PUBLISHDAYSBEFORE | int |  | YES | ((0)) |
| PUBLISHTIMEOFDAY | datetime |  | YES | ('1900-01-01 00:00:00') |
| PUBLISHTIMEZONE | int |  | YES | (NULL) |
| LINKTOPUBLICWHITEBOARD | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | NO | ((0)) |
| IANATIMEZONEID | bigint |  | YES | (NULL) |

## BlogType
**Physical table:** `OSUSR_72o_BlogType`  
**Description:** Contains all type of blogs  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## ClientCalendarDefaultSetting
**Physical table:** `OSUSR_3u1_ClientCalendarDefaultSetting`  
**Description:** It contains the default filters for workout calendar for each Client  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| LOCATIONIDS | nvarchar | 50 | YES | ('') |
| PROGRAMIDS | nvarchar | 500 | YES | ('') |

## Component
**Physical table:** `OSUSR_72o_Component`  
**Description:** Workout component.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| COMPONENTTYPEID | int |  | YES | (NULL) |
| OWNERSHIPLEVELID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| NAME | nvarchar | 300 | YES | ('') |
| DESCRIPTION | nvarchar | 4000 | YES | ('') |
| ISBENCHMARK | bit |  | YES | ((0)) |
| HASBEENSAVED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| ISNEWCOMPONENTEMAILSENT | bit |  | YES | ((0)) |
| ROUNDS | int |  | YES | ((0)) |
| EACHROUNDTYPEID | int |  | YES | (NULL) |
| LINKIFIEDDESCRIPTION | nvarchar | -1 | YES | ('') |
| SYSTEMCOMMENT | nvarchar | 2000 | YES | ('') |
| EXTERNALURL | nvarchar | 2000 | YES | ('') |
| RESULTTYPEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SCALINGID | int |  | YES | (NULL) |
| COMPONENTCATEGORYID | int |  | YES | (NULL) |
| VARIABLESETSREPSCOMPONENTID | int |  | YES |  |

## ComponentCategory
**Physical table:** `OSUSR_3u1_ComponentCategory`  
**Description:** Component Categories  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ComponentCopyHistory
**Physical table:** `OSUSR_3u1_ComponentCopyHistory`  
**Description:** Contains the Id of a source component (and Customer Id) and target component.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SOURCECOMPONENTID | int |  | YES | (NULL) |
| TARGETCOMPONENTID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SOURCECUSTOMERID | bigint |  | YES | ((0)) |
| TARGETCUSTOMERID | bigint |  | YES | ((0)) |

## ComponentType
**Physical table:** `OSUSR_72o_ComponentType`  
**Description:** Type of Components  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| PLURALLABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ComponentVideo
**Physical table:** `OSUSR_3u1_ComponentVideo`  
**Description:** Contains videos either by URL (youtube, vimeo, etc), or an identifier from an upload which is stored in Amazon S3  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COMPONENTID | int |  | YES | (NULL) |
| VIDEONAME | nvarchar | 200 | YES | ('') |
| VIDEOURL | nvarchar | 200 | YES | ('') |
| FILESTORAGEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| OWNERCUSTOMERID | bigint |  | YES | ((0)) |

## ComponentVideoBlackList
**Physical table:** `OSUSR_3u1_ComponentVideoBlackList`  
**Description:** Contains videos either by URL (youtube, vimeo, etc), or an identifier from an upload which is stored in Amazon S3  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COMPONENTVIDEOID | bigint |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| USERID | int |  | YES | (NULL) |

## CustomerHiddenComponentCategory
**Physical table:** `OSUSR_3u1_CustomerHiddenComponentCategory`  
**Description:** Contains a list of hidden component categories  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| COMPONENTCATEGORYID | int |  | YES | (NULL) |

## EachRoundType
**Physical table:** `OSUSR_72o_EachRoundType`  
**Description:** Types of Each Rounds for components  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## MergeComponentsFirestore
**Physical table:** `OSUSR_3u1_MergeComponentsFirestore`  
**Description:** Component IDs to be Merged in Firestore. Only used by a timer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FROMCOMPONENTID | int |  | YES | (NULL) |
| TOCOMPONENTID | int |  | YES | (NULL) |
| MERGESTATUSID | int |  | YES | (NULL) |

## MergeComponentsFirestoreStatus
**Physical table:** `OSUSR_3u1_MergeComponentsFirestoreStatus`  
**Description:** Table to track the status column of the MergeComponentsFirestore entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## OwnershipLevel
**Physical table:** `OSUSR_72o_OwnershipLevel`  
**Description:** definitions of who owns each component  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Request
**Physical table:** `OSUSR_3u1_Request`  
**Description:** Contains all requests made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| REQUESTTYPEID | int |  | YES | (NULL) |
| COMPONENTID | bigint |  | YES | ((0)) |
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
| FROMCOMPONENTID | bigint |  | YES | ((0)) |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |

## RequestType
**Physical table:** `OSUSR_3u1_RequestType`  
**Description:** Contains all request types that are possible to be made by our Customers or Customer's Clients, that will run in the background  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## ResultType
**Physical table:** `OSUSR_ddd_ResultType`  
**Description:** Contains all result types for components  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| ISALLOWEDFORMETCON | bit |  | YES | ((0)) |
| ISALLOWEDFORWEIGHTLIFTING | bit |  | YES | ((0)) |
| ISALLOWEDFORGYMNASTICS | bit |  | YES | ((0)) |
| ISALLOWEDFORWLTOTAL | bit |  | YES | ((0)) |
| DESCRIPTION | nvarchar | 50 | YES | ('') |
| SUPPORTSRX | bit |  | YES | ((0)) |
| SUPPORTSCHILDRESULTS | bit |  | YES | ((0)) |

## Scaling
**Physical table:** `OSUSR_3u1_Scaling`  
**Description:** Contains all possible Scaling options  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## TotalComponent
**Physical table:** `OSUSR_72o_TotalComponent`  
**Description:** for components composed by more than one component. To group components  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| PARENTCOMPONENTID | int |  | YES | (NULL) |
| COMPONENTID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## WODComponent
**Physical table:** `OSUSR_72o_WODComponent`  
**Description:** A Workout component  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| WODHEADERID | int |  | YES | (NULL) |
| COMPONENTTYPEID | int |  | YES | (NULL) |
| COMPONENTID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| MEASURECOMPONENTRESULTID | int |  | YES | (NULL) |
| WODSECTIONID | int |  | YES | (NULL) |
| COMMENT | nvarchar | 4000 | YES | ('') |
| SHOWCOMMENT | bit |  | YES | ((0)) |
| ISSECTIONHEADER | bit |  | YES | ((0)) |
| PREFIXTEXT | nvarchar | 5 | YES | ('') |
| HASMEASURE | bit |  | YES | ((0)) |
| MEASURESETS | int |  | YES | ((0)) |
| MEASUREREPS | int |  | YES | ((0)) |
| MEASUREROUNDS | int |  | YES | ((0)) |
| MEASUREHOURS | int |  | YES | ((0)) |
| MEASUREMINUTES | int |  | YES | ((0)) |
| MEASURESECONDS | int |  | YES | ((0)) |
| MEASUREDISTANCE | decimal |  | YES | ((0)) |
| MEASURECALORIES | int |  | YES | ((0)) |
| MEASUREWEIGHT | decimal |  | YES | ((0)) |
| MEASUREISMAXEFFORT | bit |  | YES | ((0)) |
| MEASUREREPSCHEME | nvarchar | 250 | YES | ('') |
| MEASUREUOMWEIGHTID | int |  | YES | (NULL) |
| MEASUREUOMDISTANCEID | int |  | YES | (NULL) |
| ORIGINALCOMPONENTID | int |  | YES | (NULL) |
| LINKIFIEDCOMMENT | nvarchar | -1 | YES | ('') |
| MOSTRECENTRESULTSENTERED | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISBENCHMARK | bit |  | YES | ((0)) |
| ISIMAGECOMPONENT | bit |  | YES | ((0)) |
| WODIMAGEID | bigint |  | YES | (NULL) |
| ISVIDEOURL | bit |  | YES | ((0)) |
| VIDEOURL | nvarchar | 200 | YES | ('') |
| VIDEOURLCOMMENT | nvarchar | 4000 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| VIDEONAME | nvarchar | 200 | YES | ('') |
| FILESTORAGEID | bigint |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## WODComponentMedia
**Physical table:** `OSUSR_3u1_WODComponentMedia`  
**Description:** Contains media or images either by URL, or an identifier from an upload which is stored in Amazon S3. For a specified Workout  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| WODCOMPONENTID | int |  | YES | (NULL) |
| MEDIANAME | nvarchar | 200 | YES | ('') |
| MEDIAURL | nvarchar | 200 | YES | ('') |
| FILESTORAGEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| COMMENT | nvarchar | 2000 | YES | ('') |

## WODComponentVariableReps
**Physical table:** `OSUSR_3u1_WODComponentVariableReps`  
**Description:** Holds the Rep Count for each Set of a WODComponent utilizing Variable Reps  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WODCOMPONENTID | int |  | YES | (NULL) |
| SET | int |  | YES | ((0)) |
| REPS | int |  | YES | ((0)) |
| SETISMAXEFFORT | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## WODComponentVideo
**Physical table:** `OSUSR_3u1_WODComponentVideo`  
**Description:** Contains videos either by URL (youtube, vimeo, etc), or an identifier from an upload which is stored in Amazon S3. For a specified Workout  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WODCOMPONENTID | int |  | YES | (NULL) |
| VIDEONAME | nvarchar | 200 | YES | ('') |
| VIDEOURL | nvarchar | 200 | YES | ('') |
| FILESTORAGEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## WODComponentVideoBlackList
**Physical table:** `OSUSR_3u1_WODComponentVideoBlackList`  
**Description:** Contains videos either by URL (youtube, vimeo, etc), or an identifier from an upload which is stored in Amazon S3, that are not supposed to show for a specified WODComponent  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| COMPONENTVIDEOID | bigint |  | YES | (NULL) |
| WODCOMPONENTID | int |  | YES | (NULL) |

## WODHeader
**Physical table:** `OSUSR_72o_WODHeader`  
**Description:** Workouts of the day.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| DATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| PUBLISHDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| NAME | nvarchar | 300 | YES | ('') |
| COMMENTS | nvarchar | 2000 | YES | ('') |
| OWNERSHIPLEVELID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| PROGRAMID | int |  | YES | (NULL) |
| BLOGPOSTID | nvarchar | 150 | YES | ('') |
| RESULTSPOSTED | bit |  | YES | ((0)) |
| HASBEENSAVED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| SHOULDPUBLISH | bit |  | YES | ((0)) |
| ISPOSTUPDATEREQUIRED | bit |  | YES | ((0)) |
| ISPOSTEDTOFACEBOOK | bit |  | YES | ((0)) |
| LASTEDITDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| WORDPRESSPOSTSTATUSID | int |  | YES | (NULL) |
| FACEBOOKPOSTID | nvarchar | 150 | YES | ('') |
| PUBLICID | nvarchar | 25 | YES | ('') |
| COPIEDFROMWODHEADERID | int |  | YES | (NULL) |
| ISFAVORITE | bit |  | YES | ((0)) |
| LINKIFIEDCOMMENTS | nvarchar | -1 | YES | ('') |
| ISFACEBOOKPOSTREQUIRED | bit |  | YES | ((0)) |
| FACEBOOKPOSTINGERROR | nvarchar | 500 | YES | ('') |
| INTERNALPUBLISHDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| SHOULDPUBLISHTOBLOG | bit |  | YES | ((0)) |
| BLOGPUBLISHDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| BLOGLINKTOPUBLICWHITEBOARD | bit |  | YES | ((0)) |
| SECUREPROGRAMMINGENABLED | bit |  | YES | ((0)) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| VIDEOLINKID | nvarchar | 20 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## WODHeaderLocation
**Physical table:** `OSUSR_72o_WODHeaderLocation`  
**Description:** Possible locations for each workout  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| WODHEADERID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## WODHeaderUserStar
**Physical table:** `OSUSR_ddd_WODHeaderUserStar`  
**Description:** Contains workouts that a client as Starred  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| USERID | int |  | YES | (NULL) |
| WODHEADERID | int |  | YES | (NULL) |
| ISSTARRED | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## WODImage
**Physical table:** `OSUSR_ddd_WODImage`  
**Description:** WOD Image entity. Has the references to the Amazon S3 buckets  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| FILEKEY | nvarchar | 50 | YES | ('') |
| IMAGECAPTION | nvarchar | -1 | YES | ('') |
| OWNERSHIPLEVELID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| FILESTORAGEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## WODSection
**Physical table:** `OSUSR_72o_WODSection`  
**Description:** Sections to group exercises  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| TITLE | nvarchar | 200 | YES | ('') |
| OWNERSHIPLEVELID | int |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## WODSectionCopyHistory
**Physical table:** `OSUSR_3u1_WODSectionCopyHistory`  
**Description:** Contains the Id of a source WOD Section (and Customer Id) and target WOD Section.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SOURCEWODSECTIONID | int |  | YES | (NULL) |
| SOURCETENANTID | int |  | YES | (NULL) |
| TARGETWODSECTIONID | int |  | YES | (NULL) |
| TARGETTENANTID | int |  | YES | (NULL) |
| SOURCECUSTOMERID | bigint |  | YES | ((0)) |
| TARGETCUSTOMERID | bigint |  | YES | ((0)) |

## WordPressPostStatus
**Physical table:** `OSUSR_72o_WordPressPostStatus`  
**Description:** Status of a workout post in wordpress  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
