# def non_repeating(str1):
#     dict1={}
#     size=len(str1)
#     for i in range(size):
#         key=str1[i]
#         if key not in dict1:
#             dict1[key]=1
#         else:
#             dict1[key]=dict1[key]+1
#         # print(dict1)
#
#     for k,v in dict1.items():
#         if v==1:
#             print(k)
#             break
#
#
#
# s='aabbc'
# non_repeating(s)
# --------------------------
def newmethod(s1):
    size2=len(s1)
    dict2={}
    for i in range(size2):
        key=s1[i]
        if key not in dict2:
            dict2[key]=1
        else:
            dict2[key]=dict2[key]+1
    for k,v in dict2.items():
        if v==1:
            print(k)
            break


stringvalue='aabbccddeef'
newmethod(stringvalue)