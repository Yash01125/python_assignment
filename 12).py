# 12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
c=int(input("Enter 3rd number: "))

sum=a+b+c
#print(sum)
if a==b:

    sum=0
elif b==c:
    sum=0
elif c==a:
    sum=0
else:
    print("The sum is",sum)
print('Sum: ',sum)