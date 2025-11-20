from typing import List

class Pair:
    def __init__(self, key: int , value: int):
        self.key = key
        self.value = value

class Solution:
    def quickSort(self, pairs: List[Pair]):
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, arr, s: int, e: int):
        if e - s + 1 <= 1:
            return
        
        pivot = arr[e]
        left = s

        for i in range(s,e):
            if arr[i].key < pivot.key:
                #if this is the case then we swap elements
                #we swap the left with the ith element
                tmp = arr[left]
                arr[left] = arr[i]
                arr[i] = tmp
                left += 1

        """
        After we exit the loop, we found the position of the inital left, so we swap first the pivot with the left position
        And then we recursively so the quick sort of left and right part
        """

        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic test
    pairs1 = [
        Pair(3, 1),
        Pair(1, 2),
        Pair(4, 3),
        Pair(2, 4),
        Pair(5, 5)
    ]
    
    print("Test 1:")
    print("Before sorting:", [(p.key, p.value) for p in pairs1])
    sorted_pairs1 = solution.quickSort(pairs1)
    print("After sorting:", [(p.key, p.value) for p in sorted_pairs1])
    print()
    
    # Test case 2: Already sorted
    pairs2 = [
        Pair(1, 10),
        Pair(2, 20),
        Pair(3, 30)
    ]
    
    print("Test 2 (already sorted):")
    print("Before sorting:", [(p.key, p.value) for p in pairs2])
    sorted_pairs2 = solution.quickSort(pairs2)
    print("After sorting:", [(p.key, p.value) for p in sorted_pairs2])
    print()
    
    # Test case 3: Reverse sorted
    pairs3 = [
        Pair(5, 1),
        Pair(4, 2),
        Pair(3, 3),
        Pair(2, 4),
        Pair(1, 5)
    ]
    
    print("Test 3 (reverse sorted):")
    print("Before sorting:", [(p.key, p.value) for p in pairs3])
    sorted_pairs3 = solution.quickSort(pairs3)
    print("After sorting:", [(p.key, p.value) for p in sorted_pairs3])
    print()
    
    # Test case 4: Duplicate keys
    pairs4 = [
        Pair(3, 1),
        Pair(1, 2),
        Pair(3, 3),
        Pair(2, 4),
        Pair(1, 5)
    ]
    
    print("Test 4 (duplicate keys):")
    print("Before sorting:", [(p.key, p.value) for p in pairs4])
    sorted_pairs4 = solution.quickSort(pairs4)
    print("After sorting:", [(p.key, p.value) for p in sorted_pairs4])


