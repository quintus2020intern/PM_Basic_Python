# r=lambda a:a+10
# print(r(10))
# q=lambda a,b:a*b
# print(q(20,7))


subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print( "Original list of tuples:" )
print( subject_marks )
subject_marks.sort( key=lambda x: x[1] )
print( "\nSorting the List of Tuples:" )
print( subject_marks )
