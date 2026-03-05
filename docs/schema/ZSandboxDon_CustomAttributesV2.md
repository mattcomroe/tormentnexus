# ZSandboxDon_CustomAttributesV2

## Tables

- [CustomAttributeDefinition](#customattributedefinition)
- [CustomAttributeDetail](#customattributedetail)
- [CustomAttributeGroup](#customattributegroup)
- [CustomAttributeLead](#customattributelead)
- [CustomAttributeLeadDetail](#customattributeleaddetail)
- [CustomAttributeType](#customattributetype)
- [CustomAttributeUserResponses](#customattributeuserresponses)
- [ObjectDefinition](#objectdefinition)

## CustomAttributeDefinition
**Physical table:** `OSUSR_pfh_CustomAttributeDefinition`  
**Description:** This table serves as the foundation for defining custom attributes, akin to a questionnaire for new gym members. It outlines specific questions (attributes) such as t-shirt size or fitness goals, aimed at personalizing the member's experience. The design ensures consistency and adaptability, with changes to questions handled by introducing new versions rather than altering existing records.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| ATTRIBUTENAME | nvarchar | 50 | YES | ('') |
| CUSTOMATTRIBUTEUIUSAGEID | int |  | YES | (NULL) |
| OBJECTDEFINITIONID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |
| ATTRIBUTELABEL | nvarchar | 50 | YES | ('') |
| CUSTOMATTRIBUTETYPEID | int |  | YES | (NULL) |
| CUSTOMATTRIBUTEGROUPID | int |  | YES | (NULL) |
| USERPROMPT | nvarchar | 1999 | YES | ('') |

## CustomAttributeDetail
**Physical table:** `OSUSR_pfh_CustomAttributeDetail`  
**Description:** Details the presentation and options of each custom attribute defined in the CustomAttributeDefinition table, using JSON to offer a flexible format. This enables a variety of question types and answer options, such as selecting a t-shirt size, enhancing the user's interaction by tailoring the interface to their needs.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CUSTOMATTRIBUTEDEFINITIONID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| JSON | nvarchar | -1 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## CustomAttributeGroup
**Physical table:** `OSUSR_pfh_CustomAttributeGroup`  
**Description:** the CustomAttributeGroup table groups related questions together, much like grouping fitness classes into categories such as cardio, strength, and flexibility. This organization helps in managing and presenting related custom attributes cohesively.  Key Elements: Each group has a label and a description, providing clarity on what types of custom attributes it contains and how they're used to enhance the gym member's experience.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 1999 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## CustomAttributeLead
**Physical table:** `OSUSR_pfh_CustomAttributeLead`  
**Description:** Extends the custom attribute system to potential gym members (leads), capturing custom attributes specific to leads. This facilitates personalized engagement strategies based on the collected attributes.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| CUSTOMATTRIBUTEDEFINITIONID | int |  | YES | (NULL) |
| LEADID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## CustomAttributeLeadDetail
**Physical table:** `OSUSR_pfh_CustomAttributeLeadDetail`  
**Description:** Stores the responses or data entered for each custom attribute by leads, using a JSON format to capture the details flexibly. This allows for a tailored approach in managing lead information, enhancing engagement and personalization.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| CUSTOMATTRIBUTELEADID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| JSON | nvarchar | -1 | YES | ('') |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## CustomAttributeType
**Physical table:** `OSUSR_pfh_CustomAttributeUIUsage`  
**Description:** This table maps each custom attribute to a specific user interface (UI) element, ensuring that data collection is both consistent and intuitive. By defining the type of UI element (e.g., dropdown list, text field, checkbox) associated with each custom attribute, the system standardizes how information is presented and collected across different parts of the application. This harmonization is crucial for maintaining a user-friendly experience, as it allows for the seamless integration of custom attributes into the system's UI.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| ISJSONDEPENDENT | bit |  | YES | ((0)) |

## CustomAttributeUserResponses
**Physical table:** `OSUSR_pfh_CustomeAttributeUserResponses`  
**Description:** Captures users' responses to custom attributes, linking each response to a specific user and client. This facilitates personalized interactions and services based on user preferences and behaviors.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| GUID | nvarchar | 50 | YES | ('') |
| CLIENTID | nvarchar | 50 | YES | ('') |
| USERID | int |  | YES | (NULL) |
| CREATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| CREATEDBYUSERID | int |  | YES | (NULL) |
| UPDATEDON | datetime |  | YES | ('1900-01-01 00:00:00') |
| UPDATEDBYUSERID | int |  | YES | (NULL) |
| ISACTIVE | bit |  | YES | ((0)) |

## ObjectDefinition
**Physical table:** `OSUSR_pfh_ObjectDefinition`  
**Description:** The ObjectDefinition table functions as a categorization framework within the gym management system, distinguishing different types of individuals and activities based on their association and role. This table segregates entities into meaningful categories such as 'Client', 'Lead', and 'Class', akin to identifying members by their engagement level or assigning activities to specific fitness goals. Each category, whether representing a person or an activity, is defined to reflect where data is stored and retrieved from.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
