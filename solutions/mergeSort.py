from typing import List

class Pair:
    def __init__(self, key:int, val:str):
        self.key = key
        self.val = val

class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        #print(pairs)
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs, start, end):
        if end - start + 1 <= 1:
            return

        middle =(start+end)//2

        self.mergeSortHelper(pairs, start, middle) #these just returns update value of pairs in place, in fucking place
        self.mergeSortHelper(pairs, middle+1, end)

        self.merge(pairs, start, middle, end)

        return pairs

    def merge(self, pairs, start, middle, end):
        L = pairs[start : middle + 1] #ahh this is not the pairs sliced, it's the same initial array, so it replaces inplace
        R = pairs[middle + 1 : end + 1]

        i, j = 0, 0
        k = start

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1

            k += 1

        """
        when one of the arrays is finished then we will add the rest of the arrray recursiverly
        and it will not create a asymettery, because we are dividing by 2
        """

        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1


        return pairs 
        
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Unsorted pairs
    print("Test 1: Unsorted pairs")
    pairs1 = [
        Pair(3, "third"),
        Pair(1, "first"),
        Pair(2, "second"),
        Pair(4, 'four')
    ]

    pair = solution.mergeSort(pairs1)

    for i in range(len(pair)):
        print(f'{pair[i].key, pair[i].val}')
