# Uses python3
import sys

def gcd_naive(a,b):
    if a > b:
        m = a%b
        while m > 0:
            a = b
            b = m
            m = a%b
        return b
    else:
        m = b%a
        while m > 0:
            b = a
            a = m
            m = b%a
        return a

def lcm_naive(a,b):
    g = gcd_naive(a,b)
    return int((a*b)//g))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

