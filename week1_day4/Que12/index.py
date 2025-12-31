# Q12: Word Counter
# 📝 Problem Statement: Create a function count_words(text) that returns the 
# number of words in a sentence.

# 📌 Sample Output:

# print(count_words("Python is powerful"))  # 3
# 📚 Topic: Functions, Strings

def count_words(text):
    word = text.split()
    return len(word)

print(count_words("Python is powerful"))