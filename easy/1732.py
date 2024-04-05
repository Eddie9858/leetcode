class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alti = 0
        max_al = 0
        for i in gain:
            alti += i
            max_al = max(alti, max_al)

        return max_al

# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/find-the-highest-altitude/submissions/1223537021?envType=study-plan-v2&envId=leetcode-75
