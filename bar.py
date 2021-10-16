import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/Administrator/Desktop/Python/c103/data.csv")

fig = px.bar(df,x="Country", y="InternetUsers")
fig.show()