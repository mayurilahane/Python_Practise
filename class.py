# #to delete the object:
# x = "hello"
# print(x) #before deleting object
# del x
# print(x) #after deleting object

class People(object):
    def __init__(self, name):
        self.name = name
    def details(self):
        return self.name

class Student(People):
    def __init__(self, name, marks):
        People.__init__(self, name)
        self.marks = marks
    def details(self):
        return (self.name, self.marks)

class Teacher(People):
    def __init__(self, name, year):
        People.__init__(self, name)
        self.year = year
    def details(self):
        return (self.name, self.year)

pep = People("mayuri")
print(pep.details())

stud = Student("rujuta", 100)
print(stud.details())

tech = Teacher("demo", 2005)
print(tech.details())

"""Default Module"""
import os
import requests

#printing objects address
class computer:
    pass
c1 = computer
print(id(c1))#to get the menory address of that object from heap memory
#heap memory stores all the objects creted and id gives its address

num = [1,2,3,4,5]
it = iter(num)
print(it) #will print object
print(next(it)) #will print next value
print(it.__next__())  #other way to print next value
print(it.__next__()) #and so on....