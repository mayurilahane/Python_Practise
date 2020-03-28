#Taking ip from keyboard
number = int(input("enter the no"))
print(number)

#tuple
tup = ("mayuri", "python")
name, lang = tup
print(name)
print(lang)

#fstring-formatting
print(f"{name} loves {lang}")

#datetime related cases
import datetime
d = datetime.date(2020, 1, 3)
print(f"{d} on {d:%A}  is my birthday")

#dict hack
dict1 = {
    1: "python",
    True: False,
    3: "india"
    }
print(dict1)

#dict hack
dict2 = {0: "mayuri",
         False: True
         }
print("dict2 = ", dict2)

#list eg1
list1 = (1, 2, 3)
list2 = (4, 5, 6)
list3 = list1+list2
print(list3)

#list ed2
var1 = "ganesh"
var2 = "ramesh"
print(f"{var1} and {var2} are good friends")

#print assings to random varibale
d = print
d("hello")

#global variable cant be updated in local function
x=10
def age():
    x=5
    print(x)
age()
print(x)

#global variable got updated in local using "global" keyword
x=10
def age():
    global x
    x=5
    print(x+1)
age()
print(x)

#new operators:
"""Division(/)
Divides the value on the left by the one on the right. Notice that division results in a floating-point value.
>>> 3/4
Output: 0.75

Exponentiation(**)
Raises the first number to the power of the second.
>>> 3**4
Output: 81

Floor Division(//)
Divides and returns the integer value of the quotient. It dumps the digits after the decimal.
>>> 4//3
Output: 1
>>> 10//3
Output: 3

Modulus(%)
Divides and returns the value of the remainder.
>>> 3%4
Output: 3
>>> 4%3
Output: 1
>>>10.5%3
Output: 1.5 """"

