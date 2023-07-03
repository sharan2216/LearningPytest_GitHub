#Recursion function
def factorial(n):
    return (n == 1) or (n * (factorial(n - 1)))


print(factorial(5))
