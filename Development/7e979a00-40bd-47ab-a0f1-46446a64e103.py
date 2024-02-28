
team_columns = ['team', 'TOV_team', 'PF_team', 'win']
player_columns = ['player', 'TOV_player', 'PF_player', 'win']

plt.figure(figsize=(14, 8))
for column in player_columns[1:]:
    sns.lineplot(x='season', y=column, data=player_season_avg, label=column)

plt.title('Player Performance Trends Over Seasons')
plt.xlabel('Season')
plt.ylabel('Average Value')
plt.legend()
plt.show()