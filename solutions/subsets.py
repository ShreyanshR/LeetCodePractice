from typing import List

class Solution:
    def subsets(self, nums:[int]) -> List[List[int]]:
        res = []
        subs = []

        def dfs(i):
            print(f"Entering dfs({i}), subs = {subs}")
            if i >= len(nums):
                res.append(subs.copy())
                print(f"Base case reached, added {subs}")
                return 
            
            subs.append(nums[i])
            dfs(i+1)
            print(f"After first dfs call, i={i}, subs = {subs}")
            
            subs.pop()
            print(f"After pop, i={i}, subs = {subs}")
            dfs(i+1)
            print(f"After second dfs call, i={i}, subs = {subs}")

        dfs(0)
           

if __name__ == "__main__":
    nums = [1, 2, 3]

    s = Solution()
    s.subsets(nums)

