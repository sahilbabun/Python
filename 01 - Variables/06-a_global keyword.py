# The "global" Keyword:
# -> Normally, when you create a variable inside a function, that variable is local,
#   ... and can only be used inside the function itself.



# -> To create a global variable inside a function, you can use the "global" keyword.
def myFunc():
    global x
    x = "awesome"
myFunc()
print("Python is "+ x)



# Also, use the "global" keyword if you want to change a global variable inside a function.
# Example:
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"
def myFunction():
    global x
    x = "fantastic"
myFunction()
print("Python is "+ x)

