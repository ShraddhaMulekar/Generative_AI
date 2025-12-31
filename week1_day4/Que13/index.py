# Q13: Leap Year Checker
# 📝 Problem Statement: Write a function is_leap_year(year) to check whether 
# a year is a leap year.

# 📌 Sample Output:

# print(is_leap_year(2024))  # True
# print(is_leap_year(2023))  # False
# 📚 Topic: Functions, Conditional Logic

def is_leap_year(year):
    if(int(year) % 4 == 0):
        return True
    else:
        return False

print(is_leap_year(2024))
print(is_leap_year(2025))
