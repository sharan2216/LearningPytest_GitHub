def palin(s):
    str1=s
    str2= str1[::-1]
    if str1==str2:
        print("palindrome")
    else:
        print("not a palindrome")

palin("jahaj")
palin("jahaja")

