#fibonacci series

def fibo():
    a=0
    b=1

    while True:
        yield a
        a,b=b,a+b


f1=fibo()

print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))
print(next(f1))