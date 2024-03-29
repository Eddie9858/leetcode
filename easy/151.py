class Solution:
    def reverseWords(self, s: str) -> str:
        words = list(s.split(" "))
        words = [word for word in words if word != ""]
        words.reverse()

        return ' '.join(words)

  # https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
  # https://leetcode.com/problems/reverse-words-in-a-string/submissions/1217058786?envType=study-plan-v2&envId=leetcode-75
