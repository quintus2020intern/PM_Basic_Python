class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print( "hi", self.name )
        print( "your mark is", self.marks )

    def grade(self):
        if self.marks >= 60 or self.marks <= 95:
            print( "1st grade" )
        elif self.marks >= 50:
            print( "2nd grade" )
        elif self.marks >= 30:
            print( "3rd grade" )
        else:
            print( "you are fail" )


n = int( input( "Enter Number of students:" ) )
for i in range( n ):
    name = input( "Enter your name:" )
    marks = int( input( "Enter your marks:" ) )
    s = Student( name, marks )
    s.display()
    s.grade()
