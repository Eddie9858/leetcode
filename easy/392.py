class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_p = 0
        s_p = 0
        while t_p < len(t) and s_p < len(s):
            if t[t_p] == s[s_p]:
                s_p += 1
            t_p += 1

        return s_p == len(s)

# https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/is-subsequence/submissions/1221775126?envType=study-plan-v2&envId=leetcode-75
