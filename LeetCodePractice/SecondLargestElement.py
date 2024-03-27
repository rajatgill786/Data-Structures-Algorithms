def SecondLargestElement(arr):
    small = float('inf')
    s_small = float('inf')
    large = float('-inf')
    s_large = float('-inf')
    for i in range(0,len(arr)):
        if arr[i]<small:
            s_small = small
            small = arr[i]
        elif arr[i]<s_small and arr[i]!=small:
            s_small = arr[i]
    for i in range(0,len(arr)):
        if arr[i]>large:
            s_large = large
            large = arr[i]
        elif arr[i]>s_large and arr[i]!=large:
            s_large = arr[i]
    return[s_small,s_large]

x = SecondLargestElement([1,3,5,3,2,57,80])
print(x)