from calendar import week
import justpy as jp
import pandas as pd 
from datetime import datetime
from pytz import utc
df1=pd.read_csv("reviews.csv",parse_dates=['Timestamp'])
share=df1.groupby(['Course Name'])['Rating'].count()
chart_def="""
{
    chart: {
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in May, 2020'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 70.67,
            sliced: true,
            selected: true
        }, {
            name: 'Edge',
            y: 14.77
        },  {
            name: 'Firefox',
            y: 4.86
        }, {
            name: 'Safari',
            y: 2.63
        }, {
            name: 'Internet Explorer',
            y: 1.53
        },  {
            name: 'Opera',
            y: 1.40
        }, {
            name: 'Sogou Explorer',
            y: 0.84
        }, {
            name: 'QQ',
            y: 0.51
        }, {
            name: 'Other',
            y: 2.6
        }]
    }]
}
"""
def simple_BasicApp():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp,text="Analysis of course review",classes="text-h3 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="These are the graph for course review")
    hc=jp.HighCharts(a=wp,options=chart_def)
    hc.options.title.text="Average rating by month"
    hc_data=[{"name":v1,"y":v2} for v1,v2 in zip(share.index,share)]
    hc.options.series[0].data=hc_data
    return wp
jp.justpy(simple_BasicApp)