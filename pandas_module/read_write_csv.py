import pandas as pd

# df=pd.read_csv("Book1.csv",skiprows=1,names=["g1","g2","g3","g4","g5","g6","g7"])#(header=1)
f = pd.read_csv( "Book1.csv", nrows=3 )
f1 = f.to_csv( "new.csv", columns=['Region', 'units'] )
print( f )
print( f1 )
