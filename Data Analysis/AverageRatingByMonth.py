from calendar import week
import justpy as jp
import pandas as pd 
from datetime import datetime
from pytz import utc
df1=pd.read_csv("reviews.csv",parse_dates=['Timestamp'])
df1['Month']=df1['Timestamp'].dt.strftime('%Y-%m')
month_average=df1.groupby(['Month']).mean()
chart_def="""
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average rating by month'
    },
    subtitle: {
        text: 'mean of Average rating by month'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'DATE'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: 'month{point.x}: rating{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Average Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}"""
def simple_BasicApp():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp,text="Analysis of course review",classes="text-h3 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="These are the graph for course review")
    hc=jp.HighCharts(a=wp,options=chart_def)
    hc.options.title.text="Average rating by month"
    hc.options.xAxis.categories=list(month_average.index)
    hc.options.series[0].data=list(month_average['Rating'])
    return wp
jp.justpy(simple_BasicApp)