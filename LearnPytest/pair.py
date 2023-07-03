l=[2,3,4,5,6,7,10,8,9,1]
n=len(l)

for i in range(1,n):
    for j in range(i+1,n):
        if l[i]+l[j]==15:
            print(l[i],l[j])
