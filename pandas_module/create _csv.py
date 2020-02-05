import pandas as pd

weather_data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017'],
    'temp': [32, 54, 45, 67],
    'windspeed': [6, 5, 7, 3],
    'event': ['rain', 'sunny', 'snow', 'winter']
}
df = pd.DataFrame( weather_data )
print( df )

# print( df )
# print( df['day'][df['event']] == 'Rain' )
# print(df.head(2))
# print(df[2:5])
# print(df.columns)
# print(df.day)
# print(type(df['day']))
# print(df[['event','day']])
# print("the maximum temperature is",df['temp'].max())
# print("the minimum temperature is",df['temp'].min())
# print("the mean tempe is",df['temp'].mean())
# print(df.describe())
# print(df[df.temp >= 30])
# print(df[df.temp==df['temp'].max()])
# df.set_index('day',inplace=True)#modify the orginal data

# print(df.loc['1/1/2017'])
# df.reset_index(inplace=True)
# print(df)
