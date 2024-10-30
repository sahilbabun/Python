# Global variables:
# -> Variables that are created outside of the function are known as Global variables.
# -> Global variables can be used by everyone, both inside of functions and outside.

# Create a variable outside of a function, and use it inside the function:
x = "awesome"
def myFunc():
    print("Python is "+ x)
myFunc()

# If you create a variable with the same name inside a function, this variable will be local, 
# ... and can only be used inside the function. The global variable with the same name will remain as it was, 
# ... global and with the original value.

# Create a variable inside a function, with the same name as the global variable:
a = "awesome"
def myFunction():
    a = "fantastic"
    print("Python is "+ a)
myFunction()
print("Python is "+ a)


