# Polymorphism: poly: muliple, morph: form
# different class with same method name
# functionality of the method depends on the object

class int:
   def __add__(self):
      print("addition of interger")

class str:
   def __add__(self):
      print("concatenate string")

# a = 10
# b = 5

# x = "a"
# y = "ball"

# print(a.__add__(b))
# print(x.__add__(y))



class Dog:
   def move(self):
      print("Dog move using leg.")

class Bird:
   def move(self):
      print("Bird moves using wings.")

class Fish:
   def move(self):
      print("Fish moves using fins.")

d1 = Dog()
b1 = Bird()
f1 = Fish()

d1.move()
b1.move()
f1.move()