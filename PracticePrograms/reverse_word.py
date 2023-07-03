str1 = 'my name is kant'

# str2 = str.split(str1)
# size = len(str2)
# rev_all=''
# for i in range(size):
#     rev = reversed(str2[i])
#     rev_all = i + rev_all + ""
#
#     print(rev_all)
str2=str1.split(' ')
n = len(str2)
str2=str2[::-1]
str2=' '.join(str2)
print(str2)
