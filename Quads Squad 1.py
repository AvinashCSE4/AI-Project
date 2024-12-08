# prompt: Create an interactive dashboard to analyze and visualize crime rates by region

import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from ipywidgets import interact, interact_manual

# Sample crime data (replace with your actual data)
data = {'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
        'Year': [2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021],
        'Crime_Rate': [10, 12, 8, 9, 15, 14, 7, 6]}
df = pd.DataFrame(data)

# Interactive dashboard
@interact
def visualize_crime(Region=list(df['Region'].unique()),
                     Year=widgets.IntSlider(min=df['Year'].min(), max=df['Year'].max(), step=1, value=df['Year'].min())):

  filtered_df = df[(df['Region'] == Region) & (df['Year'] == Year)]

  fig = px.bar(filtered_df, x='Region', y='Crime_Rate', title=f"Crime Rate in {Region} for {Year}",
                labels={'Crime_Rate': 'Crime Rate'})
  fig.show()
