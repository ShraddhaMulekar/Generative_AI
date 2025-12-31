# Q16: Create a List of First 10 Cubes Using List Comprehension
# 📝 Problem Statement: Generate a list of cubes from 1 to 10 using list 
# comprehension.

# 🎯 Expected Output:

# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
# 📚 Topic: List Comprehension

cubes = [num**3 for num in range(1,11)]
print(cubes)