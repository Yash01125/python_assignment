# 13) Write a Python program that will return true if the two given integer values are equal or their sum of difference is 5.

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

if a==b or (a-b)==5 or (a+b)==5:
    print('True')
else:
    print('False')