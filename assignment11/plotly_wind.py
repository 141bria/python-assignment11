## TASK 3
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))