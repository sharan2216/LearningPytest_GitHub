num=5
count=0
if num>1:
    for i in range(1,num+1):
        print(i)
        if(num%i)==0:
            count=count+1
    if count==2:
        print("no is prime")
    else:
        print("no is not prime")

