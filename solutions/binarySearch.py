def binarySearch(arr, target):
    L, R = 0, len(arr) - 1

    while L<=R:
        mid = (L+R)//2

        if target < arr[mid]:
            R = mid - 1
        elif target > arr[mid]:
            L = mid + 1
        else:
            return mid
        
    return -1


if __name__ == "__main__":
    arr = [1,2,3,4,5]

    x = binarySearch(arr, 4)

    print(x)
        
        