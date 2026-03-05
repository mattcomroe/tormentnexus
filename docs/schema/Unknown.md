# Unknown

## Tables

- [ANDROID_CONFIG_DETAILS](#android-config-details)
- [APP_VERSION_MODULE_VERSION](#app-version-module-version)
- [APPLICATION](#application)
- [APPLICATION_VERSION](#application-version)
- [COMPONENTPR](#componentpr)
- [IOS_CONFIG_DETAILS](#ios-config-details)
- [LEADERBOARD](#leaderboard)
- [LEVELS_ACHIEVED](#levels-achieved)
- [Log_Cyclic_Job](#log-cyclic-job)
- [Log_Cyclic_Job_Previous](#log-cyclic-job-previous)
- [Log_Error](#log-error)
- [Log_Error_Previous](#log-error-previous)
- [Log_Extension](#log-extension)
- [Log_Extension_Previous](#log-extension-previous)
- [Log_General](#log-general)
- [Log_General_Previous](#log-general-previous)
- [Log_Integration](#log-integration)
- [Log_Integration_Detail](#log-integration-detail)
- [Log_Integration_Detail_Previous](#log-integration-detail-previous)
- [Log_Integration_Previous](#log-integration-previous)
- [Log_Mobile_Request](#log-mobile-request)
- [Log_Mobile_Request_Detail](#log-mobile-request-detail)
- [Log_Mobile_Request_Detail_Previous](#log-mobile-request-detail-previous)
- [Log_Mobile_Request_Previous](#log-mobile-request-previous)
- [Log_RequestEvent](#log-requestevent)
- [Log_RequestEvent_Previous](#log-requestevent-previous)
- [Log_Screen](#log-screen)
- [Log_Screen_Previous](#log-screen-previous)
- [Log_ServiceAPI](#log-serviceapi)
- [Log_ServiceAPI_Detail](#log-serviceapi-detail)
- [Log_ServiceAPI_Detail_Previous](#log-serviceapi-detail-previous)
- [Log_ServiceAPI_Previous](#log-serviceapi-previous)
- [Log_Web_Reference](#log-web-reference)
- [Log_Web_Reference_Previous](#log-web-reference-previous)
- [Log_Web_Service](#log-web-service)
- [Log_Web_Service_Previous](#log-web-service-previous)
- [oslog_general_summary](#oslog-general-summary)
- [oslog_integration_summary](#oslog-integration-summary)
- [oslog_mobile_request_summary](#oslog-mobile-request-summary)
- [oslog_screen_summary](#oslog-screen-summary)
- [oslog_srvapi_summary](#oslog-srvapi-summary)
- [OSSYS_AREA](#ossys-area)
- [OSSYS_AREA_ENTRY_POINT](#ossys-area-entry-point)
- [OSSYS_ASSEMBLY](#ossys-assembly)
- [OSSYS_ASSEMBLY_DEPENDENCY](#ossys-assembly-dependency)
- [OSSYS_ESPACE_RUNTIME](#ossys-espace-runtime)
- [ossys_Meta_Cyclic_Job](#ossys-meta-cyclic-job)
- [ossys_Tenant](#ossys-tenant)
- [SEGMENT_AUDIT](#segment-audit)
- [snap_oslog_Cyclic_Job](#snap-oslog-cyclic-job)
- [snap_oslog_Cyclic_Job_Previous](#snap-oslog-cyclic-job-previous)
- [snap_oslog_Error](#snap-oslog-error)
- [snap_oslog_Error_Previous](#snap-oslog-error-previous)
- [snap_oslog_Extension](#snap-oslog-extension)
- [snap_oslog_Extension_Previous](#snap-oslog-extension-previous)
- [snap_oslog_General](#snap-oslog-general)
- [snap_oslog_General_Previous](#snap-oslog-general-previous)
- [snap_oslog_Int_Detail](#snap-oslog-int-detail)
- [snap_oslog_Int_Detail_Previous](#snap-oslog-int-detail-previous)
- [snap_oslog_Integration](#snap-oslog-integration)
- [snap_oslog_Integration_Previous](#snap-oslog-integration-previous)
- [snap_oslog_mobile_request](#snap-oslog-mobile-request)
- [snap_oslog_mobile_request_Previous](#snap-oslog-mobile-request-previous)
- [snap_oslog_MR_Detail](#snap-oslog-mr-detail)
- [snap_oslog_MR_Detail_Previous](#snap-oslog-mr-detail-previous)
- [snap_oslog_Parameter](#snap-oslog-parameter)
- [snap_oslog_RequestEvent](#snap-oslog-requestevent)
- [snap_oslog_RequestEvent_Previous](#snap-oslog-requestevent-previous)
- [snap_oslog_Screen](#snap-oslog-screen)
- [snap_oslog_Screen_Previous](#snap-oslog-screen-previous)
- [snap_oslog_SrvAPI](#snap-oslog-srvapi)
- [snap_oslog_SrvAPI_Detail](#snap-oslog-srvapi-detail)
- [snap_oslog_SrvAPI_Detail_Previous](#snap-oslog-srvapi-detail-previous)
- [snap_oslog_SrvAPI_Previous](#snap-oslog-srvapi-previous)
- [snap_oslog_Web_Reference](#snap-oslog-web-reference)
- [snap_oslog_Web_Reference_Previous](#snap-oslog-web-reference-previous)
- [snap_oslog_Web_Service](#snap-oslog-web-service)
- [snap_oslog_Web_Service_Previous](#snap-oslog-web-service-previous)
- [TENANTLIFTCOMPONENTTOTAL](#tenantliftcomponenttotal)
- [TENANTPRTOTAL](#tenantprtotal)
- [UCT_REPORTING_ETL_UPDATE_TIME](#uct-reporting-etl-update-time)
- [UCT_RETAIN](#uct-retain)
- [USERPRTOTAL](#userprtotal)
- [WORKATO_RECIPE_DATA](#workato-recipe-data)
- [WORKATO_RECIPE_DATA_UPDATE_TIME](#workato-recipe-data-update-time)
- [YEARREVIEW](#yearreview)
- [YR_PERFORMANCE_TMP](#yr-performance-tmp)

## ANDROID_CONFIG_DETAILS
**Physical table:** `OSSYS_ANDROID_CONFIG_DETAILS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| KEYSTORE | bigint |  | YES | (NULL) |
| ALIAS | nvarchar | 255 | YES | ('') |
| ALIASPASSWORD | nvarchar | 255 | YES | ('') |
| APPLICATIONID | nvarchar | 255 | YES | ('') |
| BUILDTYPE | nvarchar | 50 | YES | (NULL) |

## APP_VERSION_MODULE_VERSION
**Physical table:** `ossys_app_version_module_versi`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| APP_VERSION_ID | int |  | YES | (NULL) |
| MODULE_KIND_ID | int |  | YES | (NULL) |
| ESPACE_VERSION_ID | int |  | YES | (NULL) |
| EXTENSION_VERSION_ID | int |  | YES | (NULL) |
| IS_DEPENDENCY | bit |  | YES | ((0)) |

## APPLICATION
**Physical table:** `ossys_application`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| ENTRY_ESPACE_ID | int |  | YES | (NULL) |
| BACKOFFICE_ESPACE_ID | int |  | YES | (NULL) |
| DEFAULTTHEMEISMOBILE | bit |  | YES | ((0)) |
| KEY | nvarchar | 100 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| DISABLED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| APPLICATIONKIND | nvarchar | 50 | YES | (NULL) |
| TEMPLATEKEY | nvarchar | 50 | YES | ('') |
| PRIMARYCOLOR | nvarchar | 50 | YES | ('') |
| NATIVEHASH | nvarchar | 50 | YES | ('') |

## APPLICATION_VERSION
**Physical table:** `ossys_app_version`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| APPLICATIONID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## COMPONENTPR
**Physical table:** `[YearReviewDB].[dbo].[OSUSR_R4Q_COMPONENTPR]`  

_Column definitions unavailable — table is in a restricted external database (`YearReviewDB`). Elevated database access required._

## IOS_CONFIG_DETAILS
**Physical table:** `OSSYS_IOS_CONFIG_DETAILS`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| IOS_APPLICATION_IDENTIFIER | nvarchar | 255 | YES | ('') |
| IOS_CERTIFICATE | bigint |  | YES | (NULL) |
| IOS_PROV_PROFILE | bigint |  | YES | (NULL) |
| IOS_BUILDTYPE | nvarchar | 50 | YES | (NULL) |

## LEADERBOARD
**Physical table:** `[YearReviewDB].[dbo].[OSUSR_R4Q_LEADERBOARD]`  

_Column definitions unavailable — table is in a restricted external database (`YearReviewDB`). Elevated database access required._

## LEVELS_ACHIEVED
**Physical table:** `[YearReviewDB].[dbo].[OSUSR_R4Q_LEVELS_ACHIEVED]`  

_Column definitions unavailable — table is in a restricted external database (`YearReviewDB`). Elevated database access required._

## Log_Cyclic_Job
**Physical table:** `OSLOG_CYCLIC_JOB`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Cyclic_Job_Previous
**Physical table:** `OSLOG_CYCLIC_JOB_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Error
**Physical table:** `OSLOG_ERROR`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Error_Previous
**Physical table:** `OSLOG_ERROR_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Extension
**Physical table:** `OSLOG_EXTENSION`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Extension_Previous
**Physical table:** `OSLOG_EXTENSION_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_General
**Physical table:** `OSLOG_GENERAL`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_General_Previous
**Physical table:** `OSLOG_GENERAL_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Integration
**Physical table:** `OSLOG_INTEGRATION`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Integration_Detail
**Physical table:** `OSLOG_INT_DETAIL`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Integration_Detail_Previous
**Physical table:** `OSLOG_INT_DETAIL_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Integration_Previous
**Physical table:** `OSLOG_INTEGRATION_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Mobile_Request
**Physical table:** `OSLOG_MOBILE_REQUEST`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Mobile_Request_Detail
**Physical table:** `OSLOG_MR_DETAIL`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Mobile_Request_Detail_Previous
**Physical table:** `OSLOG_MR_DETAIL_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Mobile_Request_Previous
**Physical table:** `OSLOG_MOBILE_REQUEST_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_RequestEvent
**Physical table:** `OSLOG_REQUESTEVENT`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_RequestEvent_Previous
**Physical table:** `OSLOG_REQUESTEVENT_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Screen
**Physical table:** `OSLOG_SCREEN`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Screen_Previous
**Physical table:** `OSLOG_SCREEN_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_ServiceAPI
**Physical table:** `OSLOG_SRVAPI`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_ServiceAPI_Detail
**Physical table:** `OSLOG_SRVAPI_DETAIL`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_ServiceAPI_Detail_Previous
**Physical table:** `OSLOG_SRVAPI_DETAIL_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_ServiceAPI_Previous
**Physical table:** `OSLOG_SRVAPI_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Web_Reference
**Physical table:** `OSLOG_WEB_REFERENCE`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Web_Reference_Previous
**Physical table:** `OSLOG_WEB_REFERENCE_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Web_Service
**Physical table:** `OSLOG_WEB_SERVICE`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## Log_Web_Service_Previous
**Physical table:** `OSLOG_WEB_SERVICE_PREVIOUS`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## oslog_general_summary
**Physical table:** `[OSLog_Summary].[dbo].[oslog_general_summary]`  

_Column definitions unavailable — table is in a restricted external database (`OSLog_Summary`). Elevated database access required._

## oslog_integration_summary
**Physical table:** `[OSLog_Summary].[dbo].[oslog_integration_summary]`  

_Column definitions unavailable — table is in a restricted external database (`OSLog_Summary`). Elevated database access required._

## oslog_mobile_request_summary
**Physical table:** `[OSLog_Summary].[dbo].[oslog_mobile_request_summary]`  

_Column definitions unavailable — table is in a restricted external database (`OSLog_Summary`). Elevated database access required._

## oslog_screen_summary
**Physical table:** `[OSLog_Summary].[dbo].[oslog_screen_summary]`  

_Column definitions unavailable — table is in a restricted external database (`OSLog_Summary`). Elevated database access required._

## oslog_srvapi_summary
**Physical table:** `[OSLog_Summary].[dbo].[oslog_srvapi_summary]`  

_Column definitions unavailable — table is in a restricted external database (`OSLog_Summary`). Elevated database access required._

## OSSYS_AREA
**Physical table:** `OSSYS_AREA`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ESPACE_ID | int |  | YES | (NULL) |
| USER_ID | int |  | YES | (NULL) |

## OSSYS_AREA_ENTRY_POINT
**Physical table:** `OSSYS_AREA_ENTRY_POINT`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| AREA_ID | int |  | YES | (NULL) |
| NAME | nvarchar | 50 | YES | ('') |
| IS_DEFAULT | bit |  | YES | ((0)) |

## OSSYS_ASSEMBLY
**Physical table:** `OSSYS_ASSEMBLY`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| AREA_ID | int |  | YES | (NULL) |
| ESPACE_ID | int |  | YES | (NULL) |
| EXTENSION_ID | int |  | YES | (NULL) |
| HASH | nvarchar | 1000 | YES | ('') |
| SIGNATURE | ntext | 1073741823 | YES | ('') |
| IN_DEBUG | bit |  | YES | ((0)) |
| DEBUGGER_VERSION | nvarchar | 10 | YES | ('') |
| COMPILEDBUTNOTDEPLOYEDHASH | nvarchar | 1000 | YES | ('') |

## OSSYS_ASSEMBLY_DEPENDENCY
**Physical table:** `OSSYS_ASSEMBLY_DEPENDENCY`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ASSEMBLY_ID | int |  | YES | (NULL) |
| ESPACE_ID | int |  | YES | (NULL) |
| EXTENSION_ID | int |  | YES | (NULL) |
| SIGNATURE_IN_USE | ntext | 1073741823 | YES | ('') |

## OSSYS_ESPACE_RUNTIME
**Physical table:** `OSSYS_ESPACE_RUNTIME`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ESPACE_ID | int |  | YES | (NULL) |
| BROKEN_REFERENCES | int |  | YES | ((0)) |
| OUTDATED_REFERENCES | int |  | YES | ((0)) |
| MISSING_REFERENCES | int |  | YES | ((0)) |
| OUTDATED_MISSING_REFERENCES | int |  | YES | ((0)) |
| OLDPRODUCER_REFERENCES | int |  | YES | ((0)) |
| UNASSIGNED_PHONES | bit |  | YES | ((0)) |
| REQUIRES_COMPILATION | bit |  | YES | ((0)) |
| DISABLED | bit |  | YES | ((0)) |
| USERPROVIDER_VERSION_ID | int |  | YES | (NULL) |
| OUTDATED_USERPROVIDER | bit |  | YES | ((0)) |
| MISSING_USERPROVIDER | bit |  | YES | ((0)) |
| OLDPRODUCER_USERPROVIDER | bit |  | YES | ((0)) |
| OUTDATED_BROKEN_REFERENCES | int |  | YES | ((0)) |
| SECURITYSETTINGSCHANGED | bit |  | YES | ((0)) |
| PENDINGRUNTIMECONFIGS | bit |  | YES | ((0)) |

## ossys_Meta_Cyclic_Job
**Physical table:** `ossys_Meta_Cyclic_Job`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ESPACE_ID | int |  | NO |  |
| NAME | nvarchar | 50 | NO |  |
| DEFAULT_SCHEDULE | nvarchar | 2000 | YES | ('') |
| PRIORITY | int |  | NO |  |
| IS_ACTIVE | bit |  | NO |  |
| SS_KEY | nvarchar | 100 | YES | ('') |
| TIMEOUT | int |  | YES |  |
| EFFECTIVE_TIMEOUT | int |  | YES |  |
| Is_Shared | bit |  | NO | ((0)) |

## ossys_Tenant
**Physical table:** `ossys_Tenant`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 35 | YES | ('') |
| ESPACE_ID | int |  | NO |  |
| IS_ACTIVE | bit |  | NO |  |

## SEGMENT_AUDIT
**Physical table:** `[ReportingOutsystemsIntegration].[dbo].[SEGMENT_AUDIT]`  

_Column definitions unavailable — table is in a restricted external database (`ReportingOutsystemsIntegration`). Elevated database access required._

## snap_oslog_Cyclic_Job
**Physical table:** `[OSLogDB].[dbo].[oslog_Cyclic_Job]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Cyclic_Job_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_Cyclic_Job_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Error
**Physical table:** `[OSLogDB].[dbo].[oslog_Error]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Error_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_Error_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Extension
**Physical table:** `[OSLogDB].[dbo].[oslog_Extension]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Extension_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_Extension_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_General
**Physical table:** `[OSLogDB].[dbo].[oslog_General]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_General_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_General_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Int_Detail
**Physical table:** `[OSLogDB].[dbo].[oslog_Int_Detail]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Int_Detail_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_Int_Detail_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Integration
**Physical table:** `[OSLogDB].[dbo].[oslog_Integration]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Integration_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_Integration_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_mobile_request
**Physical table:** `[OSLogDB].[dbo].[oslog_mobile_request]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_mobile_request_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_mobile_request_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_MR_Detail
**Physical table:** `[OSLogDB].[dbo].[oslog_MR_Detail]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_MR_Detail_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_MR_Detail_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Parameter
**Physical table:** `[OSLogDB].[dbo].[oslog_Parameter]`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| Id | int |  | NO |  |
| Name | nvarchar | 50 | NO |  |
| Val | nvarchar | 250 | YES |  |

## snap_oslog_RequestEvent
**Physical table:** `[OSLogDB].[dbo].[oslog_RequestEvent]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_RequestEvent_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_RequestEvent_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Screen
**Physical table:** `[OSLogDB].[dbo].[oslog_Screen]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Screen_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_Screen_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_SrvAPI
**Physical table:** `[OSLogDB].[dbo].[oslog_SrvAPI]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_SrvAPI_Detail
**Physical table:** `[OSLogDB].[dbo].[oslog_SrvAPI_Detail]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_SrvAPI_Detail_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_SrvAPI_Detail_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_SrvAPI_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_SrvAPI_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Web_Reference
**Physical table:** `[OSLogDB].[dbo].[oslog_Web_Reference]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Web_Reference_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_Web_Reference_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Web_Service
**Physical table:** `[OSLogDB].[dbo].[oslog_Web_Service]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## snap_oslog_Web_Service_Previous
**Physical table:** `[OSLogDB].[dbo].[oslog_Web_Service_Previous]`  

_Column definitions pending — table is in an external database (`OSLogDB`). Run `scripts/missing_oslogdb.sql` against that database to populate._

## TENANTLIFTCOMPONENTTOTAL
**Physical table:** `[YearReviewDB].[dbo].[OSUSR_R4Q_TENANTLIFTCOMPONENTTOTAL]`  

_Column definitions unavailable — table is in a restricted external database (`YearReviewDB`). Elevated database access required._

## TENANTPRTOTAL
**Physical table:** `[YearReviewDB].[dbo].[OSUSR_R4Q_TENANTPRTOTAL]`  

_Column definitions unavailable — table is in a restricted external database (`YearReviewDB`). Elevated database access required._

## UCT_REPORTING_ETL_UPDATE_TIME
**Physical table:** `[ReportingOutsystemsIntegration].[dbo].[UCT_REPORTING_ETL_UPDATE_TIME]`  

_Column definitions unavailable — table is in a restricted external database (`ReportingOutsystemsIntegration`). Elevated database access required._

## UCT_RETAIN
**Physical table:** `[outsystems].[dbo].[UCT_RETAIN]`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## USERPRTOTAL
**Physical table:** `[YearReviewDB].[dbo].[OSUSR_R4Q_USERPRTOTAL]`  

_Column definitions unavailable — table is in a restricted external database (`YearReviewDB`). Elevated database access required._

## WORKATO_RECIPE_DATA
**Physical table:** `[ReportingOutsystemsIntegration].[dbo].[WORKATO_RECIPE_DATA_DEV]`  

_Column definitions unavailable — table is in a restricted external database (`ReportingOutsystemsIntegration`). Elevated database access required._

## WORKATO_RECIPE_DATA_UPDATE_TIME
**Physical table:** `[ReportingOutsystemsIntegration].[dbo].[WORKATO_RECIPE_DATA_UPDATE_TIME_DEV]`  

_Column definitions unavailable — table is in a restricted external database (`ReportingOutsystemsIntegration`). Elevated database access required._

## YEARREVIEW
**Physical table:** `[YearReviewDB].[dbo].[OSUSR_R4Q_YEARREVIEW]`  

_Column definitions unavailable — table is in a restricted external database (`YearReviewDB`). Elevated database access required._

## YR_PERFORMANCE_TMP
**Physical table:** `[YearReviewDB].[dbo].[YR_PERFORMANCE_TMP]`  

_Column definitions unavailable — table is in a restricted external database (`YearReviewDB`). Elevated database access required._
