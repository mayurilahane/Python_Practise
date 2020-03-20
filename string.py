#string title
s = "MAYURI LAHane"
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())

m = "hello i am ok"
print(m.split(" "))

#check whether the string is pallendrome or not
a = input("enter string : ")
z = a[::-1]
if a == z:
    print("pallendrome")
else:
    print("no pallendrome")