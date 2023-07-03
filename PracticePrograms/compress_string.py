def compress(s):
    n=len(s)
    s2=''
    count=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            count=count+1
        else:
            s2 = s2 + s[i] + ":" +str(count)+" "
            count=1
    return s2

s='aassddffggddsreer'
print(compress(s))
