# Object Oriented Programming: 

# class: structures, blueprints
# object: real world entity, data created using the class

# Syntax
# class class_name:
#    attributes
#    methods

# a = class_name()           # class_name(): class call, a is an object

class House:
   # attributes: floor, rooms, windows, door, stairs
   rooms = None
   windows = None
   doors = None
   
   def detail(self, room, window, door):
      self.rooms = room    # h1.rooms
      self.windows = window
      self.doors = door
   
   def show(self):
      print(f"""Rooms: {self.rooms}
Windows: {self.windows}
Doors: {self.doors}""")

h1 = House()
h1.detail(4, 2, 1)
h1.show()
# print(h1.rooms)   # 4
# print(h1.windows) # 2
# print(h1.doors) 

# constructor: a method that is automatically executed during object creation

class House:
   def __init__(self, room, window, door):
      self.rooms = room    # h1.rooms
      self.windows = window
      self.doors = door
   
   def show(self):
      print(f"""Rooms: {self.rooms}
Windows: {self.windows}
Doors: {self.doors}""")

h1 = House(4, 2, 1)      # House(): House class lai call, h1 is a object/instance of House class
# h1.show()
# h1.detail(4, 2, 1)
print(h1.rooms)   # 4
# print(h1.windows) # 2
# print(h1.doors)   # 1

# h2 = House()
# h2.floor = 3
# print(h2.floor)
# h2.roof = 1
# print(h2.roof)

# h3 = House()
# h3.floor = 11
# print(h3.floor)
# print(h3.rooms)
# print(h3.roof)

# create a class Car
# add attributes (....)
# create 3 objects using Car class

class str:
   def lower(self):
      print("this is a function inside a str class")
      
   def capitalize(self):
      print("Tjos os capitalize method")

a = "HELO"           # class str, a is an object
# print(type(a))
# print(a.lower())
# print(a.capitalize())

# todo:
# create a class Account 
# with attribute acc_number, balance, user name, address, contact,... attributes
# and get details/ constructor, add amount: get amt from user add it to balance, show detail: display acc_number, balance, user name, add, contact,... methods
# create 3 objects