import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df2 = pd.read_csv('traditional.csv')

percentage_columns = ['FG%', '3P%', 'FT%']
for col in percentage_columns:
    if pd.api.types.is_numeric_dtype(df2[col]):
        continue
    df2[col] = pd.to_numeric(df2[col].str.rstrip('%'), errors='coerce')


df2['PER'] = (df2['PTS'] + df2['REB'] + df2['AST'] + df2['STL'] + df2['BLK']
              - (df2['FGA'] - df2['FGM']) - (df2['FTA'] - df2['FTM']) - df2['TOV']) / df2['MIN']


top_scorers = df2.nlargest(5, 'PTS')
top_rebounders = df2.nlargest(5, 'REB')
top_playmakers = df2.nlargest(5, 'AST')
top_steal_players = df2.nlargest(5, 'STL')
top_block_players = df2.nlargest(5, 'BLK')


shooting_efficiency_metrics = ['FG%', '3P%', 'FT%']
df2[shooting_efficiency_metrics].mean().plot(kind='bar', figsize=(10, 6), color='skyblue')
plt.title('Average Shooting Efficiency Metrics for Players')
plt.xlabel('Shooting Efficiency Metrics')
plt.ylabel('Average Value')
plt.show()


plt.figure(figsize=(10, 6))
sns.scatterplot(x='MIN', y='PER', data=df2, hue='PTS', size='PTS', palette='viridis', sizes=(20, 200))
plt.title('Relationship between Player\'s Performance (PER) and Playing Time (MIN)')
plt.xlabel('Playing Time (MIN)')
plt.ylabel('Player Efficiency Rating (PER)')
plt.legend(title='Points (PTS)')
plt.show()


top_plus_minus_players = df2.nlargest(5, '+/-')


print("Top Scorers:")
print(top_scorers[['player', 'PTS']])
print("\nTop Rebounders:")
print(top_rebounders[['player', 'REB']])
print("\nTop Playmakers:")
print(top_playmakers[['player', 'AST']])
print("\nTop Steal Players:")
print(top_steal_players[['player', 'STL']])
print("\nTop Block Players:")
print(top_block_players[['player', 'BLK']])
print("\nPlayers with High Impact (+/-):")
print(top_plus_minus_players[['player', '+/-']])
