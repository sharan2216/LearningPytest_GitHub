l=[12,11,10,13,14,15]
# inputList.reverse()
# l.sort()
l1=l[::-1]
print(l1)

s=['ccc','aaa','d','bb']
# d=sorted(s) #['aaa', 'bb', 'ccc', 'd']
d=sorted(s,key=len)
print(d)
print(s)
print("-------------")

a=[10,20,30]
b=a
b.append(40)
print(a)
print(b)
print("-------------")
txt='welcome to the jungle'
x=txt.split(' ')
# x=txt.split()
print(x)

print("SLICING-------------")
name=['Reena','Sheena','Meena','Teena','Leena',]
print(name[:])
print(name[:3])#upto 3
print(name[::2])
print(name[2::2])

print("-----------")
num=[1,4,7,9]
str=["neena","meena"]
print(num+str)

num=[1,3,4,6,3,1,4,6,6]
print(num.count(6))