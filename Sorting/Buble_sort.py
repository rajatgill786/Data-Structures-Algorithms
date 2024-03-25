def buble_sort(arr):
    n = len(arr)
#traverse through all element in reverse order
    for i in range(n-1,0,-1):
        #last i element already in place
        for j in range(0,i):
            #traverse the array 0 to i
            #swap if the element found is greaterthan the next element
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
    return arr
arr = [23,2,1,44,5,6,7,8,9,86,55,4,3,5,6]
x = buble_sort(arr)
print(x)