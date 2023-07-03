arr=[2,4,3,2,5,4,6,4,5,6,3,4,2]
arr2={}
# arr2=list(set(arr))
# print(arr2)

#using array:
# n=len(arr)
# ch=[]
# for i in arr:
#     while i not in ch:
#         ch.append(i)
# print(ch)

#using lambda function:----
# duplicate_func=lambda arr2:set(arr)
# print(duplicate_func(arr2))

# #using dictionary:---
dict1={'car':["A","B","C","A"],
       'brand':["abc","xyz","abc","xyz"]
      }
dict2={}
for key,value in dict1.items():
    dict2[key]=set(value)

print(dict2)