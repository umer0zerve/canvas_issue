
team_columns = ['team', 'PTS_team', 'FG%_team', '3P%_team', 'FT%_team', 'REB_team', 'AST_team', 'STL_team', 'BLK_team', 'TOV_team', 'PF_team']
player_columns = ['player', 'PTS_player', 'FG%_player', '3P%_player', 'FT%_player', 'REB_player', 'AST_player', 'STL_player', 'BLK_player', 'TOV_player', 'PF_player']

team_avg = merged_df[team_columns].groupby('team').mean().reset_index()
player_avg = merged_df[player_columns].groupby('player').mean().reset_index()

plt.figure(figsize=(16, 8))
bar_width = 0.35
index = range(len(team_columns[1:]))
bar_positions_team = [i for i in index]
bar_positions_player = [i + bar_width for i in index]

for i, column in enumerate(team_columns[1:]):
    plt.bar(bar_positions_team[i], team_avg[column], width=bar_width, label=f'Team - {column}')

for i, column in enumerate(player_columns[1:]):
    plt.bar(bar_positions_player[i], player_avg[column], width=bar_width, label=f'Player - {column}')

plt.xlabel('Categories')
plt.ylabel('Average Value')
plt.title('Comparison of Team and Player Performance in Specific Categories')
plt.xticks([p + bar_width / 2 for p in index], team_columns[1:])
plt.legend()
plt.show()
