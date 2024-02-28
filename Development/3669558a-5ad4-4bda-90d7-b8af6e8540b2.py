
team_columns = ['team', 'TOV_team', 'PF_team', 'win']
player_columns = ['player', 'TOV_player', 'PF_player', 'win']


plt.figure(figsize=(14, 8))
plt.scatter(merged_df['TOV_team'], merged_df['PF_team'], c=merged_df['win'], cmap='coolwarm', alpha=0.7)
plt.title('Impact of Turnovers and Fouls on Team Game Outcomes')
plt.xlabel('Turnovers')
plt.ylabel('Personal Fouls')
plt.colorbar(label='Win (1: Win, 0: Loss)')
plt.show()

