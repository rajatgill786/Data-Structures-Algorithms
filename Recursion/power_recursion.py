def power(b,e):
    if type(e) != int or e<0:
        raise Exception('Invalid input')
    if e ==0:
        return 1
    elif e==1:
        return b
    return b*power(b,e-1)

x = power(5,3)
print(x)