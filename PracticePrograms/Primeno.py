count=0
n=7

if n>1:
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not a prime")


