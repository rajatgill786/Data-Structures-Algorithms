def funcwithoutbacktracking(i,n):
    if i >n:
        return
    print(f'funcwithoutbacktracking {i}')
    funcwithoutbacktracking(i+1,n)

funcwithoutbacktracking(1,5)


def funwithbacktracking(i,n):
    if i <1:
        return
    funwithbacktracking(i-1,n)
    print(f'funwithbacktracking {i}')

funwithbacktracking(5,5)