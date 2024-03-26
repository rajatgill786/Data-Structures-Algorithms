def partition(arr,high,low):
    pivot = arr[low]
    i = low
    j = high

    while i <j:
        while arr[i] <= pivot and i <=high-1:
            i +=1
        while arr[j] >pivot and j >= low+1:
            j -=1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]
    arr[low],arr[j] = arr[j],arr[low]
    return j 

def quick_sort(arr,low,high):
    if low<high:
        p_index = partition(arr,high,low)
        quick_sort (arr,low,p_index-1)
        quick_sort(arr,p_index+1,high)

arr = [23,2,1,44,5,6,7,8,9,86,55,4,3,5,6]
quick_sort(arr,0, len(arr) - 1)
print(arr)