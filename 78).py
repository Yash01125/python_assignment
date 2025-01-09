#78) Write a python program to find the longest words.

def find_word(text):
    words = text.split()
    long_word = max(words, key=len)
    return long_word

# Example usage:
text = "My name is Yash Mordhara"
long_word = find_word(text)
print(f"The longest word is: {long_word}")
