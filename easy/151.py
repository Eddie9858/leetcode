class Solution:
    def reverseWords(self, s: str) -> str:
        # split and make an list
        words = list(s.split(" "))
        # remove an empty space
        words = [word for word in words if word != ""]
        # use python reverse
        words.reverse()

        return ' '.join(words)

  # https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75
  # https://leetcode.com/problems/reverse-words-in-a-string/submissions/1217058786?envType=study-plan-v2&envId=leetcode-75
