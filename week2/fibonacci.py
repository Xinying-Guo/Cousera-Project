# Uses python3
def fib(n):
    a = 0
    b = 1
    if n <= 1:
        return n
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return c

n = int(input())
print(fib(n))