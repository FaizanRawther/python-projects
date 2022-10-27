#to analyse in 5 min
import pandas as pd
from pandas_profiling import ProfileReport
df1=pd.read_excel("children_stats_only (2).xlsx")
print(df1)
#generate a report
profile=ProfileReport(df1)
profile.to_file(output_file="childrenStats.html")