def recur_factorial(n):

    if n != 1:
       return n*recur_factorial(n-1)
    else:
        return n

n = 10
print(n,'s factorial is ==', recur_factorial(n))