from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subs = []
        

        def add(i):
            ssubs = 0
            if i >= len(candidates):
                return res.append(subs.copy())
            
            #subs.append(candidates[i])
            print(f'Sum before if: {sum(subs)}')


            if ssubs < target:
                subs.append(candidates[i])
                ssubs += candidates[i]
            
            elif ssubs > target:
                subs.pop()
                ssubs -= candidates[i]

            elif ssubs == target:
                res.append(subs.copy())

            print(f'Sum after if: {sum(subs)}')

            add(i+1)
            

        add(0)


if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7

    S = Solution()
    S.combinationSum(candidates, target)