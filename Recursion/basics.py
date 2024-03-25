
"""
def fun():
    print('1')
    print('2')
    fun()
    print('3')

fun()


RecursionError: maximum recursion depth exceeded while calling a Python object
"""

count =1 
def func():
    global count
    print(count)
    if count ==5:
        return
    count =count+1
    func()
if __name__ =="__main__":
    func()