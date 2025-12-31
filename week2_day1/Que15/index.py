# Q15: Calculate Compound Interest Using Lambda
# 📝 Problem Statement: Convert the function to lambda to calculate compound interest.

# 📥 Input: p=1000, r=5, t=2

# 🎯 Expected Output:

# 1102.5
# 📚 Topic: Lambda Functions, Math

import math

compound_interest = lambda p,r,t: p* math.pow((1+r/100),t)
print(compound_interest(1000, r=5, t=2))
