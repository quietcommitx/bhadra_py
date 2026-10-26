# Abstraction: data hiding-> hide unnecessay details/event from user

class Bike:
   key = False
   gear = False
   acc = False
   clutch = False
   
   def start(self):
      self.key = True
      self.clutch  = True
      self.acc = True
      print("Bike start")

b1 = Bike()
b1.start()