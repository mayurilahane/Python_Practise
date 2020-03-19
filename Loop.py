#The way to test Truth values is like

if x:
    pass

#* pattern problems
row = int(input("Enter the number of rows: "))
n = row
while n >= 0:
    x =  "*" * n
    print(x)
    n -= 1

#* patteern
n = int(input("Enter the number of rows: "))
i = 1
while i <= n:
    print("*" * i)
    i += 1
