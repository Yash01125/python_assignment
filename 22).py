# 22) Write a Python function to reverses a string if its length is a multiple of 4.

def string(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s

a = input("Enter a string: ")
ans = string(a)
print("Resulting string:", ans)

