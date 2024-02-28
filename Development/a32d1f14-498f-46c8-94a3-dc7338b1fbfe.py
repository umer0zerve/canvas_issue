def rename_columns(column_name):
    if '_x' in column_name:
        return column_name.replace('_x', '_team')
    elif '_y' in column_name:
        return column_name.replace('_y', '_player')
    else:
        return column_name


team = pd.read_csv('team_traditional.csv')
team['teamid'] = team['teamid'].astype("string")
player = pd.read_csv('traditional.csv', usecols=['gameid',  'playerid', 'player',  'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA',
       'FT%', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', '+/-'])

merged_df = pd.merge(team, player, on='gameid')
merged_df.columns = [rename_columns(col) for col in merged_df.columns]


print(merged_df)