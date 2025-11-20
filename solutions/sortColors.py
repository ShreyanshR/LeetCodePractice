from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        for n in nums:
            count[n] += 1

        i = 0

        """
        This is the crucial part of the code, we iterate through the whole range so for ex: 0, 1, 2
        then we count how many instances of n are there, and add it to the original array
        note that the j is doing nothing because it's just to iterate through loop
        """
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i += 1

        return nums