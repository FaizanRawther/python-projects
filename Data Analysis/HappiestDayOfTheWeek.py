import justpy as jp
import pandas as pd 
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt
df1=pd.read_csv("reviews.csv",parse_dates=['Timestamp'])
df1['Weekday']=df1['Timestamp'].dt.strftime('%A')
df1['Daynumber']=df1['Timestamp'].dt.strftime('%w')
weekDay_average=df1.groupby(['Weekday','Daynumber']).mean()
weekDay_average=weekDay_average.sort_values('Daynumber')
chart_def="""
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Reviews'
    },
    subtitle: {
        text: 'Average rating of course'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Days'
        },
        labels: {
            format: '{value} '
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Rating'
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
        pointFormat: '{point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: '',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""
def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp,text="Analysis of course review",classes="text-h3 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="These are the graph for course review")
    hc=jp.HighCharts(a=wp,options=chart_def)
    hc.options.xAxis.categories=list(weekDay_average.index.get_level_values(0))
    hc.options.series[0].data=list(weekDay_average['Rating'])
    return wp
jp.justpy(app)