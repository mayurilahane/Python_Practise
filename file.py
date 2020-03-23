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
    print(x, end='')

#function for whole operation of file
name = input("Enter the file name: ")
fobj = open(name,'w')
print(fobj.read())
fobj.close()

#using "with" statment it will directly close your file
with open('string.py') as fobj:
    for line in fobj:
        print (line)

#write somthing in file
fobj = open("filename",'w') #to ope the file in writeable mode
fobj.write("hello trying to test writing operations in string\n")
fobj.close()

"""refer this example - https://pymbook.readthedocs.io/en/latest/file.html"""
#count-spaces-tabs-and-new-lines-in-a-file
