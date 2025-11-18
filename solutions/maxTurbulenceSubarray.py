from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0, 1
        res, prev = 1, ""

        while r < len(arr):
            if arr[r-1] > arr[r] and prev != ">":
                """previous sign or begin is not the samee, so we move the right pointer by 1, and updatre the sign"""
                res = max(r-l+1, res)
                r += 1
                prev = ">"

            elif arr[r-1] < arr[r] and prev != "<":
                """we do the same thing here, checking he adjacent ones"""
                res = max(r-l+1, res)
                r += 1
                prev = "<"

            else:
                """checking if r and r-1 values are equal, and if they are we move to r+1, but if not, that means
                it can be subarrary, so we just restart again
                """
                r = r + 1 if arr[r-1] == arr[r] else r
                l = r - 1
                prev = ""

        return res