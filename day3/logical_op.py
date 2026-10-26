# Logical operator

# and: if both conditions are True then Output: True, otherwise False
# True, True = True
# True, False = False
# False, True = False
# False, False = False

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

a = 5
b = 10
c = 1
print(a < b and a < c)     # a < b = True, a < c = False

# or: if any one condition is True then output: True, otherwise False
# True, True = True
# True, False = True
# False, True = True
# False, False = False

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

print(a < b or a < c)


# not: if condition is True, output: False, vise versa
# True = False
# False = True

# print(not True)
# print(not False)

print(not (a < b or a < c))
