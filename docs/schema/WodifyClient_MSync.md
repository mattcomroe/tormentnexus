# WodifyClient_MSync

## Tables

- [CommonClientVariableSyncSteps](#commonclientvariablesyncsteps)
- [FeatureSpecificClientVariables](#featurespecificclientvariables)
- [LocalClientVariable](#localclientvariable)
- [LocalFeatureSpecificClientVariable](#localfeaturespecificclientvariable)
- [LocalSyncAtom_TimeStamps](#localsyncatom-timestamps)
- [SyncUnits](#syncunits)

## CommonClientVariableSyncSteps
**Physical table:** `OSUSR_uu0_CommonClientVariableSyncSteps`  
**Description:** Add a data step here, then update the common client variable helper to mapp the attribute to this data step  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((1)) |
| TTL | int |  | YES | ((0)) |

## FeatureSpecificClientVariables
**Physical table:** `OSUSR_uu0_FeatureSpecificClientVariables1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| TTL_MINUTES | int |  | YES | ((0)) |

## LocalClientVariable
**Physical table:** `OSUSR_uu0_LocalClientVariable`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## LocalFeatureSpecificClientVariable
**Physical table:** `OSUSR_uu0_LocalFeatureSpecificClientVariable`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## LocalSyncAtom_TimeStamps
**Physical table:** `OSUSR_uu0_LocalSyncAtom_TimeStamps`  

_Table not present in the dev environment — schema unavailable. May exist in production only._

## SyncUnits
**Physical table:** `OSUSR_uu0_SyncUnits`  
**Description:** SyncUnits used for offline syncronization  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
| ISFULLSYNC | bit |  | YES | ((0)) |
