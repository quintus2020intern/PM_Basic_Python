# # define Python user-defined exceptions
# class Error(Exception):
#    """Base class for other exceptions"""
#    pass
# class ValueTooSmallError(Error):
#    """Raised when the input value is too small"""
#    pass
# class ValueTooLargeError(Error):
#    """Raised when the input value is too large"""
#    pass
# # our main program
# # user guesses a number until he/she gets it right
# # you need to guess this number
# number = 10
# while True:
#    try:
#        i_num = int(input("Enter a number: "))
#        if i_num < number:
#            raise ValueTooSmallError
#        elif i_num > number:
#            raise ValueTooLargeError
#        break
#    except ValueTooSmallError:
#        print("This value is too small, try again!")
#        print()
#    except ValueTooLargeError:
#        print("This value is too large, try again!")
#        print()
# print("Congratulations! You guessed it correctly.")


# language = ['P', 'y', 't', 'h', 'o', 'n']
# print(language[:-4])
#
# print((1, 2) + (3, 4))
#
#
# squares = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(squares.pop(4))
# print(squares)
#
# if None:
#     print("hello")
# i = sum = 0
# while i <= 4:
#     sum += i
#     i = i+1
# print(sum)
#
#
# while 4 == 4:
#     print('4')


# def outerFunction():
#     global a
#     a = 20
#     def innerFunction():
#         global a
#         a = 30
#         print('a =', a)
# a = 10
# outerFunction()
# print('a =', a)


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __sub__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point( x, y )


p1 = Point( 3, 4 )
p2 = Point( 1, 2 )
result = p1 - p2
print( result.x, result.y )
