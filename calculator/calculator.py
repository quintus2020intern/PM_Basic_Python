from calc import Calc

cal = Calc()
print("welcome to my calculator")
print("Here the list of choice : ")
print('-' * 20)
print ("1: Addition    \t\t\t   12: sine in degrees")
print ("2: Substraction    \t\t\t   13: cosine in degrees")
print ("3: Multiplication    \t\t\t   14: Tan in degrees")
print ("4: Division    \t\t\t   15: cosec in degrees")
print ("5: sine in radinas    \t\t\t   16: sec in degrees")
print ("6: cosine in radians    \t\t\t   17: cot in degrees")
print ("7: tan in radians    \t\t\t   18: Natural Log")
print ("8: cosec in radians    \t\t\t   19: Base 10 log")
print ("9: sec in radians    \t\t\t   20: Log base 'x' ")
print ("10: cot    \t\t\t   21: Square root")
print ("11: pi   \t\t\t   22: power of")
print('-' * 20)
choice = ""
while True:
    try:
        choice = int( input( "Enter your Choice: " ) )
    except:
        print("Enter the valid choice:  ")
    if choice == 1:
        n1 = float( input( "Enter the 1st number to add :" ) )
        n2 = float( input( "Enter the 2nd number to add :" ) )
        cal.add( n1, n2 )
    if choice == 2:
        n1 = float( input( "Enter the 1st number to sub :" ) )
        n2 = float( input( "Enter the 2nd number to sub :" ) )
        cal.sub( n1, n2 )
    if choice == 3:
        n1 = float( input( "Enter the 1st number to mul :" ) )
        n2 = float( input( "Enter the 2nd number to mul :" ) )
        cal.mul( n1, n2 )
    if choice == 4:
        n1 = float( input( "Enter the 1st number to div :" ) )
        n2 = float( input( "Enter the 2nd number to div  :" ) )
        cal.div( n1, n2 )
    if choice == 5:
        n = float( input( "Enter a number to find its sine in radians:" ) )
        cal.sinrad( n )
    if choice == 6:
        n = float( input( "Enter a number to find its cos in radians:" ) )
        cal.cosrad( n )
    if choice == 7:
        n = float( input( "Enter a number to find its tan in radians:" ) )
        cal.tanrad( n )
    if choice == 8:
        n = float( input( "Enter a number to find its cosec in radians:" ) )
        cal.sinerad( n )
    if choice == 9:
        n = float( input( "Enter a number to find its sec in radians:" ) )
        cal.secrad( n )
    if choice == 10:
        n = float( input( "Enter a number to find its cot in radians:" ) )
        cal.sinrad( n )
    if choice == 11:

        cal.pie()
    elif choice == 12:
        n = float( input( "Enter a number to find its sine in degrees:" ) )
        cal.sindeg( n )
    elif choice == 13:
        n = float( input( "Enter a number to find its cossine in degrees:" ) )
        cal.cosdeg( n )
    elif choice == 14:
        n = float( input( "Enter a number to find its tan in degrees:" ) )
        cal.tandeg( n )
    elif choice == 15:
        n = float( input( "Enter a number to find its cosec in degrees:" ) )
        cal.cosecdeg( n )
    elif choice == 16:
        n = float( input( "Enter a number to find its sec in degrees:" ) )
        cal.secdeg( n )
    elif choice == 17:
        n = float( input( "Enter a number to find its cot in degrees:" ) )
        cal.cotdeg( n )
    elif choice == 18:
        n = float( input( "Enter a number to find its natural logs:" ) )
        cal.ln( n )
    elif choice == 19:
        n = float( input( "Enter a number to find its Base 10 logs:" ) )
        cal.logten( n )

    elif choice == 20:
        n1 = float( input( "Enter a base  number:" ) )
        n2 = float( input( "Enter a number to find it's log to the:" ) )
        cal.logbasex( n1, n2 )
    elif choice == 21:
        n = float( input( "Enter a number to find it's square: " ) )
        cal.squareroot( n )
    elif choice == 22:
        n1 = float( input( "Enter a base  number:" ) )
        n2 = float( input( "Enter it's power:" ) )
        cal.powerof( n1, n2 )
