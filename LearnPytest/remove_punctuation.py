str1="/* apples are & found % only @ red & green"
s=' '
for i in str1:
    if (i>='A' and i <='Z')|(i>='a' and i<='z')|(i==' '):
        s=s+i

print(s)