def searchchar(str,searc_ch):
    ch={}
    for i in str:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=1
    print(ch)

    try:
        print(ch[searc_ch])
    except:
        print(0)


s='dfgfdgfdgfdgfdgfd'
searchchar(s,'g')



