"""exception are of types -
NameError
TypeError
KeyboardIntrurrpt,etc"""

"""we can use try and except to handle this exception"""
try:
    print(abc)
except: #only except can handle any type or exception
    print("no value defined for abc")

#finally:
"""we can use finally block to execute those statments which needs to execute 
at any condition"""

"""finally:
print("every file needs to close")
fobj.close()"""

#only this will give name error to handle this:
try:
    x = input(int("enter any no."))
    print(abc)
except Exception as e: #you can specify proper name of exception
    print("no value defined")
    print(e)
    print(e)

#user defined exceptions:
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print(e.args)
