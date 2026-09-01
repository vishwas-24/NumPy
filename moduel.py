# Moduel = a file containg code you want to include in your program use 'import' to include a module (built-in or your own) 
#          usefull to break up a large program reusable seprate files
# print(help("modules"))

# import math
# import math as m
# from math import pi
# print(math.pi)

import example

result = example.pi
result1 = example.square(3)
result2 = example.cube(3)
result3 = example.circumference(3)
result4 = example.area(3)
print(result)
print(result1)
print(result2)
print(result3)
print(result4)