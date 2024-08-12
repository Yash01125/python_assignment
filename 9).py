# 9) Write python program that swap two number with temp variable and without temp variable.

print('With temp variable')
print('*'*30)
a=10
b=20
print("Before Swap value A=",a,"and B=",b)

# with temp variable
temp=a
a=b
b=temp

print("After Swap value A=",a,"and B=",b)
print('*'*60)
print('Without temp variable')
print('*'*30)

a=50
b=60
print("Before Swap value A=",a,"and B=",b)

# without temp variable

a,b=b,a

print("After Swap value A=",a,"and B=",b)
