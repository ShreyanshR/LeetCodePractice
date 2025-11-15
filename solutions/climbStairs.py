class Solution:
    def climbStairs(self, n: int) -> int:
        #print(f"Calculating for n={n}")
        one, two = 1, 1

        for i in range(n-1):
            #we just recursively add one & two
            #and we shift two to one
            #but as we update two, we have to store it in temp
            """as it's always 1 or two step, both the last recursive steps become the base case
            we just recursively add them afterwards. It's an easy problem but a tricky one to find
            code logic
            """
            temp = one
            one = one + two
            two = temp

        return one



if __name__ == "__main__":
    S = Solution()
    S.climbStairs(6)