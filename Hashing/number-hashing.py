arr= []
for i in range(12):
    num = int(input('Enter the number into list : '))
    arr.append(num)
print(arr)

#precompute

hash_list =[0]*13
for num in arr:
    hash_list[num]+=1
print(hash_list)

print(hash_list[1])