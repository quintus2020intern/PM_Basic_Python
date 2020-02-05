import csv
import operator

filename = "Book1.csv"

fields = []
rows = []

csvfile = open( filename, 'r', errors='ignore' )
csvreader = csv.reader( csvfile )
sort = sorted( csvreader, key=operator.itemgetter( 1 ) )
for row in sort:
    print( row )

'''
    # get total number of rows
print("Total no. of rows: %d" % (csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    # parsing each column of a row
    for col in row:
        print("%10s" % col),
    print('\n')
'''
