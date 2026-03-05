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
**Physical table:** `OSUSR_7vo_AxisType`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## AxisValuesType
**Physical table:** `OSUSR_7vo_AxisValuesType`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ChartEvent
**Physical table:** `OSUSR_7vo_ChartEvent`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## ChartProvider
**Physical table:** `OSUSR_7vo_ChartProvider`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## HighchartModules
**Physical table:** `OSUSR_7vo_HighchartModules`  
**Description:** Additional Highcharts modules that can be referenced.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LegendLayout
**Physical table:** `OSUSR_7vo_LegendLayout`  
**Description:** The legend position in chart  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LegendPosition
**Physical table:** `OSUSR_7vo_LegendPosition`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## LegendPosition_v1
**Physical table:** `OSUSR_hm2_LegendPosition`  
**Description:** The legend position in chart  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## OSChartVersion
**Physical table:** `OSUSR_7vo_OSChartVersion`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## SeriesEvent
**Physical table:** `OSUSR_7vo_SeriesEvent1`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## SeriesEvent_v1
**Physical table:** `OSUSR_7vo_SeriesEvent`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## SeriesType
**Physical table:** `OSUSR_7vo_SeriesType`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## StackingType
**Physical table:** `OSUSR_7vo_StackingType`  
**Description:** The way to plot multiple data series on Area, Bar, or Column charts:     - ‘NoStacking’: plot data series side by side to compare them;     - ‘Stacked’: plot data series stacked to show their contribution to a total;     - ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## StackingType_v1
**Physical table:** `OSUSR_hm2_StackingType`  
**Description:** The way to plot multiple data series on Area, Bar, or Column charts:     - ‘NoStacking’: plot data series side by side to compare them;     - ‘Stacked’: plot data series stacked to show their contribution to a total;     - ‘Stacked100Percent’: plot data series stacked to show their percentage in a total.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| ORDER | int |  | YES | ((0)) |
| IS_ACTIVE | bit |  | YES | ((0)) |

## ValuesType
**Physical table:** `OSUSR_7vo_ValuesType`  
**Description:** Set how the chart labels are handled to be displayed on the chart. The type of the values can be:  - Integer: the labels will be displayed as integer numbers.  - Decimal: the labels will be displayed as decimal numbers.  - Datetime: the labels will be displayed as datetimes.  - Text: the labels will be displayed as text and treated as categories. By default, the type is Text.  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## XAxisType
**Physical table:** `OSUSR_7vo_XAxisType`  

_Column definitions pending — not found in initial schema export. Run `scripts/missing_outsystems.sql` to populate._

## XAxisValuesType_v1
**Physical table:** `OSUSR_hm2_XAxisValuesType`  
**Description:** The data type of labels displayed on the X-axis to format them.  Using ‘Auto’ means the type is inferred from the label of the first data point.  

| Column | Data Type | Max Length | Nullable | Default |
|--------|-----------|------------|----------|---------|
| ID | int |  | NO |  |
| LABEL | nvarchar | 50 | YES | ('') |
| ORDER | int |  | YES | ((0)) |
