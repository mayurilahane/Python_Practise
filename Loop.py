#The way to test Truth values is like

if x:
    pass

#* pattern problems
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x =  "*" * n
    print(x)
    n += 1

# * pattern
n = int(input("Enter the number of rows: "))
i = 1
while i <= n:
    print("*" * i)
    i += 1

#using _ in loop because dont need to use itrative varibale
for _ in range(3):
    print("hello")

#list in for
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in a[::2]:
    print(x)

#range with list function
list1 = list(range(1, 5))
print(list1)

list2 = list(range(1, 15, 3)) #start = 1,stop = 15,waitof = 3
print(list2)

#while loop with continue and break
while True:
    n = int(input("enter integer: "))
    if n < 0:
        continue # this will take the execution back to the starting of the loop
    elif n == 0:
        break
    print("square", n ** 2)
print("bye")

#list comprehension in same line:
a = [1, 2, 3]
result1 = [x ** 2 for x in a]
print(result1)

result2 = [x - 1 for x in [x ** 2 for x in a]]
print(result2)


#tuple
a = (123)
print(type(a))

a = (123, ) #Look at the trailing comma
print(type(a))

#set default values in dict
data = {}
data.setdefault('names', []).append('Ruby')
print(data)

data.setdefault('names', []).append('Python')
print(data)
{'names': ['Ruby', 'python']}

#use of enumerate(counter)
l1 = ["eat", "sleep", "repeat"]
l2 = "geek"

obj1 = enumerate(l1) #creating enumerate objects
obj2 = enumerate(l2) # creating enumerate objects

print(list(enumerate(l1)))
print(list(enumerate(l2, 2))) # changing start index to 2 from 0
