arr=[1,1,2,2,1,3,4,5]

# lst=list(set(arr))
# print(lst)
arr2=[]
for i in arr:
    if i not in arr2:
        arr2.append(i)
print(arr2)