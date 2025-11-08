from collections import Counter


def solution():
    # Read from stdin as expected by the test case
    n = int(input())
    numbers = list(map(int, input().split()))
    
    mean = sum(numbers)/n
    middle = int(n/2)
    numbers = sorted(numbers)
    if n%2 == 0:
        median = (numbers[middle] + numbers[middle - 1])/2 
    else:
        median = numbers[middle]
        
    mode_counter = Counter(sorted(numbers))

    mode = mode_counter.most_common(1)[0][0]
    
    print(mean)
    print(median)
    print(mode)


if __name__ == "__main__":
    solution()



    