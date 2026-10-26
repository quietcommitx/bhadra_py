# Args: tuple of positional arguments
# multiple positional arguments are accepted by a parameter 
# an args is defined by '*'

def user(name,*args):
   print(args)
   for i in args:
      print(i)

n = "Ram"
c = "9+874563210"
a = "ADDRESS"

# user(n,c,a)
# user(n,c,a,15)
# user(n,c,a,15,"ram@gmail.com")

# Kwargs: dictioinary of keyword arguments
# multiple keyword arguments are accepted by a parameter 
# kwargs is defined by '**'
def user(**kwargs):
   print(kwargs)
   print(kwargs.items())
   # print(kwargs.keys())
   # print(kwargs.values())
   for i,j in kwargs.items():
      print(f"{i}:{j}")

# n = "Ram"
# c = "9+874563210"
# a = "ADDRESS"

# user(name = n,contact = c,address = a)
# user(name = n, contact = c,address = a,age = 15)
# user(name = n, contact = c,address = a,age = 15,email = "ram@gmail.com")

# return: a data is returned to the line of function call, also ends the function
# requirement: add 2 numbers using sum function then multiple it by 3
def multiple(d):
   e = d * 3
   return e

def sum(a,b):     # function define
   c = a + b
   # print((a + b) * 3)
   # print(c * 3)
   # return c
   f = multiple(c)
   return f


a = sum(10,5) 
# print(a * 3)
print(a)

# a = "hello"
# b = a.capitalize()