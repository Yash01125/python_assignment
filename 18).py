# 18)Write a Python program to count occurrences of a substring in a string.
def count(string, substring):
    return string.count(substring)

string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

occurrences = count(string, substring)

# Print the result
print(f"The substring occurs {occurrences} times in the main string.")
