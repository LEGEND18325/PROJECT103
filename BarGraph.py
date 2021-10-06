import pandas as pd
import plotly.express as px

df=pd.read_csv('CovidCasesData.csv')

figure = px.bar(df,x='date',y='cases',color='country',title='CovidCasesData')

figure.show()