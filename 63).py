#63)Write a  Python function to check whether a number is perfect or not.

def number(n):
    if n <= 0:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

print(number(6))
print(number(10))