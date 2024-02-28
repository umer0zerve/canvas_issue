def create_horizontal_bar_chart(data, x_label, y_label, title):
    fig = px.bar(data, x=y_label, y='player', orientation='h', text=y_label,
                 labels={y_label: x_label, 'player': 'Player'},
                 title=title, width=800, height=400)
    fig.show()


df2 = pd.read_csv('traditional.csv')
top_scorers = df2.nlargest(5, 'PTS')
top_rebounders = df2.nlargest(5, 'REB')
top_playmakers = df2.nlargest(5, 'AST')
top_steal_players = df2.nlargest(5, 'STL')
top_block_players = df2.nlargest(5, 'BLK')


create_horizontal_bar_chart(top_scorers, 'Points', 'PTS_player', 'Top Scorers')
create_horizontal_bar_chart(top_fg_percentage, 'Field Goal Percentage', 'FG%_player', 'Top Field Goal Percentage')
create_horizontal_bar_chart(top_3p_percentage, 'Three-Point Percentage', '3P%_player', 'Top Three-Point Percentage')
create_horizontal_bar_chart(top_ft_percentage, 'Free Throw Percentage', 'FT%_player', 'Top Free Throw Percentage')
create_horizontal_bar_chart(top_rebounders, 'Rebounds', 'REB_player', 'Top Rebounders')
create_horizontal_bar_chart(top_assist_producers, 'Assists', 'AST_player', 'Top Assist Producers')
create_horizontal_bar_chart(top_steal_producers, 'Steals', 'STL_player', 'Top Steal Producers')
create_horizontal_bar_chart(top_block_producers, 'Blocks', 'BLK_player', 'Top Block Producers')
create_horizontal_bar_chart(top_efficiency, 'Efficiency', 'Efficiency', 'Top Efficient Players')
