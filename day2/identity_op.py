# Identity operator: check if the variable and the merory location if the variables are same

a = 10
b = 10
c = 5
d = 5

print(id(a))
print(id(b))
print(id(c))
print(id(d))

# is: if memory location is same then return true else false
print(a is b)
print(a is c)

# is not: if memory location is not same then return true else false
print(a is not b)
print(a is not c)