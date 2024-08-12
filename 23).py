# 23) Write a Python program to get a string made of the first 2 and the last
# 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string.

def char(s):
    if len(s) < 2:
        return s

    first_two = s[:2]
    last_two = s[-2:]
    return first_two + last_two

string= input("Enter a string: ")
ans = char(string)
print("Resulting string:", ans)
