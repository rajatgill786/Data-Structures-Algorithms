def print_divisor(n):
    result = []
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            result.append(i)
            if i!=n//i:
                result.append(n//i)
    result.sort()
    return result

print(print_divisor(36))
