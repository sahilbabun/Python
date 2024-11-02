# Write a program to detect space in a string.

letter = "   Dear Sahil, You are Selected!    "
print(letter.strip())

# Write a program to detect double space in a string.
letter = "Dear Sahil,  You are Selected!"
print(letter.find("  "))  # return: -1
print(letter.find("  "))  # return: 11 

