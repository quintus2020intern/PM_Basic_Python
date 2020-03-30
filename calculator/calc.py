import math


class Calc():
    def add(self, num1, num2):
        answer = num1 + num2
        print("sum= ", answer)

    def sub(self, num1, num2):
        answer = num1 - num2
        print("sub= ", answer)

    def mul(self, num1, num2):
        answer = num1 * num2
        print("mul= ", answer)

    def div(self, num1, num2):
        answer = num1 / num2
        print("div= ", answer)

    def mod(self, num1, num2):
        answer = num1 % num2
        print("mod= ", answer)

    def sinrad(self, num):  # return the value of the sine of x radians
        answer = math.sin( num )
        print('sine (%f) =%f' % (num, answer))

    def cosrad(self, num):  # return the value of the cos of x radians
        answer = math.cos( num )
        print('cosine (%f) =%f' % (num, answer))

    def tanrad(self, num):  # return the value of the tan of x radians
        answer = math.tan( num )
        print('Tan(%f) =%f' % (num, answer))

    def cosecrad(self, num):  # return the value of the cosec of x radians
        answer = 1 / (math.sin( num ))
        print('sine(%f) =%f' % (num, answer))

    def secrad(self, num):  # return the value of the sec of x radians
        answer = 1 / (math.cos( num ))
        print('Sec(%f) =%f' % (num, answer))

    def cotrad(self, num):  # return the value of the sine of x radians
        answer = 1 / (math.tan( num ))
        print('Cot(%f) =%f' % (num, answer))

    def sindeg(self, num):
        answer = math.sin( math.radians( num ) )
        print('sin(%f) in degree= %f' % (num, answer))

    def cosdeg(self, num):
        answer = math.cos( math.radians( num ) )
        print('cos(%f) in degree= %f' % (num, answer))

    def tandeg(self, num):
        answer = math.tan( math.radians( num ) )
        print('tan(%f) in degree= %f' % (num, answer))

    def cosecdeg(self, num):
        answer = 1 / (math.sin( math.radians( num ) ))
        print('cosec(%f) in degree= %f' % (num, answer))

    def secdeg(self, num):
        answer = 1 / (math.cos( math.radians( num ) ))
        print('sec(%f) in degree= %f' % (num, answer))

    def cotdeg(self, num):
        answer = 1 / (math.tan( math.radians( num ) ))
        print('cot(%f) in degree= %f' % (num, answer))

    def ln(self, num):
        answer = math.log( num )
        print('ln(%f)=%f' % (num, answer))

    def logten(self, num):
        answer = math.log10( num )
        print('Log10(%f)=%f' % (num, answer))

    def logbasex(self, num, x):
        answer = math.log( num, x )
        print('log base(%f)(%f)=%f' % (x, num, answer))

    def squareroot(self, num):
        answer = math.sqrt( num )
        print('square root(%f)=%f' % (num, answer))

    def pie(self):
        print('pi=', math.pi)

    def powerof(self, num, raiseby):
        answer = math.pow( num, raiseby )
        print('%f ^ (%f) = %f' % (num, raiseby, answer))
# cal=calc()
# print("welcome to my calculator")
