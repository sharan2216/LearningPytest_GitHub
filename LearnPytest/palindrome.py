# Palindrome

str1="nitin"
n=len(str1)
x=0

for i in range(n):
    # print(str1[i])
    if str1[i]!=str1[n-i-1]:
        x=1
        break

if x==0:
    print("palindrome")
else:
    print("not a palindrome")

print("2nd method-------")
str1="jahaj"

if str1==str1[::-1]:
    print("palindrome")
else:
    print("Not a palindrome")

