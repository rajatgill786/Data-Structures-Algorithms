def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key

arr = [23,2,1,44,5,6,7,8,9,86,55,4,3,5,6]
insertion_sort(arr)
print(arr)