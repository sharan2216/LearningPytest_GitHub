#fibonacci
a=0
b=1
sum=0

for i in range(2,10):
    sum=a+b
    print(sum)
    a=b
    b=sum
