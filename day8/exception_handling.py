# Exception handling
# exception raise line place it in try block place
# except block: statements to be exected in case of exception
# can define multiple error specific except block
# can have one one catch all except block 

# try:
#    statement
# except:
#    statement

try:
   a = int(input("enter a number:"))
   print(b + 10)
except ValueError:
   print("ValueError")
except:
   print("Except block")


# calculator implement exception handling, Mark Evaluator