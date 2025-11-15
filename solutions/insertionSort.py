#Definition for a pair.

from typing import List

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res: List[List[Pair]] = []
        for i in range(1, len(pairs)):
            key_pair = pairs[i]
            j = i - 1

            while j>=0 and key_pair.key < pairs[j].key:
                pairs[j+1] = pairs[j]
                #when we do this j-1, we get the previous position,
                #so when it does for j=0, for j becomes -1, and pairs(-1+1) = pairs[0] get swaped with the smalest element
                j -= 1

            pairs[j+1] = key_pair #this is the ith element that got switched

            res.append(pairs.copy())

        return res


def format_pairs_list(pairs_list):
    """Helper function to format output for display"""
    result = []
    for item in pairs_list:
        if isinstance(item, Pair):
            result.append(f"({item.key}, '{item.value}')")
        elif isinstance(item, list):
            pair_strs = [f"({p.key}, '{p.value}')" for p in item]
            result.append("[" + ", ".join(pair_strs) + "]")
    return result


if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Unsorted pairs
    print("Test 1: Unsorted pairs")
    pairs1 = [
        Pair(3, "third"),
        Pair(1, "first"),
        Pair(2, "second")
    ]
    print("Input pairs:")
    for p in pairs1:
        print(f"  ({p.key}, '{p.value}')")
    result1 = solution.insertionSort(pairs1)
    print("Result steps:")
    for step in format_pairs_list(result1):
        print(f"  {step}")
    
    # Test case 2: Reverse sorted
    print("\nTest 2: Reverse sorted pairs")
    pairs2 = [
        Pair(5, "five"),
        Pair(3, "three"),
        Pair(1, "one")
    ]
    print("Input pairs:")
    for p in pairs2:
        print(f"  ({p.key}, '{p.value}')")
    result2 = solution.insertionSort(pairs2)
    print("Result steps:")
    for step in format_pairs_list(result2):
        print(f"  {step}")
    
    # Test case 3: Already sorted
    print("\nTest 3: Already sorted pairs")
    pairs3 = [
        Pair(1, "one"),
        Pair(2, "two"),
        Pair(3, "three")
    ]
    print("Input pairs:")
    for p in pairs3:
        print(f"  ({p.key}, '{p.value}')")
    result3 = solution.insertionSort(pairs3)
    print("Result steps:")
    for step in format_pairs_list(result3):
        print(f"  {step}")