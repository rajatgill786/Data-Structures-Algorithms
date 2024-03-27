def sorted(arr):
    for i in range(0,len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True


x = sorted([1,3,4,5,6,66])
print(x)