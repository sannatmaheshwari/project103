import pandas as x
import plotly.express as y

df = x.read_csv("covid.csv")
report = y.scatter(df,x="date",y="cases",color="country")
report.show()