# WDS_Component_Sandbox

## Tables

- [Timer](#timer)
- [TimerIntervals](#timerintervals)

## Timer
**Physical table:** `OSUSR_qp6_Timer`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| NUMBEROFSETS | int |  | YES | ((0)) |
| RESTBETWEENSETSSECONDS | int |  | YES | ((0)) |
| RESTBETWEENSETSCOLOR | nvarchar | 50 | YES | ('') |
| RESTBETWEENINTERVALSSECONDS | int |  | YES | ((0)) |
| RESTBETWEENINTERVALSCOLOR | nvarchar | 50 | YES | ('') |
| WARMUPSECONDS | int |  | YES | ((0)) |
| WARMUPCOLOR | nvarchar | 50 | YES | ('') |
| COOLDOWNSECONDS | int |  | YES | ((0)) |
| COOLDOWNCOLOR | nvarchar | 50 | YES | ('') |

## TimerIntervals
**Physical table:** `OSUSR_qp6_TimerIntervals`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | bigint |  | NO |  |
| NAME | nvarchar | 50 | YES | ('') |
| TIMESECONDS | int |  | YES | ((0)) |
| COLOR | nvarchar | 50 | YES | ('') |
| TIMERID | bigint |  | YES | (NULL) |
