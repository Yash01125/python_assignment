# 26)How will you remove last object from a list?
#
# - To remove the last object from a list in Python, you have a few options.there are givenif below...
#
# 1. Using the pop() Method:
print('Using pop() Method')
lst1=[1,2,3,4,5]
print(lst1.pop())
print(lst1)

# 2. Using Slicing:
print('Using Slicing')
print(lst1[:-1])

# 3. Using del Statement
print('Using del statement')
del lst1[-1]
print(lst1)






