import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r

        while l<=r:
            hours = 0
            k = (l+r)//2

            for p in piles:
                hours += math.ceil(p/k)
            
            if hours <= h:
                #we are eating to fast
                res = k
                r = k - 1
            else:
                #eating too slow
                l = k + 1

        return res