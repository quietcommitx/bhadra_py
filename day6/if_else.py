# if else
# if condition True, if block is executed
# if the condition of elif is True, elid block is executed
# if can be followed by multiple elif blocks
# if all the upper conditions are False, then else block is executed

# Syntax:
# if condition:
#    statment1
#    statment2
# elif statement:
#     statement1
# elif condition:
#     statement
# else:
#     statement

a = 10
b = 10
# requirement: 
# if a is greater than b then print out "A is greater than B"
# if a is equal to  b then print out "A is equal to B."
# if a is less than b then print out "A is less than B"

if a > b:   # if condition True, action execute
   print("A is greater than B.")
elif a == b:
   print("A is equal to B.")
else:
   print("A is less than B.")


# todo:
# Calculator
# get 2 numbers from user
# get an operator from user(+,-,*,/)
# if operator is eqaual to +, then print out the sum of 2 number
# if operator is -, then print out the subracttion of 2 number
# if operator is *, then print out the multiplication of 2 number
# if operator is /, then print out the division of 2 number

# Mark Evaluator
# get mark from user
# if the entered marks is greater than 90 and less than 100, print a statement ("Excelent")
# if the entered marks is greater than 80 and less than 90, print a statement
# if the entered marks is greater than 70 and less than 80, print a statement
# if the entered marks is greater than 60 and less than 70, print a statement
# if the entered marks is greater than 50 and less than 60, print a statement
# if the entered marks is greater than 40 and less than 50, print a statement
# if the entered marks less than 40, print a statement
# if the mark is greater than 100 or less than 0 then print out a statement("invalid data")

# create a list of username
# get the username from user
# if the username exist print a statment
# if user doesnot exist print a statement


# nested statements

# Syntax:
# if condition:
#    statment1
   # if condition:
   #    statment1
   # elif statement:
   #     statement1
   # elif condition:
   #     statement
   # else:
   #     statement
# elif statement:
#     statement1
# elif condition:
#     statement
# else:
#     statement
#     # if condition:
      #    statment1
      # elif statement:
      #     statement1
      # elif condition:
      #     statement
      # else:
      #     statement

a = 100
b = 10
c = 15

if a > b:   # if condition True, action execute
   print("A is greater than B.")
   if a > c:   # if condition True, action execute
      print("A is greater than C. nested")
   elif a == c:
      print("A is equal to C. nested")
   else:
      print("A is less than C. nested")
elif a == b:
   print("A is equal to B.")
else:
   print("A is less than B.")
   if a > b:   # if condition True, action execute
      print("A is greater than B. nested")
   elif a == b:
      print("A is equal to B. nested")
   else:
      print("A is less than B. nested")

# get user ko age
# if age is less than 18 print out "not Eligible for license"
#     ask if they want to get license or not(y/n):
#          if yes: print a statement
#          if no: print a statement
# if age is greater than or equal to 18 print out "Eligible for license"
#     ask if they have license(y/n):
#        if yes: print a statement
#        if no: ask if they want to get a license(y/n)
#              if y: print a statement
#              if n: print a statement