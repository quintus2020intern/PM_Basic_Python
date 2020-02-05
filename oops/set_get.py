class Student:
    def set(self, name, marks):
        self.name = name
        self.marks = marks

    def get(self):
        return self.name

    def get1(self):
        return self.marks
    # def grade(self):
    #         if self.marks>=60 or self.marks <= 95:
    #             print("1st grade")
    #         elif self.marks>=50:
    #             print("2nd grade")
    #         elif self.marks>=30:
    #             print("3rd grade")
    #         else:
    #             print("you are fail")


n = int( input( "Enter Number of students:" ) )
for i in range( n ):
    name = input( "Enter your name:" )
    marks = int( input( "Enter your marks:" ) )
    s = Student()
    s.set( name, marks )
    # s.set(marks)
    print( "hi", s.get() )
    print( "your mark is", s.get1() )
