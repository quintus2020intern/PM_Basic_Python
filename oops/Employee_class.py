class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print( "Employee no is :", self.eno )
        print( "Employee name is:", self.ename )
        print( "Employee salary is :", self.esal )


class Test:
    def modify(emp):
        emp.esal = emp.esal + 10000
        emp.display()


e = Employee( 1, "punu", 50000 )
Test.modify( e )
