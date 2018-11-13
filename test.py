#!/usr/bin/env python3

import plotly.plotly as pp
import plotly.graph_objs as pg
import pandas as pd

# read in mortality data
data = pd.read_csv("out.csv")
# select age < 1 data
data = data[data.age_group_name == '<1 year']
# select the columns we need
data = data[['fit','year_id','sex']]

# prepare input data for graphing
male_data = pg.Scatter(
    x = data['year_id'][data['sex'] == 'Male'],
    y = data['fit'][data['sex'] == 'Male'],
    name = 'Male',
    mode ='markers',
    marker = dict(
        color = ('rgb(205, 12, 24)'))
)

female_data = pg.Scatter(
    x = data['year_id'][data['sex'] == 'Female'],
    y = data['fit'][data['sex'] == 'Female'],
    name = 'Female',
    mode ='markers',
    marker = dict(
        color = ('rgb(12, 12, 24)'))
)

data_both = [male_data, female_data]

# Edit the layout
layout = dict(title = 'Mortality Rate 1980 - 2040',
              xaxis = dict(title = 'Year'),
              yaxis = dict(title = 'Rate')
              )

fig = dict(data=data_both, layout=layout)
pp.iplot(fig, filename='line', auto_open=True)
