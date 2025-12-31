# Q10: Calculator Function
# 📝 Problem Statement: Create a function calculator(a, b, operation) that performs add, subtract, multiply, or divide.

# 📌 Sample Output:

# print(calculator(10, 5, 'add'))        # 15
# print(calculator(10, 5, 'divide'))     # 2.0
# print(calculator(10, 0, 'divide'))     # Cannot divide by zero
# 📚 Topic: Functions, Conditional Logic


def calculator(a, b, operation):
    if (operation == "add"):
        return("Addition: ",a+b)
    elif (operation == "substraction"):
        return("Substraction: ",a-b)
    elif (operation == "multiplication"):
        return("Multiplication: ",a*b)
    elif (operation == "divide"):
        if(b == 0):
            return("Cannot divide by zero")
        else:
            return("Division: ",a/b)
    else:
        return("operation not valid😔")


print(calculator(10, 5, "add"))
print(calculator(10, 5, "substraction"))
print(calculator(10, 5, "multiplication"))
print(calculator(10, 5, "divide"))
print(calculator(10, 0, "divide"))
print(calculator(10, 8, "modulo"))


