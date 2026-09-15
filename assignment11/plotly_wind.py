## TASK 3
import plotly.express as px
import plotly.data as pldata
df = pldata.wind(return_type='pandas')
print(df.head(10))
print(df.tail(10))
float()
df["strength"] = df["strength"].str.replace(r"-.*|\+","",regex=True).astype(float)
fig = px.scatter(df, x= 'strength',y='frequency',color='direction')
fig.write_html("wind.html",auto_open=True)