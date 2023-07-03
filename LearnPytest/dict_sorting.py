dict1={1:"Apple",3:"grape",2:"banana",5:"orange",4:"mango",7:"guava",6:"pineapple"}
d=sorted(dict1)
print(d)
dict2={}
for i in d:
    dict2[i]=dict1[i]
print(dict2)

