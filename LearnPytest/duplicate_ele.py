arr=[1,4,3,6,2,5,3,5,5,6,2,1,1]
arr2=set(arr)
print(arr2)

#using array:----
arr3=[]
for i in arr:
    if(i not in arr3):
        arr3.append(i)
print(arr3)

#using Lambda:---

output=lambda arr:set(arr)
print(output(arr))