def charsearch(str,c):
    ch={}
    for i in str:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=1
    print(ch)
    try:
        print(ch[c])
    except:
        print(0)


charsearch("ssghdfkghfkdghdfkjhgdfklghldss","s")