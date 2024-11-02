# Write a program to fill in a letter template given below with name and date.
'''
    letter = "Dear <|Name|>, You are Selected!, <|Date|>."

'''

letter = "Dear <|Name|>, You are Selected!, <|Date|>."
print(letter.replace("<|Name|>", "Sahil").replace("<|Date|>", "03 November, 2024"))

