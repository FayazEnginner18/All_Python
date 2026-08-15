def recur(n):
    if n==0:
        return 1
    else:
        return n*recur(n-1)
print(recur(0))

# def countdown(n):
#     if n==0:
#         print("done!")
#         return
#     print(n)
#     countdown(n-1)
# countdown(5)
def nested(data):
    total=0
    for item in data:
        if isinstance(item,list):
            total+=nested(item)
        else:
            total+=item
    return total

lists=[1,[2,[3,[4,[5,[6]]]]]]
print(nested(lists))

# c=(10)
# if isinstance(c,int):
#     print("yes")
# else:
#     print("no")

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)

print(fib(10))

import sys
print(sys.getrecursionlimit())