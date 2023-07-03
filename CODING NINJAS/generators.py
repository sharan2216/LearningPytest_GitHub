def factorial(n):
    i=1
    fact=i
    while(i<n):
        fact=fact*i
        print(fact)
        yield
        i=i+1


a=factorial(8)
a.__next__()
a.__next__()
a.__next__()
a.__next__()
a.__next__()

