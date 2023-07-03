x=(10,20,[40,50,60])
print(x)
x[2][0]=30
print(x[2][0])

print("------------")
tup=("Reena","Sheena")+("Meena","Neena")
print(tup)

tup1=(("reena")*4)
print(tup1)

tup2=(1,2,3,1,2,7,1,5,8)
print(tup2.count(1))
print(1 in tup2)
print(9 not in tup2)
a=sorted(tup2)
print(a)
print(max(tup2))
print(min(tup2))
print(sum(tup2))
