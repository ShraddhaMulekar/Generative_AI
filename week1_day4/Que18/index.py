# Q18: Convert a List of Names to Lowercase Using List Comprehension
# 📝 Problem Statement: Convert all names in the list to lowercase using 
# list comprehension.

# 📥 Input:

# ["John", "ALICE", "BOB"]
# 🎯 Expected Output:

# ["john", "alice", "bob"]
# 📚 Topic: List Comprehension, String Methods

word_list = ["john", "alice", "bob"]

lowercase_word = [word.lower() for word in word_list if word.isupper]
print(lowercase_word)

