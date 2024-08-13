# 29) Write a Python function to get the largest number, smallest num and sum of all from a list.

lst1=[1,2,3,4,5,6,7,8,9]

largest = 0
smallest = 0
total_sum = 0

for i in lst1:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
    total_sum += i
print(total_sum)
print(largest)
print(smallest)
