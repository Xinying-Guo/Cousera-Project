# Uses python3
import sys

import sys

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

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    
    
    for i in range(2,m*m):
          mod_number1 = fib(i) % m
          mod_number2 = fib(i + 1) % m
          if mod_number1 == 0 and mod_number2 == 1:
              break
          else:
              continue

    mod_number = n % i
    if mod_number <= 1:
        return mod_number
    elif mod_number == 2:
        return 1
    else:
        fin_number = fib(mod_number) % m
        return fin_number
    

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
