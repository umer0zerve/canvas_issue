import plotly.express as px


merged_df['date'] = pd.to_datetime(merged_df['date'])
merged_df['year'] = merged_df['date'].dt.year.astype(str)


total_points = merged_df.groupby(['year', 'team'])['PTS_team'].sum().reset_index()


top_10_teams = total_points.groupby('team')['PTS_team'].sum().nlargest(10).index


filtered_df = total_points[total_points['team'].isin(top_10_teams)]


fig = px.line(filtered_df, x='year', y='PTS_team', color='team',
              title='Top 10 Teams - Total Points Over Time',
              labels={'PTS_team': 'Total Points', 'year': 'Year'},
              line_group='team')


fig.update_layout(xaxis=dict(categoryorder='category ascending'))


fig.update_traces(marker=dict(size=8), line=dict(width=2))
fig.update_layout(
    legend=dict(title_text='Team'),
    font=dict(family='Arial, sans-serif', size=12, color='RebeccaPurple'),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_title_font=dict(color="white"),
    yaxis_title_font=dict(color="white"),
    legend_title_font=dict(color="white"),
    legend_font=dict(color="white"),
    title_font=dict(color="white"),
    xaxis=dict(tickfont=dict(color="white")),
    yaxis=dict(tickfont=dict(color="white")),
)

fig.show()