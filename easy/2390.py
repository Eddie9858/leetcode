class Solution:
    def removeStars(self, s: str) -> str:
        a = []

        for i in s:
            if i == '*':
                a.pop()
            else:
                a.append(i)

        return ''.join(a)

  # https://leetcode.com/problems/removing-stars-from-a-string/?envType=study-plan-v2&envId=leetcode-75
  # https://leetcode.com/problems/removing-stars-from-a-string/submissions/1229121736?envType=study-plan-v2&envId=leetcode-75
