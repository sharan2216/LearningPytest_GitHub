dict1={'car':['ford','maruti','tata','ford','tata'],
       'brand':['mustang','range','mustang','range','mustang']}

dict2={}

for key,value in dict1.items():
    dict2[key]=set(value)
print(dict2)

#---------

dict3={'name':['A','B','C','A','C','B'],
       'age':[21,22,23,21,22,23]
       }
dict4={}
for key,value in dict3.items():
    dict4[key]=set(value)
print(dict4)