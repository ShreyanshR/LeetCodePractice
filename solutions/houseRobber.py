from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        #rob1, rob2, n, n+1

        """
        so we do a temp var that max b/w rob1 + n, and  rob
        then rob1 is shifted to rob 2
        and rob2 is shifted to the max
        1,1,3,1

        
        """

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2


if __name__ == "__main__":
    nums = [1, 1, 3, 3]
    nums1 = [2,9,8,3,6]
    nums2=[5,1,2,10,6,2,7,9,3,1]

    S= Solution()

    print(S.rob(nums2))
    print("_"*20)
    print(S.rob(nums1))

