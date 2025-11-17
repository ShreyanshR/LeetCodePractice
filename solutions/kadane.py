from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curS = 0
        
        for num in nums:
            curS = max(curS, 0) #we reset to 0, if the curSum is negative
            curS += num
            maxSum = max(curS, maxSum)

        return maxSum