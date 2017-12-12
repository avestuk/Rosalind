count = 0

def fib(n, k):
    if n == 1 or n ==2:
        global count = 1
    global count+= k
    return fib(n-1, k) + fib(n-1, k)


print(fib(5,3))
