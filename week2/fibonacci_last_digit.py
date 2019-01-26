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
        return c%10

n = int(input())
print(fib(n))

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
