from collections import defaultdict
from typing import List

class Solution:
    def topKFreq(self, nums: List[int], k:int) -> List[int]:
        t = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            t[num] = 1 + t.get(num, 0)

        for num, count in t.items():
            freq[count].append(num)
        
        print(freq)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                print(i,n)
                res.append(n)
                print(res)
                if len(res) == k:
                    return res


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    S = Solution()
    S.topKFreq(nums, k)