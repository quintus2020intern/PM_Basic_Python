# class Test:
#     count = 0  # static variable
#
#     def __init__(self):
#         Test.count = Test.count + 1
#
#     @classmethod
#     def getNoOfObject(cls):
#         print("no of object", cls.count)
#
#
# t1 = Test()
# t1.getNoOfObject()


# class Test:
#     @classmethod
#     def df(cls):
#         print(id(cls))
#
# print(id(Test))
# Test.df()


class Test:

    def __init__(self):
        print( id( self ) )


t1 = Test()
print( id( t1 ) )
