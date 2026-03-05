# WodifyClient_MSync

## Tables

- [CommonClientVariableSyncSteps](#commonclientvariablesyncsteps)
- [FeatureSpecificClientVariables](#featurespecificclientvariables)
- [LocalClientVariable](#localclientvariable)
- [LocalFeatureSpecificClientVariable](#localfeaturespecificclientvariable)
- [LocalSyncAtom_TimeStamps](#localsyncatom-timestamps)
- [SyncUnits](#syncunits)

## CommonClientVariableSyncSteps
**Physical table:** `OSUSR_UU0_COMMONCLIENTVARIABLESYNCSTEPS`  
**Description:** Add a data step here, then update the common client variable helper to mapp the attribute to this data step  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((1)) |
| TTL | int |  | YES | ((0)) |

## FeatureSpecificClientVariables
**Physical table:** `OSUSR_UU0_FEATURESPECIFICCLIENTVARIABLES1`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ISACTIVE | bit |  | YES | ((0)) |
| TTL_MINUTES | int |  | YES | ((0)) |

## LocalClientVariable
**Physical table:** `OSUSR_UU0_LOCALCLIENTVARIABLE`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions not found in schema export._

## LocalFeatureSpecificClientVariable
**Physical table:** `OSUSR_UU0_LOCALFEATURESPECIFICCLIENTVARIABLE`  
**Description:** Store single attribute configuration settings. These will persist past a lost session.  

_Column definitions not found in schema export._

## LocalSyncAtom_TimeStamps
**Physical table:** `OSUSR_UU0_LOCALSYNCATOM_TIMESTAMPS`  

_Column definitions not found in schema export._

## SyncUnits
**Physical table:** `OSUSR_UU0_SYNCUNITS`  
**Description:** SyncUnits used for offline syncronization  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| LABEL | nvarchar | 50 | NO |  |
| ISFULLSYNC | bit |  | YES | ((0)) |
