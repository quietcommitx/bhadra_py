# Encapsulation: bind the properties into a single unit, data hiding/ attribute and methods private, 
# "__" is followed by attributes or methods name to make them private
# to access private properties a public methods is to be used
class Login:
   def get_info(self,username, password):
      self.__username = username
      self.__password = password
   
   def __detail(self):
      print(f"Username: {self.__username}, Password: {self.__password}")
   
   def show(self):
      return self.__detail()


p1 = Login()
p1.get_info("ram", "ram123")
p1.show()
# print(p1.__username)
# print(p1.__password)

# todo:
# creat a class Account with attribute: username, acc_number, acc_balance, password, define private attribute
# method: login(username, password), show details(user details show), define private methods
# create 2 objects, print out all the details 