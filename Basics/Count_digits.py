import math

def count_digit(num:int)->int:
    return math.floor(math.log10(num)+1)


print(count_digit(1234))