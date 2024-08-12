# 14)Write a python program to sum of the first n positive integers.

n=int(input("Enter a number: "))
x=0
if n < 0:
    print("Negative number")
for i in range(1,n+1):
    x=x+i
print(x)