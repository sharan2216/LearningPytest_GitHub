l=[9,7,5,77,55,44,99,22,11,21,78]
maxi = l[10]
mini =l[0]

for i in l:
    if i > maxi:
        maxi = i
    if i < mini:
        mini = i

print(maxi)
print(mini)

