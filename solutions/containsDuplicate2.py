from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        L = 0

        for R in range(len(nums)):
            #this is the simple case where R-L <= k
            #in the other problem it was just greater than K, that's why +1
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True

            window.add(nums[R])

        return False