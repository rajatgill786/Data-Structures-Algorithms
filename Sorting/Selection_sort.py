def selection_sort(arr):
    n = len(arr)

    #traverse through all element
    for i in range(n):
        #find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1,n):
            if arr[j]<arr[min_idx]:
                min_idx = j
                #swap the found minimum element with the first element
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    return arr

arr = [23,2,1,44,5,6,7,8,9,86,55,4,3,5,6]

x  = selection_sort(arr)
print(x)