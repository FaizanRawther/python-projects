from turtle import color, width
from WebcamFaceDetection import df1
from bokeh.plotting import output_file,show,curdoc,figure
from bokeh.models import HoverTool, ColumnDataSource
 
df1["Start_string"] = df1["Start"].dt.strftime('%Y-%m-%d %H:%M:%S')
df1["End_string"] = df1["End"].dt.strftime('%Y-%m-%d %H:%M:%S')
 
from WebcamFaceDetection import df1
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
import pandas
 
cds = ColumnDataSource(df1)
 
p = figure(
    x_axis_type = "datetime",
    height = 100,
    width = 500,
    sizing_mode = "scale_both",
    title = "Motion graph"
)
 
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1
 
hover = HoverTool(
    tooltips = [
        ("Start", "@Start{%d/%m/%Y %H:%M:%S}"), 
        ("End", "@End{%d/%m/%Y %H:%M:%S}")
    ],
    formatters = {
        "@Start" : "datetime",
        "@End" : "datetime"
    }
)
p.add_tools(hover)
 
q = p.quad(
    left = "Start", 
    right = "End", 
    bottom = 0, 
    top = 1,
    color = "green",
    source = cds
)
 
output_file("Graph.html")
show(p)