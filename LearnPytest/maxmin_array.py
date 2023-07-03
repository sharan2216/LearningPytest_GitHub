def maxmin(arr):
    max=arr[0]
    size=len(arr)

    for i in range(size):
        if arr[i]>max:
            max=arr[i]
    return max


arr=[5,4,6,7,3,2,1,9,8]
print(maxmin(arr))

def minarr(arr):
    min=arr[0]
    size2=len(arr)
    for i in range(size2):
        if arr[i]<min:
            min=arr[i]
    return min


arr=[5,4,6,7,3,2,1,9,8]
print(minarr(arr))
