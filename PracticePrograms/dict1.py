def method1(n):
    dict={3:'FIZZ',5:'BUZZ'}

    for i in range(1,n+1):
        result=''
        for k,v in dict.items():
            if i%k==0:
                result=result+v
            if not result:
                result=i
            print(result)

method1(15)
