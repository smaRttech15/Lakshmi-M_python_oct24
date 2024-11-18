import pandas as pd

players = {'Player':['sachin', 'kumble', 'srinath', 'dravid', 'sehwag', 'bumra', 'agarkar', 'ganguly'], 'Team' : ['mi', 'csk', 'kkr', 'rcb', 'mi', 'csk', 'dd', 'kkr'], 'Price' : [10, 2, 2, 3, 5, 4, 6, 8], 'Type' : ['batsman', 'bowler', 'bowler', 'batsman', 'batsman', 'bowler', 'bowler', 'batsman'], 'Run' : [1000, 150, 125, 950, 900, 90, 450, 885], 'Wicket' : [20, 85, 83, 12, 35, 80, 90, 10] }

df = pd.DataFrame(players)

print(df[df['Price'] == df['Price'].min()])

print(df.groupby('Team').Player.count())

print(df[df['Price'] == df['Price'].max()])

print(df.groupby(['Team']).Run.sum())

print(df.groupby(['Team']).Run.mean())

print(df.sort_values(by='Run'))

print(df.sort_values(by='Price', ascending=0))

print(df.sort_values(by='Wicket', ascending=0))

print(df.loc[df.groupby('Team')['Price'].idxmax(), ['Team', 'Player', 'Price']])