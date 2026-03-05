# OutSystemsCharts

## Tables

- [AxisType](#axistype)
- [AxisValuesType](#axisvaluestype)
- [ChartEvent](#chartevent)
- [ChartProvider](#chartprovider)
- [HighchartModules](#highchartmodules)
- [LegendLayout](#legendlayout)
- [LegendPosition](#legendposition)
- [LegendPosition_v1](#legendposition-v1)
- [OSChartVersion](#oschartversion)
- [SeriesEvent](#seriesevent)
- [SeriesEvent_v1](#seriesevent-v1)
- [SeriesType](#seriestype)
- [StackingType](#stackingtype)
- [StackingType_v1](#stackingtype-v1)
- [ValuesType](#valuestype)
- [XAxisType](#xaxistype)
- [XAxisValuesType_v1](#xaxisvaluestype-v1)

## AxisType
**Physical table:** `OSUSR_7VO_AXISTYPE`  

_Column definitions not found in schema export._

## AxisValuesType
**Physical table:** `OSUSR_7VO_AXISVALUESTYPE`  

_Column definitions not found in schema export._

## ChartEvent
**Physical table:** `OSUSR_7VO_CHARTEVENT`  

_Column definitions not found in schema export._

## ChartProvider
**Physical table:** `OSUSR_7VO_CHARTPROVIDER`  

_Column definitions not found in schema export._

## HighchartModules
**Physical table:** `OSUSR_7VO_HIGHCHARTMODULES`  
**Description:** Additional Highcharts modules that can be referenced.  

_Column definitions not found in schema export._

## LegendLayout
**Physical table:** `OSUSR_7VO_LEGENDLAYOUT`  
**Description:** The legend position in chart  

_Column definitions not found in schema export._

## LegendPosition
**Physical table:** `OSUSR_7VO_LEGENDPOSITION`  

_Column definitions not found in schema export._

## LegendPosition_v1
**Physical table:** `OSUSR_HM2_LEGENDPOSITION`  
**Description:** The legend position in chart  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## OSChartVersion
**Physical table:** `OSUSR_7VO_OSCHARTVERSION`  

_Column definitions not found in schema export._

## SeriesEvent
**Physical table:** `OSUSR_7VO_SERIESEVENT1`  

_Column definitions not found in schema export._

## SeriesEvent_v1
**Physical table:** `OSUSR_7VO_SERIESEVENT`  

_Column definitions not found in schema export._

## SeriesType
**Physical table:** `OSUSR_7VO_SERIESTYPE`  

_Column definitions not found in schema export._

## StackingType
**Physical table:** `OSUSR_7VO_STACKINGTYPE`  
**Description:** The way to plot multiple data series on Area, Bar, or Column charts:     - ‘NoStacking’: plot data series side by side to compare them;     - ‘Stacked’: plot data series stacked to show their contribution to a total;     - ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.  

_Column definitions not found in schema export._

## StackingType_v1
**Physical table:** `OSUSR_HM2_STACKINGTYPE`  
**Description:** The way to plot multiple data series on Area, Bar, or Column charts:     - ‘NoStacking’: plot data series side by side to compare them;     - ‘Stacked’: plot data series stacked to show their contribution to a total;     - ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ValuesType
**Physical table:** `OSUSR_7VO_VALUESTYPE`  
**Description:** Set how the chart labels are handled to be displayed on the chart. The type of the values can be:  - Integer: the labels will be displayed as integer numbers.  - Decimal: the labels will be displayed as decimal numbers.  - Datetime: the labels will be displayed as datetimes.  - Text: the labels will be displayed as text and treated as categories. By default, the type is Text.  

_Column definitions not found in schema export._

## XAxisType
**Physical table:** `OSUSR_7VO_XAXISTYPE`  

_Column definitions not found in schema export._

## XAxisValuesType_v1
**Physical table:** `OSUSR_HM2_XAXISVALUESTYPE`  
**Description:** The data type of labels displayed on the X-axis to format them.  Using ‘Auto’ means the type is inferred from the label of the first data point.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
