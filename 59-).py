# 59) Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.

s='a-1,b-2,c-3'
print(type(s))

x=s.split(',')
print(x)
a=dict(x)
print(a)