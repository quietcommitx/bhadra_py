# Pillars of OOP
# Inheritance: super-sub class, parent-child class, base-derived class
# properties of a class is inherited by another class
# child class can use the attributes and methods of parent class
# child class can have unique attributes and methods
# parent class and child class can have method with same name(override)

class Car:
   model = None
   brand = None
   color = None

   def get_detail(self, model, brand, color):
      self.model = model
      self.brand = brand
      self.color = color

   def show_detail(self):
      print(f"""Model: {self.model}
Brand: {self.brand}
Color: {self.color}""")

class EV(Car):
   speed = None
   
   def get_speed(self, speed):
      self.speed = speed
   
   def show_detail(self):
      print(f"""Model: {self.model}
Brand: {self.brand}
Color: {self.color}
Speed: {self.speed}""")

ev1 = EV()
ev1.get_speed("250")
print(ev1.speed)
ev1.show_detail()

# todo:
# create a class animal with attributes: eye, ear, legs, .....
# methods: sound, movement, ..., ...

# create a class dog that extends/inherits animal class with attribute name, ...
# methods: get name/details, sound, movement

# create a class bird that inherits animal class with name attribute,... methods: get name/details, sound, movement, ....
























# Polymorphism
# Encapsulation
# Abstraction