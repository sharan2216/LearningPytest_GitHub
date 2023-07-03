set1={'python','java','c'}
set1.add('c++')
print(set1)
set2={1,2,3}
set2.update({5,6,7})
print(set2)
# print(set2[1])
print("-----------")
list1=[1,2,3]
list2=[4,5,6]
list3=[7,8,9]

set1 = set(list1)
set2 = set(list2)
set1.update(set2)
print(set1)
set1.update(list3)
print(set1)

print("----------")
a={1,3,5,7,9}
a.remove(1)
print(a)
a.discard(7)
print(a)
print("----------")
#frozenset

student={'name':'Ankit,'Age':21,'sex':'male',}
