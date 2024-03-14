from math import sqrt


def checkPrime(num):
    for i in range(2,int(sqrt(num))+1):
        if num %i ==0:
            return False
    return True

print(checkPrime(2))


"""
TC : O(sqrt(n))
SC : O(1)
"""