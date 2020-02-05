import pandas as pd

# df=pd.read_csv("Book1.csv",skiprows=1,names=["g1","g2","g3","g4","g5","g6","g7"])#(header=1)
# f=pd.read_excel("Book1.xlsx",'Sheet1')
# f1=f.to_csv("new1.csv")
# print(f)
# print(f1)
weather_data = pd.DataFrame( {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017'],
    'temp': [32, 54, 45, 67],
    'windspeed': [6, 5, 7, 3],
    'event': ['rain', 'sunny', 'snow', 'winter']
} )
weather = pd.DataFrame( {
    'day': ['6/1/2017', '4/2/2017', '8/3/2017', '9/4/2017'],
    'temp': [32, 54, 45, 67],
    'wind': [6, 5, 7, 3],
    'event': ['rain', 'sunny', 'snow', 'winter']
} )
# ExcelWriter class,writer object
with pd.ExcelWriter( 'Book2.xlsx' )as writer:
    weather_data.to_excel( writer, sheet_name="weather" )
    weather.to_excel( writer )
