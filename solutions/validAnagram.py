class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1, t1 = {}, {}

        for i in range(len(s)):
            s1[s[i]] = 1 + s1.get(s[i], 0)
            t1[t[i]] = 1 + t1.get(t[i], 0)

        return s1 == t1



if __name__ == "__main__":
    s = "racecar"
    t = "carracx"

    S = Solution()
    print(S.isAnagram(s,t))