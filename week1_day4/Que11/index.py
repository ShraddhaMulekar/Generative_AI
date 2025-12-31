# Q11: Even or Odd Checker
# 📝 Problem Statement: Write a function check_even_odd(num) that returns 
# "Even" if number is even, otherwise "Odd".

# 📌 Sample Output:

# print(check_even_odd(7))   # Odd
# print(check_even_odd(10))  # Even
# 📚 Topic: Functions, Conditional Logic

def check_even_odd(num):
    if(num%2==0):
        return(f"{num} is: Even")
    else:
        return(f"{num} is: Odd")

print(check_even_odd(15))
print(check_even_odd(18))
