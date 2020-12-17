import pandas as pd
import numpy as np
import cufflinks as cf
cf.go_offline()
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
df=pd.read_csv('2011_US_AGRI_Exports')
data=dict(type='choropleth',
          locations=df['code'],
          locationmode='USA-states',
          colorscale='Portland',
          text=df['text'],
          z=df['total exports'],
          marker = dict(line = dict(color = 'rgb(255,255,255)',width = 2)),
          colorbar={'title':'Millions'})
layout=dict(title='2011 US agri exports',
            geo=dict(scope='usa',
                     showlakes=False,
                     lakecolor='rgb(85,173,240)'))
choromap2=go.Figure(data=[data],layout=layout)
iplot(choromap2)

