# Customer_CS

## Tables

- [ApiKeyType](#apikeytype)
- [AsyncProcess](#asyncprocess)
- [BusinessType](#businesstype)
- [Customer](#customer)
- [CustomerApiKey](#customerapikey)
- [CustomerAvatarRingSetting](#customeravatarringsetting)
- [CustomerDeletedTwilioPhoneNumber](#customerdeletedtwiliophonenumber)
- [CustomerImage](#customerimage)
- [CustomerMFARequiredRole](#customermfarequiredrole)
- [CustomerSettingContactInformation](#customersettingcontactinformation)
- [CustomerSettingEmail](#customersettingemail)
- [CustomerSettingGeneral](#customersettinggeneral)
- [CustomerSettingRetain](#customersettingretain)
- [CustomerStripeReaderOrder](#customerstripereaderorder)
- [CustomerTwilioAuthentication](#customertwilioauthentication)
- [CustomerTwilioPhoneNumber](#customertwiliophonenumber)
- [CustomerTwilioPhoneNumberUser](#customertwiliophonenumberuser)
- [DefaultTheme](#defaulttheme)
- [GymProgram](#gymprogram)
- [GymProgramLocationIntegrationAvailability](#gymprogramlocationintegrationavailability)
- [ImageType](#imagetype)
- [LeadWebFormSpamProtection](#leadwebformspamprotection)
- [Location](#location)
- [LocationCoordinates](#locationcoordinates)
- [LocationHistory](#locationhistory)
- [LocationPeopleSettings](#locationpeoplesettings)
- [LocationPeopleSettingsHistory](#locationpeoplesettingshistory)
- [LocationProgram](#locationprogram)
- [LocationSettingPartner](#locationsettingpartner)
- [PayRate](#payrate)
- [PayRateRule](#payraterule)
- [PayRateRuleType](#payrateruletype)
- [PayRateSubRule](#payratesubrule)
- [PayRateSubRuleType](#payratesubruletype)
- [PayRateType](#payratetype)
- [ProcessingFeeTaxType](#processingfeetaxtype)
- [ReinstateCustomer](#reinstatecustomer)
- [Request](#request)
- [RequestType](#requesttype)
- [RetainEmailTemplate](#retainemailtemplate)
- [SeamCustomerDevice](#seamcustomerdevice)
- [SeamCustomerDeviceCount](#seamcustomerdevicecount)
- [SeamCustomerLocationMapping](#seamcustomerlocationmapping)
- [SecureProgrammingOption](#secureprogrammingoption)
- [SimpleSignInSort](#simplesigninsort)
- [ThemeLocation](#themelocation)
- [ThemeLocationCSS](#themelocationcss)
- [WodifindLocationOffering](#wodifindlocationoffering)
- [WodifindOfferingType](#wodifindofferingtype)
- [WodifySitesAccess](#wodifysitesaccess)
- [WorkatoCustomerAccount](#workatocustomeraccount)
- [WorkatoCustomerAccountUser](#workatocustomeraccountuser)

## ApiKeyType
**Physical table:** `OSUSR_5ui_ApiKeyType`  
**Description:** Contains all type of API keys that a customer can use to integrate between Wodify and third-party tools  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## AsyncProcess
**Physical table:** `OSUSR_5ui_AsyncProcess1`  
**Description:** Auxiliar entity that contains all asynchronous processes, which will run through the AP module in BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## BusinessType
**Physical table:** `OSUSR_5ui_BusinessType`  
**Description:** Contains all business types.  If a Customer has multiple locations, it is possible to have a different business type for each location, otherwise the customer will have one business type  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| EXTERNALVALUE | nvarchar | 50 | YES | ('') |

## Customer
**Physical table:** `OSUSR_5ui_Customer`  
**Description:** Contains the main data of the customer, namely it's private name and if is active or not  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| BUSINESSTYPEID | int |  | YES | (NULL) |
| APPLYBTYPEALLLOCATIONS | bit |  | YES | ((0)) |

## CustomerApiKey
**Physical table:** `OSUSR_5ui_TenantApiKey`  
**Description:** API keys that can be used to authorize a request to Wodify's external APIs.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| APIKEY | nvarchar | 150 | YES | ('') |
| CUSTOMERID | bigint |  | YES | (NULL) |
| APIKEYTYPEID | int |  | YES | (NULL) |

## CustomerAvatarRingSetting
**Physical table:** `OSUSR_5ui_CustomerAvatarRingSetting`  
**Description:** Defines Customer overwrites for Avatar Rings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| AVATARRINGID | int |  | YES | (NULL) |
| LABEL | nvarchar | 50 | YES | ('') |
| ISENABLED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| COLORHEXCODE | nvarchar | 10 | YES | ('') |

## CustomerDeletedTwilioPhoneNumber
**Physical table:** `OSUSR_5ui_CustomerDeletedTwilioPhoneNumber`  
**Description:** When a customer deletes one of their Twilio provisioned numbers for SMS, the last usage details for that number on deletion (used for billing)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PHONENUMBER | nvarchar | 20 | YES | ('') |
| COUNTLASTMONTHSMSMESSAGES | int |  | YES | ((0)) |
| COUNTLASTMONTHMMSMESSAGES | int |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PHONENUMBERSID | nvarchar | 50 | YES | ('') |
| LOCATIONID | int |  | YES | (NULL) |

## CustomerImage
**Physical table:** `OSUSR_3bu_TenantImage`  
**Description:** DO NOT DELETE THIS without checking with Clay first. This entity contains old customer pictures that Clay mentioned he would like to migrate somewhere. Make sure that work is done or don't need to be done before deleting this entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| IMAGE | varbinary | -1 | YES | (NULL) |
| FILENAME | nvarchar | 250 | YES | ('') |
| FILETYPE | nvarchar | 1000 | YES | ('') |
| LOCATIONID | int |  | YES | (NULL) |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 200 | YES | ('') |
| IMAGETYPEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | YES | (NULL) |

## CustomerMFARequiredRole
**Physical table:** `OSUSR_5ui_CustomerMFARequiredRole3`  
**Description:** Contains customer settings for which roles need to perform MFA when signing in  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| ROLEID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISLOCKEDFORCUSTOMER | bit |  | YES | ((0)) |

## CustomerSettingContactInformation
**Physical table:** `OSUSR_72o_TenantSettingContactInformation`  
**Description:** contains customer settings related to contacts  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| PUBLICNAME | nvarchar | 50 | YES | ('') |
| STREETADDRESS1 | nvarchar | 50 | YES | ('') |
| STREETADDRESS2 | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| PROVINCE | nvarchar | 50 | YES | ('') |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| WEBSITE | nvarchar | 100 | YES | ('') |
| PHONENUMBER | nvarchar | 20 | YES | ('') |
| FEEDBACKENABLED | bit |  | YES | ((0)) |
| FEEDBACKEMAILADDRESS | nvarchar | 250 | YES | ('') |
| LEADEMAILADDRESS | nvarchar | 2000 | YES | ('') |
| LEADFORMREDIRECTURL | nvarchar | 350 | YES | ('') |
| LEADWEBFORMKEY | nvarchar | 10 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| WODIFYSUBDOMAIN | nvarchar | 50 | YES | ('') |
| LEADWEBFORMSPAMPROTECTIONID | int |  | YES | (NULL) |
| RECAPTCHASITEKEY | nvarchar | 500 | YES | ('') |
| RECAPTCHASECRET | nvarchar | 500 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| CUSTOMERID | bigint |  | NO |  |
| DEFAULTSERVICEEMAIL | nvarchar | 250 | YES | ('') |

## CustomerSettingEmail
**Physical table:** `OSUSR_5ui_TenantSettingEmail`  
**Description:** Entity that has extended properties for a Customer, this specific one related to email settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| EMAILSIGNATURE | nvarchar | -1 | YES | ('') |
| ENABLEEMAILSIGNATURE | bit |  | YES | ((0)) |
| EMAILFROMLABEL | nvarchar | 100 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERID | bigint |  | NO | (NULL) |
| HASINAPPCHATENABLED | bit |  | YES | ((0)) |
| HASCALENDAREVENTSENABLED | bit |  | YES | ((0)) |
| EMAILSERVICECONFIGURATIONSET | int |  | YES | (NULL) |

## CustomerSettingGeneral
**Physical table:** `OSUSR_72o_TenantSettingGeneral`  
**Description:** Entity that extends properties of customer's general settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| UOMWEIGHTID | int |  | YES | (NULL) |
| UOMDISTANCEID | int |  | YES | (NULL) |
| USESMAILCHIMP | bit |  | YES | ((0)) |
| MAILCHIMPAPIKEY | nvarchar | 50 | YES | ('') |
| MAILCHIMPLIST | nvarchar | 50 | YES | ('') |
| WODPUBLISHTIMEOFFSET | int |  | YES | ((0)) |
| TWITTERHASHTAG | nvarchar | 139 | YES | ('') |
| DATEFORMATID | int |  | YES | (NULL) |
| USE24HOURTIME | bit |  | YES | ((0)) |
| MRR | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HISTORY | nvarchar | -1 | YES | ('') |
| CURRENCY | nvarchar | 5 | YES | ('') |
| CURRENCYSIGNIFICANTDIGITS | int |  | YES | ((0)) |
| DECIMALSEPARATOR | nvarchar | 5 | YES | ('') |
| GROUPSEPARATOR | nvarchar | 5 | YES | ('') |
| AGEOFMAJORITY | int |  | YES | ((0)) |
| HASBEENASKEDAOM | bit |  | YES | ((0)) |
| LANGUAGEID | int |  | YES | (NULL) |
| ISSUSPENDED | bit |  | YES | ((0)) |
| SUSPENSIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| USEMINIMUMCARTVALUE | bit |  | YES | ((0)) |
| MINIMUMCARTVALUE | decimal |  | YES | ((0)) |
| ENABLEMEMBERCASHSELFSERVICE | bit |  | YES | ((0)) |
| ENABLEMEMBERCHECKSELFSERVICE | bit |  | YES | ((0)) |
| ENABLEGUESTCASHSELFSERVICE | bit |  | YES | ((0)) |
| ENABLEGUESTCHECKSELFSERVICE | bit |  | YES | ((0)) |
| PUBLISHINWODIFYDAYSBEFORE | int |  | YES | ((0)) |
| PUBLISHINWODIFYTIMEOFDAY | datetime |  | YES | ('1900-01-01 00:00:00') |
| MAILCHIMPLISTID | nvarchar | 50 | YES | ('') |
| DEACTIVATIONDATETIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| WORDPRESS_COMID | bigint |  | YES | (NULL) |
| WORDPRESS_ORGID | bigint |  | YES | (NULL) |
| NONGENDERISENABLED | bit |  | YES | ((0)) |
| NONGENDERDEFAULTFILTER | int |  | YES | ((0)) |
| CUSTOMERID | bigint |  | NO | (NULL) |
| ONETIMEEXERCISESDEFAULTNAME | nvarchar | 300 | YES | ('') |
| UOMTEMPERATUREID | int |  | YES | (NULL) |
| APPAPPEARANCE | int |  | YES | ((0)) |
| RESERVATIONSORT | int |  | YES | (NULL) |
| SIGNEDINSORT | int |  | YES | (NULL) |
| PINPOSITION | nvarchar | 50 | YES | ('') |
| ENABLECUSTOMDICTIONARY | bit |  | YES | ((0)) |
| DISPLAYWEEKLYSTREAKS | bit |  | YES | ((1)) |
| ENABLERETAILLAST4PHONEVERIFY | bit |  | YES | ((0)) |
| ENABLERETAILPINVERIFY | bit |  | YES | ((0)) |
| ADDTOUPCOMINGINVOICEPAYMENT | bit |  | YES | ((1)) |
| ADDTOUPCOMINGINVOICESSPOS | bit |  | YES | ((0)) |
| UPCOMINGINVOICEMOBILERETPOS | bit |  | YES | ((0)) |
| UPCOMINGINVOICEUNITOFTIME | int |  | YES | (NULL) |
| UPCOMINGINVOICELIMIT | int |  | YES | ((0)) |
| DISPLAYLOCATIONSTIMES | bit |  | YES | ((1)) |
| EnableHomepageBirthdays | bit |  | YES |  |
| EnableHomepageBuyTab | bit |  | YES |  |
| ISCLASSPASSENABLED | bit |  | YES | ((0)) |
| FEATUREDPRODUCTS | bit |  | YES | ((0)) |
| POSFEATUREDPRODUCTS | bit |  | YES | ((0)) |
| MOBILEPOSFEATUREDPRODUCTS | bit |  | YES | ((0)) |
| ISWELLHUBENABLED | bit |  | YES | ((0)) |
| POPULARPRODUCTLIMIT | int |  | YES | ((0)) |
| MINIMUMCARTVALUEFILTER | int |  | YES | ((0)) |

## CustomerSettingRetain
**Physical table:** `OSUSR_5ui_CustomerSettingRetain`  
**Description:** Entity that has extended properties for a Customer, this specific one related to retain settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CUSTOMERID | bigint |  | NO |  |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| SNOOZEDATERANGEVALUE | int |  | YES | ((0)) |
| SNOOZEDATERANGETYPE | nvarchar | 50 | YES | ('') |
| SNOOZEDISABLESNOOZEFOREVER | bit |  | YES | ((0)) |
| RISKLEVEL | nvarchar | 50 | YES | ('') |

## CustomerStripeReaderOrder
**Physical table:** `OSUSR_5ui_CustomerStripeReaderOrder`  
**Description:** Holds the most recent successful Stripe cc reader terminal order date  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CUSTOMERID | bigint |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| LASTORDERDATE | datetime |  | YES | ('1900-01-01 00:00:00') |

## CustomerTwilioAuthentication
**Physical table:** `OSUSR_5ui_CustomerTwilioAuthentication`  
**Description:** Contains data related to twilio's authentication  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CUSTOMERID | bigint |  | NO |  |
| ACCOUNTSID | nvarchar | 50 | YES | ('') |
| AUTHTOKEN | nvarchar | 50 | YES | ('') |
| APIKEY | nvarchar | 50 | YES | ('') |
| APISECRET | nvarchar | 50 | YES | ('') |
| CONVERSATIONSSERVICESID | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| PARTICIPANTCONVERSATIONLIMIT | int |  | YES | ((0)) |

## CustomerTwilioPhoneNumber
**Physical table:** `OSUSR_5ui_CustomerProvisionedPhoneNumber`  
**Description:** Contains a customers Twilio provisioned numbers for SMS and the identity values that Phone number is connected to  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PHONENUMBER | nvarchar | 20 | YES | ('') |
| LOCATIONID | int |  | YES | (NULL) |
| FRIENDLYNAME | nvarchar | 50 | YES | ('') |
| TWILIOUSERIDENTITY | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| TWILIOPHONENUMBERSID | nvarchar | 50 | YES | ('') |
| VERIFICATIONSTATUSID | int |  | YES | (NULL) |

## CustomerTwilioPhoneNumberUser
**Physical table:** `OSUSR_5ui_CustomerTwilioPhoneNumberEmployee`  
**Description:** A users associated with a CustomerTwilioPhoneNumber  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERTWILIOPHONENUMBER | bigint |  | YES | (NULL) |
| USERID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CUSTOMERTWILIOPHONENUMBERID | bigint |  | YES | (NULL) |

## DefaultTheme
**Physical table:** `OSUSR_3bu_DefaultTheme`  
**Description:** Entity with base/default themes for the Location Theme  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| BACKGROUNDCOLOR | nvarchar | 50 | YES | ('') |
| TEXTCOLOR | nvarchar | 50 | YES | ('') |
| HIGHLIGHTTEXTCOLOR | nvarchar | 50 | YES | ('') |
| MENUCOLOR | nvarchar | 50 | YES | ('') |
| INPUTCOLOR | nvarchar | 50 | YES | ('') |
| ACCENTCOLOR | nvarchar | 50 | YES | ('') |

## GymProgram
**Physical table:** `OSUSR_5ui_GymProgram`  
**Description:** Contains all Programs for all Gyms (Customers)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 200 | YES | ('') |
| COLOR | nvarchar | 7 | YES | ('') |
| PUBLISHEXTERNALLY | bit |  | YES | ((0)) |
| COUNTTOWARDSATTENDANCELIMITS | bit |  | YES | ((0)) |
| SECUREPROGRAMMINGENABLED | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SECUREPROGRAMMINGOPTIONID | int |  | YES | (NULL) |
| ORDER | int |  | YES | ((0)) |
| DISPLAYORDER | int |  | YES | ((0)) |
| HIDEATTENDANCECOUNTS | bit |  | YES | ((0)) |
| SHOWATTENDANCECOUNTS | bit |  | YES | ((0)) |
| ISCLASSPASSENABLED | bit |  | YES |  |

## GymProgramLocationIntegrationAvailability
**Physical table:** `OSUSR_5ui_GymProgramLocationIntegrationAvailability`  
**Description:** Holds records of Program/Location combinations and if they are enabled in Wellhub or Classpass ProgramLocations that are disabled do not exist in this table  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| PROGRAMID | int |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| ISCLASSPASSENABLED | bit |  | YES | ((0)) |
| ISWELLHUBENABLED | bit |  | YES | ((0)) |
| WELLHUBPRODUCTID | bigint |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ImageType
**Physical table:** `OSUSR_3bu_ImageType`  
**Description:** DO NOT DELETE THIS without checking with Clay first. This entity identifies the image type from CustomerImage entity, which contains old customer pictures that Clay mentioned he would like to migrate somewhere. Make sure that work is done or don't need to be done before deleting this entity  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| MAXX | int |  | YES | ((0)) |
| MAXY | int |  | YES | ((0)) |
| DESCRIPTION | nvarchar | 50 | YES | ('') |

## LeadWebFormSpamProtection
**Physical table:** `OSUSR_72o_LeadWebFormSpamProtection`  
**Description:** Contains all types of spam protection for the lead web form  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## Location
**Physical table:** `OSUSR_72o_Location`  
**Description:** Entity which holds information about a Location  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| STREETADDRESS1 | nvarchar | 50 | YES | ('') |
| STREETADDRESS2 | nvarchar | 50 | YES | ('') |
| CITY | nvarchar | 50 | YES | ('') |
| STATEID | int |  | YES | (NULL) |
| ZIPCODE | nvarchar | 50 | YES | ('') |
| COUNTRYID | int |  | YES | (NULL) |
| PROVINCE | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISACTIVE | bit |  | YES | ((0)) |
| SHOWINWODIFIND | bit |  | YES | ((0)) |
| WODIFINDNAME | nvarchar | 50 | YES | ('') |
| WODIFINDDESCRIPTION | nvarchar | 250 | YES | ('') |
| PAYMENTPROCESSORCONFIGURATIO | int |  | YES | (NULL) |
| BILLINGCONTACT | int |  | YES | (NULL) |
| BILLINGCONTACTCC | int |  | YES | (NULL) |
| WEBSITE | nvarchar | 100 | YES | ('') |
| PHONENUMBER | nvarchar | 20 | YES | ('') |
| EMAIL | nvarchar | 250 | YES | ('') |
| TWITTERHASHTAG | nvarchar | 139 | YES | ('') |
| EMAILSIGNATURE | nvarchar | -1 | YES | ('') |
| ENABLEEMAILSIGNATURE | bit |  | YES | ((0)) |
| EMAILFROMLABEL | nvarchar | 100 | YES | ('') |
| EMAILSUBDOMAINID | int |  | YES | (NULL) |
| PAYMENTMETHODID | int |  | YES | (NULL) |
| BILLINGCONTACTPHONE | nvarchar | 20 | YES | ('') |
| STAFFSIGNATURE | nvarchar | 500 | YES | ('') |
| STAFFSIGNATURECLOUDINARYFILE | int |  | YES | (NULL) |
| ABNNUMBER | nvarchar | 50 | YES | ('') |
| GSTNUMBER | nvarchar | 50 | YES | ('') |
| SALESFORCEID | nvarchar | 50 | YES | ('') |
| STAFFSIGNATUREEXTERNALIMAGEI | bigint |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| AFFILIATEID | bigint |  | YES | ((0)) |
| BUSINESSTYPEID | int |  | YES | (NULL) |
| STRIPETERMINALLOCATIONID | nvarchar | 50 | YES | ('') |
| PASSPROCESSINGFEEENABLED | bit |  | YES | ((0)) |
| PROCESSINGFEECUTOFFAMOUNT | decimal |  | YES | ((0)) |
| TIMEZONEID | int |  | YES | (NULL) |
| LEADOWNERID | int |  | YES | (NULL) |
| CLIENTOWNERID | int |  | YES | (NULL) |
| PROCESSINGFEETAXTYPEID | int |  | YES | (NULL) |
| PROCESSINGFEETAXRATE | decimal |  | YES | ((0)) |
| PROCESSINGFEEMAXIMUMAMOUNT | decimal |  | YES | ((0)) |
| IANATIMEZONEIDENTIFIER | bigint |  | YES | (NULL) |

## LocationCoordinates
**Physical table:** `OSUSR_72o_LocationCoordinates`  
**Description:** Contains latitute and longitude for the specified location  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | int |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| LATITUDE | decimal |  | YES | ((0)) |
| LONGITUDE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| HASGEOLOCATIONFAILED | bit |  | YES | ((0)) |
| CUSTOMERID | bigint |  | YES | (NULL) |

## LocationHistory
**Physical table:** `OSUSR_5ui_LocationHistory`  
**Description:** Entity that will have the Location history  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LOCATIONID | int |  | NO |  |
| HISTORY | nvarchar | -1 | YES | ('') |

## LocationPeopleSettings
**Physical table:** `OSUSR_3bu_LocationPeopleSettings`  
**Description:** Entity that has the location people settings  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LOCATIONID | int |  | NO |  |
| REFERLOCATIONID | int |  | YES | (NULL) |
| LEADEMAILADDRESS | nvarchar | 2000 | YES | ('') |
| LEADFORMREDIRECTURL | nvarchar | 350 | YES | ('') |
| LEADWEBFORMSPAMPROTECTIONID | int |  | YES | (NULL) |
| RECAPTCHASITEKEY | nvarchar | 500 | YES | ('') |
| RECAPTCHASECRET | nvarchar | 500 | YES | ('') |
| LEADWEBFORMKEY | nvarchar | 10 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## LocationPeopleSettingsHistory
**Physical table:** `OSUSR_3bu_LocationPeopleSettingsHistory`  
**Description:** Entity that will have the people settings history  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| LOCATIONPEOPLESETTINGSID | int |  | NO |  |
| HISTORY | nvarchar | -1 | YES | ('') |

## LocationProgram
**Physical table:** `OSUSR_5ui_LocationProgramSimpleSignIn`  
**Description:** Associates a Location with a Program for Simple Sign-In filtering  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| GYMPROGRAMID | int |  | YES | (NULL) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## LocationSettingPartner
**Physical table:** `OSUSR_5ui_LocationSettingPartner`  
**Description:** Contains integration partner IDs for Customers and Locations  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| TENANT_ID | int |  | YES | (NULL) |
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| LOCATIONID | int |  | YES | (NULL) |
| INTEGRATIONPARTNERID | int |  | YES | (NULL) |
| INTEGRATIONID | nvarchar | 100 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| EXTERNALID | nvarchar | 100 | YES | ('') |

## PayRate
**Physical table:** `OSUSR_5ui_PayRate`  
**Description:** Set on Payroll > Pay Rates. Holds the PayRates per Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PAYRATETYPEID | int |  | YES | (NULL) |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 500 | YES | ('') |
| ISMINPAYENABLED | bit |  | YES | ((0)) |
| ISMAXPAYENABLED | bit |  | YES | ((0)) |
| MINPAY | decimal |  | YES | ((0)) |
| MAXPAY | decimal |  | YES | ((0)) |
| ISTOCOUNTNOSHOWS | bit |  | YES | ((0)) |
| ISTOCOUNTLATECANCELLATIONS | bit |  | YES | ((0)) |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PayRateRule
**Physical table:** `OSUSR_5ui_PayRateRule`  
**Description:** Set when adding/editing a PayRate. Holds the PayRateRules per PayRate/Customer.  Examples:  PerClassOrSession {Coach}/Provider receives $[Rate] per class/session.  PerHour Employee receives $[Rate] per hour.  PerAttendee (with PerAttendeeStandard SubRuleType) {Coach}/Provider receives $[Rate] per attendee.  PercentageOfSessionRevenue (for Appointments only) Employee receives %[Rate] of session revenue.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PAYRATEID | bigint |  | YES | (NULL) |
| PAYRATERULETYPEID | int |  | YES | (NULL) |
| RATE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PayRateRuleType
**Physical table:** `OSUSR_5ui_PayRateRuleType`  
**Description:** Holds the types of PayRateRules  Examples:  PerClassOrSession {Coach}/Provider receives $ per class/session.  PerHour Employee receives $ per hour.  PerAttendee (with PerAttendeeStandard SubRuleType) {Coach}/Provider receives $ per attendee.  PercentageOfSessionRevenue (for Appointments only) Employee receives % of session revenue.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PayRateSubRule
**Physical table:** `OSUSR_5ui_PayRateSubRule`  
**Description:** Set when adding/editing a PayRate. Holds the PayRateSubRules per PayRateRule/PayRate/Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| PAYRATERULEID | bigint |  | YES | (NULL) |
| PAYRATESUBRULETYPEID | int |  | YES | (NULL) |
| RANGESTART | int |  | YES | ((0)) |
| RANGEEND | int |  | YES | ((0)) |
| RATE | decimal |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## PayRateSubRuleType
**Physical table:** `OSUSR_5ui_PayRateSubRuleType`  
**Description:** Holds the types of PayRateSubRules  Examples:  PerAttendeeStandard {Coach}/Provider receives $ per attendee.  PerAttendeeFlat When # of attendees is between X and Y, {coach} receives $ for the class/session.  PerAttendeeTiered When # of attendees is between X and Y, {coach} receives $ per attendee.  PerAttendeeIncremental With a total of X to Y attendees, {coach} receives $ per attendee.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## PayRateType
**Physical table:** `OSUSR_5ui_PayRateType`  
**Description:** Holds the types of PayRates  Class: Pay rates that can be assigned to classes.  Class pay rate rules include pay per class, pay per hour, and pay per attendee.  Appointment: Pay rates that can be assigned to appointments.  Appointment pay rate rules include pay per appointment, pay per hour, and pay per attendee.  Administrative: Pay rates for time-based work not associated with coaching classes or providing services; e.g. front desk, admin, cleaning. Administrative pay rates have one available rule: pay per hour.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ProcessingFeeTaxType
**Physical table:** `OSUSR_5ui_ProcessingFeeTaxType`  
**Description:** Contains all type of taxable configurations that can be selected for a given location's POPF tax strategy.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ReinstateCustomer
**Physical table:** `OSUSR_5ui_ReinstateCustomer`  
**Description:** Auxiliar entity that contains all waivers asynchronous processes, which will run through the Waivers_AP BPT process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| SUSPENSIONDATE | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## Request
**Physical table:** `OSUSR_5ui_Request`  
**Description:** Request data to be used in an Asynchronous Process  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| REQUESTTYPEID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | ((0)) |
| ATTRIBUTES | nvarchar | -1 | YES | ('') |
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

## RequestType
**Physical table:** `OSUSR_5ui_RequestType`  
**Description:** The type of request  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## RetainEmailTemplate
**Physical table:** `OSUSR_5ui_RetainEmailTemplate`  
**Description:** Entity which holds the template for Retain emails  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| TEMPLATENAME | nvarchar | 255 | YES | ('') |
| SUBJECT | nvarchar | 1000 | YES | ('') |
| BODY | nvarchar | -1 | YES | ('') |
| BCC | nvarchar | 1000 | YES | ('') |
| CC | nvarchar | 1000 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| ISDEFAULT | bit |  | YES | ((0)) |

## SeamCustomerDevice
**Physical table:** `OSUSR_5ui_SeamCustomerDevice`  
**Description:** Seam device under this Customer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| DEVICEID | nvarchar | 100 | YES | ('') |
| NAME | nvarchar | 100 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## SeamCustomerDeviceCount
**Physical table:** `OSUSR_5ui_SeamCustomerDeviceCount`  
**Description:** The Device Count across all Seam accounts for this customer ID  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| CUSTOMERID | bigint |  | YES | (NULL) |
| CURRENTMANAGEDDEVICECOUNT | int |  | YES | ((0)) |
| MAXDEVICECOUNTBILLINGPERIOD | int |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| DEVICECOUNTPRIORBILLPERIOD | int |  | YES | ((0)) |

## SeamCustomerLocationMapping
**Physical table:** `OSUSR_5ui_SeamCustomerLocationMapping`  
**Description:** Mappping of Wodify and Seam Data  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| CUSTOMERID | bigint |  | YES | ((0)) |
| LOCATIONID | bigint |  | YES | ((0)) |
| SEAMCUSTOMERID | nvarchar | 100 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CURRENTMANAGEDDEVICECOUNT | int |  | YES | ((0)) |
| MAXDEVICECOUNTBILLINGPERIOD | int |  | YES | ((0)) |

## SecureProgrammingOption
**Physical table:** `OSUSR_5ui_SecureProgrammingOption`  
**Description:** When Secure Wod Programming is enabled, this entity contains all possible options.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 60 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## SimpleSignInSort
**Physical table:** `OSUSR_5ui_SimpleSignInSort`  
**Description:** Different Sort types for Simple Sign In  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ThemeLocation
**Physical table:** `OSUSR_3bu_ThemeLocation`  
**Description:** Represents a theme color for the wodify client view  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| DEFAULTTHEMEID | int |  | YES | (NULL) |
| BACKGROUNDCOLOR | nvarchar | 16 | YES | ('') |
| TEXTCOLOR | nvarchar | 16 | YES | ('') |
| HIGHLIGHTCOLOR | nvarchar | 16 | YES | ('') |
| MENUCOLOR | nvarchar | 16 | YES | ('') |
| ACCENTCOLOR | nvarchar | 16 | YES | ('') |
| INPUTCOLOR | nvarchar | 50 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## ThemeLocationCSS
**Physical table:** `OSUSR_3bu_ThemeLocationCSS`  
**Description:** Entity to hold the Theme Location CSS  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| THEMELOCATIONID | bigint |  | NO |  |
| CSS | nvarchar | -1 | YES | ('') |

## WodifindLocationOffering
**Physical table:** `OSUSR_5ui_WodifindLocationOffering`  
**Description:** List of offerings for a given Wodifind-enabled location (e.g., programs/services offered)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LOCATIONID | int |  | YES | (NULL) |
| CUSTOMERID | bigint |  | YES | (NULL) |
| WODIFINDOFFERINGTYPEID | int |  | YES | (NULL) |
| NAME | nvarchar | 100 | YES | ('') |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## WodifindOfferingType
**Physical table:** `OSUSR_5ui_WodifindOfferingType`  
**Description:** Offering type for Wodifind-enabled location (e.g., program)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |

## WodifySitesAccess
**Physical table:** `OSUSR_5ui_WodifySites`  
**Description:** Stores records for customers with Wodify Sites active  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CUSTOMERID | bigint |  | NO |  |
| ISACTIVE | bit |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## WorkatoCustomerAccount
**Physical table:** `OSUSR_5ui_WorkatoCustomerAccount`  
**Description:** Contains mapping of Wodify Customer Id, Location Id to Workato Workspace Id  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WODIFYCUSTOMERID | bigint |  | YES | (NULL) |
| WODIFYLOCATIONID | int |  | YES | (NULL) |
| WORKATOWORKSPACEID | bigint |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |

## WorkatoCustomerAccountUser
**Physical table:** `OSUSR_5ui_WorkatoCustomerAccountUser`  
**Description:** Contains a mapping of Wodify Users to Workato Users and Workspace  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| WORKATOCUSTOMERACCOUNTID | bigint |  | YES | (NULL) |
| WODIFYUSERID | int |  | YES | (NULL) |
| WORKATOUSERID | bigint |  | YES | ((0)) |
| CREATEDBY | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBY | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
