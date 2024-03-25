str = 'aeeroplanner'  #97-122


char_hash = [0]*26

for ch in str:
    idx = ord(ch)-97
    char_hash[idx]+=1
print(char_hash)
print(char_hash[ord('a')-97])