#62)Write a Python function to check whether a number is in a given range

def re(number, start, end):
    return start <= number <= end

print(re(15,1,10))
print(re(5,1,10))