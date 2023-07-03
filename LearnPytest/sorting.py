l=[32,31,21,22,12,13,14,15]

n=len(l)

for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]

print(l)

