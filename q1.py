import pandas as pd
import numpy as np
import cufflinks as cf
cf.go_offline()
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
df=pd.read_csv('2014_World_Power_Consumption')
data=dict(type='choropleth',
        colorscale = 'Viridis',
        reversescale = True,
          locations=df['Country'],
         locationmode='country names',
          z=df['Power Consumption KWH'],
          text=df['Text'],
          colorbar={'title':'Power Consumption of the World'})
layout=dict(title='World Power Consumption 2014',
            geo=dict(showframe=False,
                     projection=dict(type='conic conformal')))
choromap4=go.Figure(data=[data],layout=layout)
iplot(choromap4)