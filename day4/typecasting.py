# Typecasting: Type conversion, changing datatype

# implicite typecast: compatibility match python datatype convert
# explicite typecast: manual process of changing datatype

a = 50
print(type(a))

# convert to string - str()
b = str(a)        # "50"
print(type(b))
print(b)
# b = "abc"

# convert to integer - int()
c = int(b)        # 50
print(type(c))
print(c)

# convert to float - float()
d = float(c)
print(type(d))
print(d)

# convert to list - list()
a = "ConvertConvert"
my_list = list(a)
print(my_list)

# convert to tuple - tuple()
my_tuple = tuple(my_list)
print(my_tuple)

# convert to set - set()
my_set = set(my_tuple)
print(my_set)

# convert to dictionary - dict()
b = [("name","ram"),("age","25")]
my_dict = dict(b)
print(my_dict)

# boolean
a = "abc"
my_bool = bool(a)
print(my_bool)

# Indexing and Slicing