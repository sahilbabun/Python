# calculate hypotenuse of triangle

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a,2) + pow(b,2))

print(f"The value of side C is: {c}cm")
