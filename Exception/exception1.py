# try:
#      raise Exception('spam', 'eggs')
# except Exception as inst:
#      print(type(inst))    # the exception instance
#      print(inst.args)     # arguments stored in .args
#      print(inst)          # __str__ allows args to be printed directly,
#                           # but may be overridden in exception subclasses
#      x, y = inst.args     # unpack args
#      print('x =', x)
#      print('y =', y)


# def this_fails():
#      x = 1/0
# try:
#      this_fails()
# except ZeroDivisionError as err:
#      print('Handling run-time error:', err)

# class Error(Exception):
#     """Base class for exceptions in this module."""
#     pass
#
# class InputError(Error):
#     """Exception raised for errors in the input.

# Attributes:
#         expression -- input expression in which the error occurred
#         message -- explanation of the error
#     """
#
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.message = message
#
# class TransitionError(Error):
#     """Raised when an operation attempts a state transition that's not
#     allowed.
#
#     Attributes:
#         previous -- state at beginning of transition
#         next -- attempted new state
#         message -- explanation of why the specific transition is not allowed
#     """
#
#     def __init__(self, previous, next, message):
#         self.previous = previous
#         self.next = next
#         self.message = message

#
# def bool_return():
#          try:
#              return True
#          finally:
#              return False
# bool_return()
#
# def divide(x, y):
#      try:
#         result = x / y
#      except ZeroDivisionError:
#          print("division by zero!")
#      else:
#         print("result is", result)
#      finally:
#         print("executing finally clause")
# divide(2,0)

import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print( "The entry is", entry )
        r = 1 / int( entry )
        break
    except:
        print( "Oops!", sys.exc_info()[0], "occured." )  # sys.exc_info()[0] (defines which type of exception is raise)
        print( "Next entry." )
        print()
print( "The reciprocal of", entry, "is", r )
