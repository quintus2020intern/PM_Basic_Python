import pandas as pd

df = pd.read_csv( 'Book1.csv' )
# print(df['Total'][df['Region']=='East'],'\n')
print( df[['Region', 'Total']][df.Region == 'East'] )

# print(df[['Total','Region']]=='East')
# print(df['Total'].max())
# print(type(df))
# print(df.head())
# print(df.tail())


# for item in df1:
#     if 'East' in 'Region':
#         csvfile = open( 'pandas.csv', 'w' )
#         csv_writer=csv.writer(csvfile,delimiter='\t')

# import csv
#
# filename = "Book1.csv"
#
# fields = []
# rows = []
#
# csvfile = open(filename, 'r', errors='ignore')
# csv_reader = csv.reader(csvfile)
#
#
# for row in csv_reader:
#
#       fields.append(row[1])
#
#       rows.append(row[6])
# print(fields)
# print(rows)
# csvfile1=open('pandas.csv','w')
# csv_writer=csv.writer(csvfile1,delimiter='\t')
# for line in row:
#     if 'East' in fields:
#         print(rows[])
