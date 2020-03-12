# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    if numbers[0]<numbers[1]:
        numbers[0],numbers[1] = numbers[1], numbers[0]
    for i in range(2,n):
        if numbers[i]>numbers[1]:
            if numbers[i]>numbers[0]:
                numbers.insert(0,numbers[i])
                numbers.pop(i+1)
            else:
                numbers[i],numbers[1] = numbers[1], numbers[i]
    
    return numbers[0]*numbers[1]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
