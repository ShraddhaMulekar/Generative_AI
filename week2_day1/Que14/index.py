# Q14: Compute Area of Circle Using Lambda
# 📝 Problem Statement: Convert the function to lambda to compute the area of a circle.

# 📥 Input: radius = 5

# 🎯 Expected Output:

# 78.53981633974483
# 📚 Topic: Lambda Functions, Math

import math

number = int(input("Enter the number: "))
p = math.pi

area_of_circle = (lambda x:p*x*x)
print(area_of_circle(number))
