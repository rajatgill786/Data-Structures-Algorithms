#Without backtracking
def funwithoutbacktracking(i,n):
    if i<n:
        return
    print(i)
    funwithoutbacktracking(i-1,n)
    

funwithoutbacktracking(10,1)

#with backtracking


def funwithbacktracking(i,n):
    if i >n:
        return
    funwithbacktracking(i+1,n)
    print(i)

funwithbacktracking(1,10)