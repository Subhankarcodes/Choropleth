import pandas as pd
import numpy as np
import cufflinks as cf
cf.go_offline()
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
df=pd.read_csv('2012_Election_Data')
data=dict(type='choropleth',
        colorscale = 'Viridis',
        reversescale = True,
          locations=df['State Abv'],
         locationmode='USA-states',
          z=df['Voting-Age Population (VAP)'],
          text=df['State'],
          colorbar={'title':'Elections of the States'})
layout=dict(title='State Elections',
            geo=dict(showframe=False,
                     projection=dict(type='conic conformal')))
choromap5=go.Figure(data=[data],layout=layout)
iplot(choromap5)