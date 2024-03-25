#parameterised way 

def fun(i,sum):
    if i <1:
        print(sum)
        return
    fun(i-1,sum+i)

fun(10,0)

#functional way 

def fun1(n):
    if n==1:
        return 1
    return n+fun1(n-1)

x = fun1(10)
print(x)