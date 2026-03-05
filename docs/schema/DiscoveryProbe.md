# DiscoveryProbe

## Tables

- [APIControl](#apicontrol)
- [ApplicationDef](#applicationdef)
- [ApplicationNode](#applicationnode)
- [ApplicationReference](#applicationreference)
- [Configuration](#configuration)
- [Domain](#domain)
- [DomainLayer](#domainlayer)
- [DomainReference](#domainreference)
- [DomainReferenceApplication](#domainreferenceapplication)
- [DomainReferenceModule](#domainreferencemodule)
- [DomainReferenceNameKind](#domainreferencenamekind)
- [ElementNode](#elementnode)
- [ImportMap_Application](#importmap-application)
- [ImportMap_Domain](#importmap-domain)
- [ImportMap_Element](#importmap-element)
- [ImportMap_Module](#importmap-module)
- [ImportMap_ModuleLayer](#importmap-modulelayer)
- [LifeTimeServiceUsers](#lifetimeserviceusers)
- [MenuItem](#menuitem)
- [ModuleDef](#moduledef)
- [ModuleEffort](#moduleeffort)
- [ModuleLayer](#modulelayer)
- [ModuleNode](#modulenode)
- [OldReference](#oldreference)
- [Reference](#reference)
- [ReferenceKind](#referencekind)
- [SnapShot](#snapshot)
- [Snapshot_json](#snapshot-json)
- [SnapShot_Stats](#snapshot-stats)
- [SnapShot_StatsApplications](#snapshot-statsapplications)
- [SnapShot_StatsDomain](#snapshot-statsdomain)
- [SnapShot_StatsModules](#snapshot-statsmodules)
- [SnapshotModuleDefTmp](#snapshotmoduledeftmp)
- [SnapshotToLoad](#snapshottoload)
- [SystemApps](#systemapps)
- [TimerStatus](#timerstatus)

## APIControl
**Physical table:** `OSUSR_mrn_APIControl`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| TIMERID | bigint |  | YES | ((0)) |
| TIMERNAME | nvarchar | 50 | YES | ('') |
| STARTTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENDTIME | datetime |  | YES | ('1900-01-01 00:00:00') |
| STATUS | int |  | YES | (NULL) |
| SNAPSHOTID | bigint |  | YES | ((0)) |

## ApplicationDef
**Physical table:** `OSUSR_mrn_ApplicationDef`  
**Description:** Stores the information about an OutSystems application and its violations  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| APPLICATIONID | int |  | YES | (NULL) |
| LAYER | int |  | YES | (NULL) |
| UPPERVIOLATIONS | nvarchar | -1 | YES | ('') |
| SIDEVIOLATIONS | nvarchar | -1 | YES | ('') |
| CYCLICVIOLATIONS | nvarchar | -1 | YES | ('') |
| FANIN | int |  | YES | ((0)) |
| FANOUT | int |  | YES | ((0)) |
| ISSELECTED | bit |  | YES | ((0)) |
| ISDELETED | bit |  | YES | ((0)) |
| DOMAINID | bigint |  | YES | (NULL) |
| TOTALVIOLATIONS | bigint |  | YES | ((0)) |
| UPPERVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| SIDEVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| CYCLICDEPENDENCIESCOUNTER | bigint |  | YES | ((0)) |

## ApplicationNode
**Physical table:** `OSUSR_mrn_ApplicationNode`  
**Description:** Ties an Application to a specific Snapshot  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SNAPSHOTID | int |  | YES | (NULL) |
| APPLICATIONDEFID | int |  | YES | (NULL) |
| NAME | nvarchar | 150 | YES | ('') |

## ApplicationReference
**Physical table:** `OSUSR_mrn_ApplicationReference`  
**Description:** Entity that stores the applications references  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SOURCEAPPLICATION | int |  | YES | (NULL) |
| TARGETAPPLICATION | int |  | YES | (NULL) |

## Configuration
**Physical table:** `OSUSR_mrn_Configuration`  
**Description:** Stores the general configurations for the Discovery application  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| EMAILID | int |  | YES | (NULL) |
| EMAILLIST | nvarchar | 2000 | YES | ('') |
| NRRECORDSTOSHOWINSCREENS | int |  | YES | ((0)) |
| SENDCYCLICVIOLATIONEMAIL | bit |  | YES | ((0)) |
| SENDUPPERVIOLATIONEMAIL | bit |  | YES | ((0)) |
| SENDSIDEVIOLATIONEMAIL | bit |  | YES | ((0)) |
| SENDDOMAINVIOLATION | bit |  | YES | ((0)) |
| OVERWRITEALREADYCLASSIFIED | bit |  | YES | ((0)) |
| USEDOMAIN | bit |  | YES | ((0)) |
| VERSION | nvarchar | 50 | YES | ('') |

## Domain
**Physical table:** `OSUSR_mrn_Domain1`  
**Description:** Defines an independent ecosystem that your teams can manage at their own pace and needs  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DOMAINLAYERID | int |  | YES | (NULL) |
| GUID | nvarchar | 100 | YES | ('') |
| LABEL | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| NUMBEROFTRESPASSERS | int |  | YES | ((0)) |
| HASVIOLATIONS | bit |  | YES | ((0)) |
| UPPERVIOLATIONS | nvarchar | -1 | YES | ('') |
| UPPERVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| SIDEVIOLATIONS | nvarchar | -1 | YES | ('') |
| SIDEVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| DOWNDEPENDENCIES | nvarchar | -1 | YES | ('') |
| DOWNDEPENDENCIESCOUNTER | int |  | YES | ((0)) |
| EXPOSEENTITIES | bit |  | YES | ((0)) |
| EXPOSEDENTITIESDOMAIN | nvarchar | -1 | YES | ('') |
| EXPOSEDENTITIESDOMAINCOUNTER | int |  | YES | ((0)) |
| EXPOSEACTIONS | bit |  | YES | ((0)) |
| EXPOSEDACTIONSDOMAIN | nvarchar | -1 | YES | ('') |
| EXPOSEDACTIONSDOMAINCOUNTER | int |  | YES | ((0)) |

## DomainLayer
**Physical table:** `OSUSR_mrn_DomainLayer`  
**Description:** Domain Layers  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| COLOR | nvarchar | 14 | YES | ('') |
| DESCRIPTION | nvarchar | 512 | YES | ('') |

## DomainReference
**Physical table:** `OSUSR_mrn_DomainReference`  
**Description:** Stores references between domains  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SOURCEDOMAINID | bigint |  | YES | (NULL) |
| TARGETDOMAINID | bigint |  | YES | (NULL) |

## DomainReferenceApplication
**Physical table:** `OSUSR_mrn_DomainReferenceApplication`  
**Description:** Stores information about references between domain applications  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DOMAINREFERENCEID | bigint |  | YES | (NULL) |
| SOURCEAPPLICATIONDEFID | int |  | YES | (NULL) |
| TARGETAPPLICATIONDEFID | int |  | YES | (NULL) |

## DomainReferenceModule
**Physical table:** `OSUSR_mrn_DomainReferenceModule`  
**Description:** Stores information about references between domain modules  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DOMAINREFERENCEAPPLICATIONID | bigint |  | YES | (NULL) |
| SOURCEMODULEDEFID | int |  | YES | (NULL) |
| TARGETMODULEDEFID | int |  | YES | (NULL) |

## DomainReferenceNameKind
**Physical table:** `OSUSR_mrn_DomainReferenceNameKind`  
**Description:** Stores information about the reference kind in a domain module  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DOMAINREFERENCEMODULEID | bigint |  | YES | (NULL) |
| NAME | nvarchar | 100 | YES | ('') |
| REFERENCEKINDID | bigint |  | YES | (NULL) |
| ELEMENTKIND | nvarchar | 50 | YES | ('') |

## ElementNode
**Physical table:** `OSUSR_mrn_ElementNode`  
**Description:** Stores the information about an OutSystems element and the Module/Snapshot it belongs to  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SNAPSHOTID | int |  | YES | (NULL) |
| MODULEDEFID | int |  | YES | (NULL) |
| NAME | nvarchar | 100 | YES | ('') |
| KIND | nvarchar | 50 | YES | ('') |
| SSKEY | nvarchar | 250 | YES | ('') |
| ISPUBLIC | bit |  | YES | ((0)) |

## ImportMap_Application
**Physical table:** `OSUSR_mrn_ImportMap_Application`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| INDEX | int |  | NO |  |
| APPLICATIONDEFID | int |  | YES | (NULL) |

## ImportMap_Domain
**Physical table:** `OSUSR_mrn_ImportMap_Domain1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| INDEX | int |  | NO |  |
| DOMAINID | bigint |  | YES | (NULL) |

## ImportMap_Element
**Physical table:** `OSUSR_mrn_ImportMap_Element`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| INDEX | int |  | NO |  |
| ELEMENTNODEID | int |  | YES | (NULL) |

## ImportMap_Module
**Physical table:** `OSUSR_mrn_ImportMap_Module`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| INDEX | int |  | NO |  |
| MODULEDEFID | int |  | YES | (NULL) |
| MODULENODEID | int |  | YES | (NULL) |

## ImportMap_ModuleLayer
**Physical table:** `OSUSR_mrn_ImportMap_ModuleLayer`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| INDEX | int |  | NO |  |
| MODULELAYERID | int |  | YES | (NULL) |

## LifeTimeServiceUsers
**Physical table:** `OSUSR_mrn_LifeTimeServiceUsers`  
**Description:** Stores the information about the LifeTime user set in the configurations  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| USERNAME | nvarchar | 50 | YES | ('') |
| PASSWORD | nvarchar | 500 | YES | ('') |
| KEY | varbinary | -1 | YES | (NULL) |
| LIFETIMEENVIRONMENTURL | nvarchar | 200 | YES | ('') |

## MenuItem
**Physical table:** `OSUSR_mrn_MenuItem`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| CAPTION | nvarchar | 50 | YES | ('') |

## ModuleDef
**Physical table:** `OSUSR_mrn_ModuleDef`  
**Description:** Stores the information about an OutSystems module and its violations  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 2000 | YES | ('') |
| SS_KEY | nvarchar | 250 | YES | ('') |
| KIND | nvarchar | 10 | YES | ('') |
| APPLICATIONDEFID | int |  | YES | (NULL) |
| ESPACEID | int |  | YES | (NULL) |
| EXTENSIONID | int |  | YES | (NULL) |
| LAYER | int |  | YES | (NULL) |
| UPPERVIOLATIONS | nvarchar | -1 | YES | ('') |
| SIDEVIOLATIONS | nvarchar | -1 | YES | ('') |
| CYCLICDEPENDENCIES | nvarchar | -1 | YES | ('') |
| FANIN | bigint |  | YES | ((0)) |
| FANOUT | bigint |  | YES | ((0)) |
| ISSELECTED | bit |  | YES | ((0)) |
| ISDELETED | bit |  | YES | ((0)) |
| TOTALVIOLATIONS | bigint |  | YES | ((0)) |
| UPPERVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| SIDEVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| CYCLICDEPENDENCIESCOUNTER | bigint |  | YES | ((0)) |
| WEAKUPPERVIOLATIONS | nvarchar | -1 | YES | ('') |
| WEAKUPPERVIOLATIONSCOUNTER | int |  | YES | ((0)) |

## ModuleEffort
**Physical table:** `OSUSR_mrn_ModuleEffort`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| SNAPSHOTID | int |  | YES | (NULL) |
| MODULEDEFID | int |  | YES | (NULL) |
| EFFORT | decimal |  | YES | ((0)) |

## ModuleLayer
**Physical table:** `OSUSR_mrn_ModuleLayer`  
**Description:** Stores the information about a Module Layer  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| DESCRIPTION | nvarchar | 256 | YES | ('') |
| SUFFIX | nvarchar | 50 | YES | ('') |
| PREFIX | nvarchar | 50 | YES | ('') |
| PARENTID | int |  | YES | (NULL) |
| ISEXTENSIONLAYER | bit |  | YES | ((0)) |
| CHECKSIDEVIOLATIONS | bit |  | YES | ((0)) |

## ModuleNode
**Physical table:** `OSUSR_mrn_ModuleNode`  
**Description:** Ties a Module to a specific Snapshot  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SNAPSHOTID | int |  | YES | (NULL) |
| APPLICATIONDEFID | int |  | YES | (NULL) |
| MODULEDEFID | int |  | YES | (NULL) |
| NAME | nvarchar | 100 | YES | ('') |
| SSKEY | nvarchar | 250 | YES | ('') |
| KIND | nvarchar | 10 | YES | ('') |
| AOS | int |  | YES | ((0)) |
| EFFORT | decimal |  | YES | ((0)) |

## OldReference
**Physical table:** `OSUSR_mrn_OldReference`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SNAPSHOTID | int |  | YES | (NULL) |
| SOURCEMODULENODEID | int |  | YES | (NULL) |
| TARGETELEMENTNODEID | int |  | YES | (NULL) |

## Reference
**Physical table:** `OSUSR_mrn_Reference`  
**Description:** Stores the information about references of a module's element in another module for a specific snapshot  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SNAPSHOTID | int |  | YES | (NULL) |
| SOURCEMODULENODEID | int |  | YES | (NULL) |
| TARGETELEMENTNODEID | int |  | YES | (NULL) |
| ISRECENT | bit |  | YES | ((0)) |

## ReferenceKind
**Physical table:** `OSUSR_mrn_ReferenceKind`  
**Description:** Reference Kinds (Outsystems Element types)  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| IS_ACTIVE | bit |  | YES | ((0)) |
| ALLOWFROMVERTORNULLTOVERT | bit |  | YES | ((0)) |
| ALLOWFROMVERTORNULLTOFOUND | bit |  | YES | ((0)) |
| ALLOWFROMFOUNDTOFOUND | bit |  | YES | ((0)) |
| ALLOWFROMFOUNDTOVERT | bit |  | YES | ((0)) |
| ISSTRONGREFERENCE | bit |  | YES | ((0)) |
| ISNOTCYCLE | bit |  | YES | ((0)) |
| ENABLEVIOLATIONS | bit |  | YES | ((0)) |

## SnapShot
**Physical table:** `OSUSR_mrn_SnapShot`  
**Description:** Entity used to keep information about Snapshots  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| INSTANT | datetime |  | YES | ('1900-01-01 00:00:00') |
| ENVIRONMENTNAME | nvarchar | 100 | YES | ('') |
| INPROGRESS | bit |  | YES | ((0)) |
| JSONVERSION | nvarchar | 50 | YES | ('') |

## Snapshot_json
**Physical table:** `OSUSR_mrn_Snapshot_json`  
**Description:** Entity used to keep the JSON text regarding a specific Snapshot  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| JSON | nvarchar | -1 | YES | ('') |

## SnapShot_Stats
**Physical table:** `OSUSR_mrn_SnapShot_Stats`  
**Description:** Entity with the agregator of the snapshots statistics taken on the environment only ( only snapshots of the enviorment activation code will be created )  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SNAPSHOTID | int |  | YES | (NULL) |
| SNAPSHOTDATE | datetime |  | YES | ('1900-01-01 00:00:00') |

## SnapShot_StatsApplications
**Physical table:** `OSUSR_mrn_SnapShot_StatsApplications`  
**Description:** Entity with the agregator of the snapshots statistics taken on the environment for all active aplications  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| DOMAINGUID | nvarchar | 100 | YES | ('') |
| SNAPSHOT_STATSID | bigint |  | YES | (NULL) |
| APPLICATIONID | int |  | YES | (NULL) |
| UPPERVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| SIDEVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| CYCLICDEPENDENCIESCOUNTER | bigint |  | YES | ((0)) |
| TOTALCOUNTER | bigint |  | YES | ((0)) |

## SnapShot_StatsDomain
**Physical table:** `OSUSR_mrn_SnapShot_StatsDomain`  
**Description:** Entity with the agregator of the snapshots statistics taken on the environment for all active Domains  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SNAPSHOT_STATSID | bigint |  | YES | (NULL) |
| DOMAINGUID | nvarchar | 100 | YES | ('') |
| NUMBEROFTRESPASSERS | bigint |  | YES | ((0)) |
| UPPERVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| SIDEVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| DOWNDEPENDENCIESCOUNTER | int |  | YES | ((0)) |

## SnapShot_StatsModules
**Physical table:** `OSUSR_mrn_SnapShot_StatsModules`  
**Description:** Entity with the agregator of the snapshots statistics taken on the environment for all active modules  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| SNAPSHOT_STATSID | bigint |  | YES | (NULL) |
| APPLICATIONID | int |  | YES | (NULL) |
| SS_KEY | nvarchar | 250 | YES | ('') |
| UPPERVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| SIDEVIOLATIONSCOUNTER | bigint |  | YES | ((0)) |
| CYCLICDEPENDENCIESCOUNTER | bigint |  | YES | ((0)) |
| TOTALCOUNTER | bigint |  | YES | ((0)) |

## SnapshotModuleDefTmp
**Physical table:** `OSUSR_mrn_SnapshotModuleDefTmp`  
**Description:** Auxiliary table for module definition fans  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| FANOUT | int |  | YES | ((0)) |
| MODULEDEFID | int |  | YES | (NULL) |
| SNAPSHOTID | int |  | YES | (NULL) |

## SnapshotToLoad
**Physical table:** `OSUSR_mrn_SnapshotToLoad`  
**Description:** Entity used to keep information about which Snapshot is waiting to be loaded  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| SNAPSHOTID | int |  | YES | (NULL) |
| KEEPLAYERS | bit |  | YES | ((0)) |

## SystemApps
**Physical table:** `OSUSR_mrn_SystemApps`  
**Description:** Applications to exclude from analysis  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| IGNORE | bit |  | YES | ((0)) |

## TimerStatus
**Physical table:** `OSUSR_mrn_TimerStatus`  
**Description:** Static Entity with Timer Status  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |
