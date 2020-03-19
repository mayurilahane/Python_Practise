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