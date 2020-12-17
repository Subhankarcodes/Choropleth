import pandas as pd
import numpy as np
import cufflinks as cf
cf.go_offline()
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
df=pd.read_csv('gdp-ppp-csv-.csv')
data=dict(type='choropleth',
          locations=df['Economy'],
          z=df['(millions of international dollars)'],
          text=df['Economy'],
          colorbar={'title':'GDP in Millions'})
layout = dict(
    title = '2017 Global GDP',
    geo = dict(
        showframe = False,
        projection = dict(type = 'azimuthal equal area')
    ))
choromap3 = go.Figure(data = [data],layout = layout)
iplot(choromap3)