# String Methods:

a = "Hello, world!"

# len() methods:
print(len(a))


# endswith("...suffix...") methods: 
'''
 -> It returns a boolean: True or False.
 -> It takes an input string.
'''
print(a.endswith("ld"))  # return False because it's not end with "ld".


# startswith("...prefix...") methods:
'''
 -> It returns a boolean: True or False.
 -> It also takes an input string.
'''
print(a.startswith("Hel"))  # return True because it starts with "Hel".


# capitalize() methods:
b = "python"
print(b.capitalize())   # return 'Python' because it capitalizes the only first letter of strings.


# upper() methods: returns the string in upper case.
print(b.upper())  # return: 'PYTHON' 


# lower() methods: returns the string in lower case.
print(a.lower())


# strip() methods: Removes any leading and trailing whitespace.
text = "  Hello, World!  "
print(text.strip())  # Output: "Hello, World!"


# replace(old, new) methods: replaces a string with another string.
print(a.replace("world", "Python"))  # Output: "Hello, Python!"


# split(separator) methods:
print(a.split())       # Output: ['Hello,', 'world!']
print(a.split(','))    # Output: ['Hello', ' world!']


# join(iterable) methods: Joins the elements of an iterable (e.g., a list) into a single string, with the string acting as a separator.
word = ["Hello", "World!"]
print(" ".join(word))


# find(substring) methods: Returns the index of the first occurrence of a substring. Returns -1 if not found.
txt = "Hello, World!"
print(txt.find("World!")) # Output: 7


# count(substring) methods: Returns the number of occurrences of a substring.
print(txt.count("o"))


