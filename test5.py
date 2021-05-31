import pandas as pd
import plotly.express as px
import numpy as np
import plotly.io as pio

data = pd.read_csv('https://raw.githubusercontent.com/nurfnick/COVID_Travel/master/Combined.csv')

scatter = px.scatter(data, x='COVID Cases', y="Workplace Travel", animation_frame='Date',animation_group='FIPS',
          size='Population',color='State', hover_name='County',
          range_x=[1,200000], range_y=[-90,50], log_x=True)
scatter.show()

masks = pd.read_csv('https://raw.githubusercontent.com/nurfnick/COVID_Travel/master/mask_requirements.csv')
dates = pd.to_datetime(pd.unique(data.Date))
day = masks.iloc[1,1]
dates[dates > day]
data['Dates'] = pd.to_datetime(data.Date)
data['Masks']=0
for i in range (0,len(masks)):
    data.loc[(data['State']==masks.iloc[i,0])&(data['Dates']>pd.to_datetime(masks.iloc[i,1])),"Masks"]=1
data.loc[(data['State'] == masks.iloc[i, 0]) & (data['Dates'] > pd.to_datetime(masks.iloc[i, 1]))]
mask = px.scatter(data, x='COVID Cases', y="Workplace Travel",
          animation_frame='Date',animation_group='FIPS',symbol = 'Masks',
          size='Population',color='State', hover_name='County',
          range_x=[1,200000], range_y=[-90,50], log_x=True)
mask.update_layout(template='plotly_white')
mask.update_layout(title='COVID cases and Workplace Travel by County in US')
mask.show()