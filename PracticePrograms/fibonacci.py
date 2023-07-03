# a=0
# b=1
# sum=0
# for i in range(2,10):
#     sum=a+b
#     print(sum,end=' ')
#     a=b
#     b=sum
#

#factorial:

def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

n=5
print(f"factorial of {n} is :", fact(n))

#sum of array:
arr=[2,3,4,5,1,6]
print(f"sum of array is :",sum(arr))
l=len(arr)
for i in range(1,l):
    if i>i+1:
        max=i
    else:
        max=i+1

print("max no of an array is :",max)