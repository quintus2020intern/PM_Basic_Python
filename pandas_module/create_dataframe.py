import pandas as pd

'''
Read from csv
'''
df = pd.read_csv( "Book1.csv" )
print( df )
'''
Read from Excel
'''
df = pd.read_excel( 'MOCK_DATA(1).xlsx' )
data = pd.read_excel( "Book1.xlsx" )
print( data )
'''
Read from python dictionary
'''
weather_data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017'],
    'temp': [32, 54, 45, 67],
    'windspeed': [6, 5, 7, 3],
    'event': ['rain', 'sunny', 'snow', 'winter']
}
df = pd.DataFrame( weather_data )
print( df )
'''
Read from list of tuple
'''
weather_data = [
    ('1/1/2017', 23, 6, 'Rain'),
    ('2/1/2017', 24, 8, 'sunny'), ('3/1/2017', 25, 9, 'winter')

]
df = pd.DataFrame( weather_data, columns=["day", "temp", "speed", "event"] )
print( df )

'''
Read from list of dictionary
'''
weather_data = [
    {'day': '1/1/2017', 'temp': 23, 'speed': 6, 'event': 'Rain'},
    {'day': '2/1/2017', 'temp': 24, 'speed': 5, 'event': 'summer'},
    {'day': '3/1/2017', 'temp': 25, 'speed': 7, 'event': 'winter'},
]

df = pd.DataFrame( weather_data )
df1 = df.fillna( method="bfill" )
# df.dropna()
print( df1 )

