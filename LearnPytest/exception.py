l=[9,7,5,77,55,44,99,22,11,21,78]

sum = 0

for i in l:
    if i == 99:
        raise Exception("exception :1 is found")
    else:
        sum = sum+1

print(sum)