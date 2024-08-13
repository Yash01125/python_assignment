# 49) Write a Python script to concatenate following dictionaries to create a new one.

dict1={1:'yash'}
dict2={2:'meru'}
dict3={}

for i in (dict1,dict2):
    dict3.update(i)
print(dict3)