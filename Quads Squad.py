# prompt: Create an interactive dashboard to analyze and visualize crime rates by region  pie chart

import pandas as pd
import plotly.express as px

# Sample crime data (replace with your actual data)
data = {'Region': ['North', 'South', 'East', 'West'],
        'Crime_Rate': [150, 100, 75, 50]}
df = pd.DataFrame(data)

# Create interactive pie chart
fig = px.pie(df, values='Crime_Rate', names='Region', title='Crime Rates by Region',
             color_discrete_sequence=px.colors.sequential.RdBu)

# Customize chart (optional)
fig.update_traces(textposition='inside', textinfo='percent+label')

# Show the chart
fig.show()