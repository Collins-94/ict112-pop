"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
ef reversed_string(input_string):
    input_string = "Programming"
    return input_string[::-1]
original_string = "Programmig"
reversed_string = reversed_string(original_string)
print(f"The reversed string of '{original_string}' is: '{reversed_string}'")



"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def print_name(full_name):
    full_name = input("Enter name")
    name_parts = full_name.split()
    name = ""
    for part in name_parts:
        if part:
            name += part[0].upper() + "."
    print(name[:-1])
user_full_name = input("Enter your full name: ")
print_name(user_full_name)



"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""
def is_palindrome(input_string):
    processed_string = ''.join(filter(str.isalnum, input_string)).lower()
    reversed_string = processed_string[::-1]
    return processed_string == reversed_string
test_string = input("Enter a string: ")
if is_palindrome(test_string):
  print(f"'{test_string}' is a palindrome.")
else:
  print(f"'{test_string}' is not a palindrome.")



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
def count_words(sentence):
    words = sentence.split()
    return len(words)
user_sentence = input("Enter a sentence: ")
word_count = count_words(user_sentence)
print(f"The sentence '{user_sentence}' contains {word_count} words.")



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""
def replace_is_with_was(input_string):
    changed_string = input_string.replace("is", "was")
    return changed_string
original_string = "This is a string and it is an example."
changed_string = replace_is_with_was(original_string)
print(f"Original string: {original_string}")
print(f"Changed string: {changed_string}")
