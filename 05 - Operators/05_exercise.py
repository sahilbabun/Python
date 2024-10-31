# Calculate the area of circle using math module

import math

radius = float(input("Enter radius: "))
# area = math.pi * radius ** 2
area = math.pi * pow(radius, 2)
print(f"The area of circle is: {round(area, 2)}cm")

