# Accounting

# register/Login
# if choice register
# get username and password from user and store the data in a file
# if choice is login
# get username and password from user 

# check if the username exist in the file (y/n):
#  if no print a statement("User does not exist")
#     if yes, check if the entered password is equal to the password in the dictionary(y/n)
#        if no, print a statement("Invalid credential")
#        if yes, show 2 choice. 1. Show detail, 2. Add balance, 3. Withdraw
#              if user choice 1: show the user balance from the file
#              if user choice 2: get amount to add from user, get balance from the file and add the amount with the balance, print the total balance
#              if user choice 3: get amount to withdraw,  get balance from the file, check if the amount is less than balance(y/n), if yes subtract amount from balancew, if no print out insufficient balance

username = input("Enter username: ")
password = input("Enter password: ")
login = False
for i,j in user_details.items():
   if i == username and password == j:
      login = True

if login:
   print("SHow the choices 1,2,3")
else:
   print("Invalid credential")