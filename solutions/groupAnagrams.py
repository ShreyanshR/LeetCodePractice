from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for sen in strs:
            key = "".join(sorted(sen))
            res[key] = [sen] + res.get(key, [])

        return list(res.values())

    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #so that it gives default value if the key doesn't exist

        for s in strs:
            count = [0] * 26 # for a to z , 26 char values

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        
        return res.values()

