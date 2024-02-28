import plotly.express as px

fig = px.box(merged_df, x='home', y='PTS_team', points="all",
             title='Home vs Away Performance',
             labels={'home': 'Location', 'PTS_team': 'Points'},
             category_orders={'home': ['home', 'away']})

fig.update_layout(xaxis=dict(tickangle=45))

fig.show()
