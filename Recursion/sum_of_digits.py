def withbacktrack(i,sum):
    if i<1:
        print(sum)
        return
    withbacktrack(i-1,sum+i)

withbacktrack(3,0)