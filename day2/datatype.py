# Datatype

# string: alphabets, number, speciabl characters
# define usong ['...', "...", '''...''', """..."""]

# a = 'this is a line\'s 123 #$*&#()'
# b = "this is \"WOrld\" a line's"
# c = '''this is 
# "World" a line's'''
# """this is a line"""
a = "10"
print(a)
print(type(a))
# print(b)
# print(c)

# interger: whole number
a = 10            
# overwrite: 'a' variable has both string and interger assigned to it, calls the most recent variable or closest variable
print(a)
print(type(a))


# float: decimal number
a = 10.5
print(a)
print(type(a))

# boolean data
a = True
b = False
print(type(a))

# None type
a = None
print(type(a))


# Group datatype:
# List: [] is used to define list, can contain multiple data of multiple datatype, mutable(changeable), ordered
my_list = [1,2,3,4, "hi","hello", 15.55, 20.5]
print(my_list)
print(type(my_list))


# Tuple: () used to define tuple, can contain multiple data of multiple datatype, ordered, immutable(unchangeable)
my_tuple = (1,2,3,4, "hi","hello", 15.55, 20.5)
print(my_tuple)
print(type(my_tuple))

# Set: {} used to define set, can contain multiple data of multiple datatype, unordered, does not contain duplicate data
my_set = {1,2,3,4, "hi","hello", 15.55, 20.2 , "hi","hi", 2,2,3}
print(my_set)
print(type(my_set))

# Dictionary: {} used to define dictionary, key:value pair ->a data, key should be unique
my_dict = {"key":"value", 1:10, "name":"ram", "age":35,"name":"sita"}
print(my_dict)
print(type(my_dict))