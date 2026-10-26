# Function: task specific, reusable

# syntax
# def function_name():        function define
#    statements

# function_name()          this is function call
a = 10   # global variable: can be called and used anywhere in the program
def sum():     # function define
   a = 15   # local variable: can only be called and used inside this function
   b = 5
   print(a + b)


sum()    # function call

# Parameter: variable defined inside the paranthesis in function defination
# Arguments: variable/value inside the paranthesis in function call
# argument is passed to the parameter

def sum(x,y,z):       # x is a parameter
   print(x + y + z)

# sum(10, 15 , 20)

# types of arguments
# Positional Argument: data is assigned sequential i.e. 1st para = 1st arg, 2nd para = 2nd arg, ....
def user(name, contact, add):
   print(f"""Name: {name}
Contact: {contact}
Address:{add}""")

n = "Ram"
c = "9+874563210"
a = "ADDRESS"
user(n,c,a)
user(c,n,a)

# Keyword Argument: direct data is assigned to parameter during function call
def user(name, contact, add):
   print(f"""Name: {name}
Contact: {contact}
Address:{add}""")

n = "Ram"
c = "9+874563210"
a = "ADDRESS"
# user(name=n,contact=c,add =a)
user(contact = c,name = n, add = a)

# Default argument:
n = "Ram"
c = "9+874563210"
a = "ADDRESS"
def user(name=n, contact="default contant", add="default address"):
   print(f"""Name: {name}
Contact: {contact}
Address:{add}""")


user(name="SITA",contact=c,add =a)
user()

# implement function
# implement while loop
# Calculator
# get 2 numbers from user
# get an operator from user(+,-,*,/)
# if operator is eqaual to +, then print out the sum of 2 number
# if operator is -, then print out the subracttion of 2 number
# if operator is *, then print out the multiplication of 2 number
# if operator is /, then print out the division of 2 number
# ask to rerun the calculator, if yes rerun the calculator, if no end the loop

# create a function that print out the introduction of the user
# get name, address and other details from user that can be used for introduction


# args, kwargs, return