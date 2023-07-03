arr=[2,4,3,2,5,4,6,4,5,6,3,4,1]
n=len(arr)
max = arr[n-1]
min = arr[0]

for i in arr:
    if i>max:
        max=i
    else:
       if i<min:
           min=i

print(max)
print(min)

