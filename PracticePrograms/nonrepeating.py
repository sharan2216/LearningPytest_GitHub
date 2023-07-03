def non_repeating(str):
    dict={}
    size=len(str)

    for i in range(size):
        key=str[i]
        if key not in dict:
            dict[key]=1
        else:
            dict[key]=dict[key]+1

    print(dict)

    for key,value in dict.items():
        if (value==1):
            print(key)
            break

non_repeating('aabbccddsgghh')


