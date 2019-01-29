# Uses python3
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

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    
    
    for i in range(2,100):
          mod_number1 = fib(i) % 10
          mod_number2 = fib(i + 1) % 10
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
        fin_number = fib(mod_number) % 10
        return fin_number


def fibonacci_sum_naive(n):
    if get_fibonacci_last_digit_naive(n+2) == 0:
        return 9
    else:
        last_digit = get_fibonacci_last_digit_naive(n+2)-1
        return last_digit

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
