#function basic
def sum(a, b):
    return a+b
print(sum(10, 40))

#example of default argument
def test(a , b=-99):
    if a > b:
        return True
    else:
        return False

print(test(2, 5))
print(10)

#list with function
def f(a, data=[]):
    data.append(a)
    return data
print(f(1))
print(f(2))
print(f(3))

#keyword arguments
"""keyword arg will act like positional argument when 
 you will give values it will take in sequence"""

#higher order function - take function as ip and return function as output
import datetime
def high(func, value):
    return func(value)
list = high(dir, datetime)
print(list[-8::])
print(list)

