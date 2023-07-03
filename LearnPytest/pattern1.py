def design_pattern(n):
    for row in range(1,6):
        for col in range(row,0,-1):
            print(col,end='')
        print()

design_pattern(5)

#2--------

def design_pattern2(n):
    space = 4
    for row in range(1,6):
        for k in range(1,space+1):
            print(" ",end="")
        for col in range(1,row+1):
            print(row,end=" ")
        print()
        space=space-1

design_pattern2(5)
