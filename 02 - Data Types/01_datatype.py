# Built-in Data Types:
#  -> Python variables can hold values of different data types, and different types can do different things.

# Python has the following data types built-in by default, in these categories:
# Text Type:        --->	    str
# Numeric Types:    --->	    int, float, complex
# Sequence Types:   --->	    list, tuple, range
# Mapping Type:	    --->        dict
# Set Types:	    --->        set, frozenset
# Boolean Type:	    --->        bool
# Binary Types:	    --->        bytes, bytearray, memoryview
# None Type:	    --->        NoneType


# Getting the data type:
# -> You can get the data type of any object by using the type() function:
x = 5
print(type(x))


# Setting the data type:
# -> In Python, the data type is set when you assign a value to a variable:

# String:
s = "Hello World"
print(s)        # display x:
print(type(s))  # display the data type of x: str


# Complex:
c = 1j
print(c)        # display a:
print(type(c))  # display the data type of a: complex


# list:
l = ["apple", "banana", "cherry"]
print(l)        # display b:
print(type(l))  # display the data type of b: list

# tuple:
t = ("apple", "banana", "cherry")
print(t)        # display t:
print(type(t))  # display the data type of t: tuple

# dictionary:
d = {"name" : "John", "age" : 36}
print(d)        # display d:
print(type(d))  # display the data type of d: dict

# set:
st = {"apple", "banana", "cherry"}
print(st)       # display st:
print(type(st)) # display the data type of st: set

