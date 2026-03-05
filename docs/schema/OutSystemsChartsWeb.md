# OutSystemsChartsWeb

## Tables

- [InternalChartType](#internalcharttype)
- [InternalXAxisValuesType](#internalxaxisvaluestype)
- [LegendPosition](#legendposition)
- [StackingType](#stackingtype)
- [XAxisValuesType](#xaxisvaluestype)

## InternalChartType
**Physical table:** `OSUSR_bjy_InternalChartType`  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## InternalXAxisValuesType
**Physical table:** `OSUSR_bjy_InternalXAxisValuesType`  
**Description:** The data type of labels displayed on the X-axis to format them.  Using ‘Auto’ means the type is inferred from the label of the first data point.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |

## LegendPosition
**Physical table:** `OSUSR_bjy_LegendPosition`  
**Description:** The position where the legend is displayed on charts.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## StackingType
**Physical table:** `OSUSR_bjy_StackingType`  
**Description:** The way to plot multiple data series on Area, Bar, or Column charts:     - ‘NoStacking’: plot data series side by side to compare them;     - ‘Stacked’: plot data series stacked to show their contribution to a total;     - ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## XAxisValuesType
**Physical table:** `OSUSR_bjy_XAxisValuesType`  
**Description:** The data type of labels displayed on the X-axis to format them.  Using ‘Auto’ means the type is inferred from the label of the first data point.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
