import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('team_traditional.csv')

percentage_columns = ['FG%', '3P%', 'FT%']
for col in percentage_columns:
    if pd.api.types.is_numeric_dtype(df1[col]):
        continue
    df1[col] = pd.to_numeric(df1[col].str.rstrip('%'), errors='coerce')

df1['TotalPoints'] = df1['PTS']

df1['FG_Percentage'] = df1['FGM'] / df1['FGA'] * 100
df1['3P_Percentage'] = df1['3PM'] / df1['3PA'] * 100
df1['FT_Percentage'] = df1['FTM'] / df1['FTA'] * 100

# Convert 'season' column to datetime format
df1['season'] = pd.to_datetime(df1['season'])

team_performance_metrics = ['REB', 'AST', 'STL', 'BLK', 'TOV']


correlation_matrix = df1[['TotalPoints', 'FG_Percentage', '3P_Percentage', 'FT_Percentage'] + team_performance_metrics].corr()
seasonal_trends = df1.groupby('season').mean()

seasonal_trends[['TotalPoints', 'FG_Percentage', '3P_Percentage', 'FT_Percentage']].plot(kind='line', marker='o', figsize=(12, 6))
plt.title('Seasonal Trends in Team-level Statistics')
plt.xlabel('Season')
plt.ylabel('Average Value')
plt.legend(loc='upper left')
plt.show()
