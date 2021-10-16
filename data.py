import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/Administrator/Desktop/Python/c103/line_chart.csv")

fig = px.line(df,x="Country", y="Per capita income", color ="Country", title="per capita income of countries")
fig.show()