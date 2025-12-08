class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1, s2 = {}, {}

        for i in range(len(s)):
            s1[s[i]] = 1 + s1.get(s[i], 0)
            #print(s1)
            s2[t[i]] = 1 + s2.get(t[i], 0)

        return s1 == s2

if __name__ == "__main__":

    s = "racecar"
    t = "carrace"

    S = Solution()
    S.isAnagram(s,t)