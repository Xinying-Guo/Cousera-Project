# python3

def max_pair_1(numbers):
    n = len(numbers)
    if n == 1:
        return 0
    else:
        if numbers[0] > numbers[1]:
            max1 = numbers[0]
            max2 = numbers[1]
        else:
            max1 = numbers[1]
            max2 = numbers[0]
        for i in range(2,n):
            if numbers[i] > max2:  
                if numbers[i] > max1:
                    max2 = max1
                    max1 = numbers[i]
                else:
                    max2 = numbers[i]
        return max1*max2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pair_1(input_numbers))
