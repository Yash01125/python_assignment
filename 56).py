# 56)Write a Python program to map two lists into a dictionary
# Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

d1=[1,2,3]
d2=['yash','meru','shubh']

x=dict(zip(d1,d2))
print(x)
print(type(x))