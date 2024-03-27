def largestElementArray(arr):
    largest =0
    for i in range(0,len(arr)):
        if arr[i]> largest:
            largest = arr[i]
    return largest

x = largestElementArray([1,2,34,4,5,56,6,643,22222,23])
print(x)