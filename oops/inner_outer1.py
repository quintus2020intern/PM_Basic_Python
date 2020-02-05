class Person:
    def __init__(self):
        self.name = "ppm"
        self.dob = self.DOB()

    def display(self):
        print( "name:", self.name )
        self.dob.display()

    class DOB:
        def __init__(self):
            self.dd = 9
            self.mm = 5
            self.yyyy = 2020

        def display(self):
            print( 'DOB={}/{}/{}'.format( self.dd, self.mm, self.yyyy ) )


p = Person()
p.display()
