# String: String is a sequence of characters.
# we can write a string in three different ways:
a = 'Python'
b = "Python"
c = '''Python'''


# You can display a string literal with the print() function:
print(a)
print(b)
print(c)


# QUOTES INSIDE QUOTES:
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


# Strings are Arrays:
'''
   1. strings in Python are arrays of bytes representing unicode characters.
   2. However, Python does not have a character data type, a single character is simply a string with a length of 1.
   3. Square brackets can be used to access elements of the string. 

'''
a = "Hello, world!"
print(a)
print(a[1])


# Looping through a String:
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)


# String Length:
# -> To get the length of a string, use the "len()" function.
# -> The "len()" function returns the length of a string.
a = "Hello, world!"
print(len(a))


# CHECK STRING:
# 'in' keyword:
# -> To check if a certain phrase or character is present in a string, we can use the keyword "in".
# -> It returns a boolean: True if the phrase is present, False otherwise.
# Check if "free" is present in the following text:
txt = "The best thing in life are free!"
print("free" in txt)
print("bad" in txt)

# Use it in an "if" statement:
if "free" in txt:
    print("Yes, 'free' is present")


# CHECK IF NOT:
# 'not in' keyword:
# -> To check if a certain phrase or character is NOT present in a string, we can use the keyword 'not in'.
# -> It also returns a boolean: True if the phrase is present, False otherwise.
print("expensive" not in txt)

# Use it in an if statement:
if "expensive" not in txt:
    print("No, 'expensive' is NOT present")

