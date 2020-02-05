# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print ("An exception")
#     raise  # To determine whether the exception was raised or not


# def example():
#     try:
#         int('N/A')
#     except ValueError as e:
#         raise RuntimeError('A parsing error occurred')
#
# example()


# def example3():
#     try:
#         int('N / A')
#     except ValueError:
#         raise RuntimeError('A parsing error occurred') from None
# example3()


def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32


print( KelvinToFahrenheit( 273 ) )
print( int( KelvinToFahrenheit( 505.78 ) ) )
print( KelvinToFahrenheit( -5 ) )
