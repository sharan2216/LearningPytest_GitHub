def least_repeating(s, search_char):
    ch = {}
    for i in s:
        if i in ch:
            ch[i] = ch[i] + 1
        else:
            ch[i] = 1
    print(ch)
    try:
        print(ch[search_char])
    except:
        print(0)

    print(ch)
str = "sfsffdsfdssfsfsfeesrfvdsv"
least_repeating(str,'s')

#
# def newsearch(s,searchstr):
#     ch={}
#     for i in s:
#         if i in ch:
#             ch[i] = ch[i]+1
#         else:
#             ch[i] = 1
#     try:
#         print(ch[searchstr])
#     except:
#         print(0)
#
#
#
# str1="sfsdfsdgdsgdsgd"
# newsearch(str1,'d')