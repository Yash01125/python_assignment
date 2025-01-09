#64)Write a Python function that checks whether a passed string is palindrome or not

def p(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(p("print"))
print(p("madam"))
