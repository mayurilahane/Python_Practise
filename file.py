#to open a file
# obj = open(path or name of file)
# eg:
fobj = open("/home/mlahane/python_eg/Python_Practise/Loop.py")
print(fobj)

"""If you call read() again it will return empty
string as it already read the whole file.
so first close it then read it again or take other file as input """

fobj.read() #will read the file
fobj.readline() #will read one line of file
fobj.readlines()#read multiple lines

#reading file using for loop
fobj = open("/home/mlahane/python_eg/Python_Practise/Loop.py")
for x in fobj:
    print(x, end='') #or just x also will work

#function for whole operation of file
name = input("Enter the file name: ")
fobj = open(name,'w')
print(fobj.read())
fobj.close()

#for creation of new file on command line
obj = open("/home/mlahane/python_eg/Python_Practise/y.py", 'a+/w+/r+') #+ is imp for creation

#using "with" statment it will directly close your file
with open('string.py') as fobj:
    for line in fobj:
        print (line)

#i just know about "with" is ,its only uses to close the file

#write something in file
fobj = open("filename",'w'/'a') #to ope the file in writeable mode
fobj.write("hello trying to test writing operations in string\n")
fobj.close()

"""refer this example - https://pymbook.readthedocs.io/en/latest/file.html"""
#count-spaces-tabs-and-new-lines-in-a-file

#WAP to get how much time(measuring time in microsec)is required to create 10,100,1000 files with writing unique content
import datetime
a = datetime.datetime.now().time().microsecond
for i in range(100):
    obj = open(f"/home/mlahane/python_eg/Python_Practise/{i}hello.py", "w+")#tried with other names(x,y)
    obj.write(f"{i} hello am in")
b = datetime.datetime.now().time().microsecond
print(f"time before creating files{a}, time after creation of files{b}, exact time of file creation{a-b}")

#deleting all created files from above program
import os
list = ["x", "y", "hello"]
for i in range(100):
    for j in list:
        try:
            os.remove(f"/home/mlahane/python_eg/Python_Practise/{i}{j}.py")
        except Exception as e:
            print(e)