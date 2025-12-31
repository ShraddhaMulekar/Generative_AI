# Q17: Extract Only Odd Numbers from a Given List
# 📝 Problem Statement: Use list comprehension to extract odd numbers from a 
# given list.

# 📥 Input:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_num = [num for num in numbers if num%2!=0]
print(odd_num)

