empty_dict={}
print(type(empty_dict))
print("---------")
a={}
a['jan']=1
a['feb']=2
a['mar']=3
print(a)
print("---------")
#dictionary of integers------
dict1={1:'Net',2:'Set',3:'OS'}
print(dict1)
#dictionary of mixed values-------
print("---------")
dict2={'Name':'NetSetos',1:[1,2,3,4]}
print(dict2)
print(dict2.keys())
print(dict2.values())
print(dict2['Name'])
# print(dict2['Age'])
print("---------")
print(dict2.get('Name'))
print("---------")
dict3=dict([(1,'python'),(2,'java')])
print(dict3)
print(dict3.get(1))
print("---Dictionary Operations------")
#Dictionary Operations
a={1:'Jan',2:'Feb',3:'Mar',5:'Apr',6:'May',6:'Jun'}
# print(a)
# b=dict(a)
b=a.copy()
print(b)
print("------------")
dict11={'Name':'Rahul','Class':'5','Roll No':34}
print(dict11)
dict11['Name']='Abhishek'
print(dict11)
dict11['Address']='MG Road,Bangalore'
print(dict11)
c=dict11.pop('Roll No')
print(c)
print(dict11)





