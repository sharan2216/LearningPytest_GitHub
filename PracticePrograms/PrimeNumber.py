def primeno(start,end):
    for num in range(start,end):
        if num>1:
            for i in range(2, num + 1):
                if num % i== 0:
                    break
                else:
                    print(num)


primeno(2,100)
