# Menu_CS

## Tables

- [AdminPrimaryMenu](#adminprimarymenu)
- [AdminSecondaryMenu](#adminsecondarymenu)
- [Application](#application)
- [DefaultMenuItems](#defaultmenuitems)
- [ManagementPrimaryMenu](#managementprimarymenu)
- [ManagementSecondaryMenu](#managementsecondarymenu)
- [MenuFeature](#menufeature)
- [MenuIconCategory](#menuiconcategory)
- [MenuIcons](#menuicons)
- [MenuItem](#menuitem)
- [MenuItem_Extension](#menuitem-extension)
- [MenuPlacement](#menuplacement)
- [MenuPlacementSegment](#menuplacementsegment)
- [MenuType](#menutype)
- [MobileScreen](#mobilescreen)
- [UserDefaultSecondaryMenu](#userdefaultsecondarymenu)

## AdminPrimaryMenu
**Physical table:** `OSUSR_XUF_ADMINPRIMARYMENU`  
**Description:** The Primany Menu Items for the Admin Menu.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ICONCLASS | nvarchar | 50 | YES | ('') |
| CAPTION | nvarchar | 50 | YES | ('') |
| URL | nvarchar | 100 | YES | ('') |
| ROLES | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| MENUITEM | nvarchar | 50 | YES | ('') |
| ISINBETA | bit |  | YES | ((0)) |
| IONICTAG | nvarchar | 50 | YES | ('') |
| ISNEW | bit |  | YES | ((0)) |
| ISUPDATED | bit |  | YES | ((0)) |

## AdminSecondaryMenu
**Physical table:** `OSUSR_XUF_ADMINSECONDARYMENU`  
**Description:** The Secondary Menu Items for the Admin Menu.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PRIMARYMENUITEMID | int |  | YES | (NULL) |
| CAPTION | nvarchar | 50 | YES | ('') |
| URL | nvarchar | 100 | YES | ('') |
| ROLES | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| MENUITEM | nvarchar | 50 | YES | ('') |
| ISINBETA | bit |  | YES | ((0)) |
| IONICTAG | nvarchar | 50 | YES | ('') |
| ISUSAONLY | bit |  | YES | ((0)) |
| BETATOOLTIPTEXT | nvarchar | 500 | YES | ('') |
| ISNEW | bit |  | YES | ((0)) |
| ISROLESRESTRICTED | bit |  | YES | ((0)) |
| ISONLYFORWODIFYPAYMENTS | bit |  | YES | ((0)) |
| ISUPDATED | bit |  | YES | ((0)) |
| CANBEDEFAULTSCREEN | bit |  | YES | ((0)) |

## Application
**Physical table:** `OSUSR_XUF_APPLICATION`  
**Description:** Static entity for distinguishing between applications  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| APPLICATIONNAME | nvarchar | 50 | YES | ('') |
| URL | nvarchar | 250 | YES | ('') |
| ENTRYESPACE | nvarchar | 50 | YES | ('') |
| ENTRYNAME | nvarchar | 50 | YES | ('') |
| USEENTRY | bit |  | YES | ((0)) |

## DefaultMenuItems
**Physical table:** `OSUSR_X0F_DEFAULTMENUITEMS_SE`  
**Description:** Hold the default menus for mobile navigation settings, to apply when customer access it the first time or on reset to defaults  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| MENUICONSSEID | nvarchar | 50 | YES | (NULL) |
| MOBILESCREENSSEID | nvarchar | 50 | YES | (NULL) |
| MENUICONSID | nvarchar | 50 | YES | (NULL) |
| MOBILESCREENSID | nvarchar | 50 | YES | (NULL) |
| MENUTYPEID | nvarchar | 50 | YES | (NULL) |
| MOBILESCREENID | nvarchar | 50 | YES | (NULL) |
| ISPERFORM | bit |  | YES | ((0)) |

## ManagementPrimaryMenu
**Physical table:** `OSUSR_XUF_MANAGEMENTPRIMARYMENU`  
**Description:** The Primany Menu Items for the Management Menu.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ICONCLASS | nvarchar | 50 | YES | ('') |
| CAPTION | nvarchar | 50 | YES | ('') |
| URL | nvarchar | 100 | YES | ('') |
| ROLES | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| MENUITEM | nvarchar | 50 | YES | ('') |
| ISINBETA | bit |  | YES | ((0)) |
| IONICTAG | nvarchar | 50 | YES | ('') |
| ADMINSECONDARYMENUID | int |  | YES | (NULL) |

## ManagementSecondaryMenu
**Physical table:** `OSUSR_XUF_MANAGEMENTSECONDARYMENU`  
**Description:** The Primany Menu Items for the Management Menu.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| PRIMARYMENUITEMID | int |  | YES | (NULL) |
| CAPTION | nvarchar | 50 | YES | ('') |
| URL | nvarchar | 100 | YES | ('') |
| ROLES | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| MENUITEM | nvarchar | 50 | YES | ('') |
| ISINBETA | bit |  | YES | ((0)) |
| IONICTAG | nvarchar | 50 | YES | ('') |

## MenuFeature
**Physical table:** `OSUSR_X0F_FEATUREMENU`  
**Description:** Category the menu item falls under for feature.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## MenuIconCategory
**Physical table:** `OSUSR_X0F_MENUICONCATEGORY_SE`  
**Description:** Represents the category grouping for available menu icons used in the Wodify mobile application's customizable navigation. Categories help organize icons by function or context (e.g., Main Actions, People, Documents). Each icon in MenuIcons_SE references a category from this entity.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## MenuIcons
**Physical table:** `OSUSR_X0F_MENUICONS_SE`  
**Description:** Defines the curated set of icons available for use in the Wodify mobile app's custom menu system. Each icon entry includes its structured name (e.g., 24_activityFeed), an associated category (MenuIconCategory_SE), and a display order. These icons are rendered using css classes that follow Wodify’s design system conventions.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ICONNAME | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| MENUICONCATEGORYSEID | int |  | YES | (NULL) |
| IS_RESERVED | bit |  | YES | ((0)) |
| MENUICONCATEGORYID | int |  | YES | (NULL) |

## MenuItem
**Physical table:** `OSUSR_X0F_CUSTOMCUSTOMERMENU`  
**Description:** Defines a configurable navigation menu item available in the Wodify mobile application. Each entry represents a reusable menu link that can be placed in one or more menu layouts (e.g., bottom tabs, side menus) via the {CustomCustomerMenuPlacement} table. Menu items can route users to internal mobile screens or external URLs via linked extension data.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| MENUTYPESEID | nvarchar | 50 | YES | (NULL) |
| MENUICONSSEID | nvarchar | 50 | YES | (NULL) |
| MOBILESCREENSSEID | nvarchar | 50 | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| MENUTYPEID | nvarchar | 50 | YES | (NULL) |
| MENUICONSID | nvarchar | 50 | YES | (NULL) |
| MOBILESCREENSID | nvarchar | 50 | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| FEATUREMENUID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDBY | int |  | YES | (NULL) |
| MOBILESCREENID | nvarchar | 50 | YES | (NULL) |

## MenuItem_Extension
**Physical table:** `OSUSR_X0F_MENUITEM_EXTENSION`  
**Description:** Provides external link and asset metadata for menu items defined in {CustomCustomerMenu}. Used when a menu item is not tied to a predefined mobile screen (i.e., {MobileScreenId} is null), this table supports URL overrides, dynamic parameters, and rich content integrations (e.g., CKBox assets, Smart Button Pages). This allows a single menu item to point to external web resources, BEE/CKEditor documents, or content widgets rendered in-app.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| MENUITEMID | int |  | NO |  |
| URLOVERRIDE | nvarchar | -1 | YES | ('') |
| URLMEDIAEXTENSION | nvarchar | 50 | YES | ('') |
| URLASSETID | nvarchar | 50 | YES | ('') |
| SMARTBUTTONPAGEID | bigint |  | YES | ((0)) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## MenuPlacement
**Physical table:** `OSUSR_X0F_MENUPLACEMENT1`  
**Description:** Links a CustomCustomerMenu to one or more MenuTypes with a defined display order. Supports reuse of a menu item across multiple menu placements.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| MENUTYPEID | nvarchar | 50 | YES | (NULL) |
| MENUITEMID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MenuPlacementSegment
**Physical table:** `OSUSR_X0F_MENUPLACEMENTSEGMENT1`  
**Description:** Defines visibility rules and order for a given menu item within a specific menu type and for a specific segment of users. Enables targeted menu customization.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| MENUPLACEMENTID | bigint |  | YES | (NULL) |
| SEGMENTID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## MenuType
**Physical table:** `OSUSR_X0F_MENUTYPE_SE`  
**Description:** Specifies the different menu placement types available for configuration in the Wodify mobile app. This includes options such as Bottom Tabs (main navigation), Side Menu for Coaches, and Side Menu for all users. Each custom menu item in CustomMenuTable references a menu type from this entity to determine its placement.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## MobileScreen
**Physical table:** `OSUSR_X0F_MOBILESCREENS1`  
**Description:** Defines a 1:1 mapping between customizable menu options and their corresponding screen destinations across both the Wodify mobile and admin web platforms. Each record represents a uniquely identifiable screen and supports dynamic routing based on selected menu items.  Validate all screens using "urlmappings" via https://dev.wodify.com/WodifyClient/moduleservices/moduleinfo  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| KEY | nvarchar | 50 | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| STATICTERMV2ID | nvarchar | 50 | YES | (NULL) |
| FEATUREID | int |  | YES | (NULL) |
| STATICTERMID | int |  | YES | (NULL) |
| URLPARAMETERS | nvarchar | 50 | YES | ('') |
| MENUICONID | nvarchar | 50 | YES | (NULL) |
| ISPERFORM | bit |  | YES | ((0)) |
| URLOVERRIDE | nvarchar | 50 | YES | ('') |
| ISTERMPLURAL | bit |  | YES | ((0)) |

## UserDefaultSecondaryMenu
**Physical table:** `OSUSR_X0F_USERDEFAULTSECONDARYMENU`  
**Description:** Contains the default secondary menu (default landing page) for the specified User  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| DEFAULTSECONDARYMENUID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
