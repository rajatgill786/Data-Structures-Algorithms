list = [1,2,3,2,1,2,3,21,1,1,2,334,4]

hash_map = {}

for num in list:
    hash_map[num] = hash_map.get(num,0)+1

print(hash_map)