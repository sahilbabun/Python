# Slicing Strings:
'''
 -> You can return a range of characters by using the slice syntax.
 -> Specify the start index and the end index, separated by a colon, to return a part of the string.


      name = " p  y  t  h  o  n "   => Length: 6
index=         0  1  2  3  4  5 
 
              -6 -5 -4 -3 -2 -1   => Indexing, in reverse order.

    -> The index in a string starts from 0 to (length - 1).
    
    Syntax:
            sl = name [ index_start : index_end ]

           ^ index_start = first index included
           ^ index_end = last index is not included

           sl[0:3] returns "pyt" ---> characters from 0 to 3
           sl[1:3] returns "yt" ---> characters from 1 to 3

      Use of Double colon:
      -> A double colon (::) lets us include a third parameter, the step, after the second colon. 
      This extra flexibility allows for more complex slicing, such as skipping characters or reversing a string.

      text = "Hello, World!"
      print(text[0:len(text):2])  # Output: "Hlo ol!"

'''

b = "Hello, world!"
print(b[2:5])  # 'llo'
print(b[0:3])

# Negative Indexing:
print(b[-4:-1])
print(b[1:4])  # In positive form of b[-4 : -1]

# Slice from the start:
print(b[ : 5])  # we also write this as: print(b[0:5])

# Slice from the end:
print(b[2: ])   # By leaving out the end index, the range will go to the end.

# Slicing with skip value:  string[start: end: step(skip)]
print(b[0: len(b): 3])
print(b[:: 3])  # 'Hl r!'
# Reverse the string:
print(b[:: -1])


