class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        s = list(s)
        n_list = []

        for i, word in enumerate(s):
            if word.lower() in vowels:
                n_list.append(i)

        for i in range(len(n_list)//2):
            s[n_list[i]], s[n_list[-i-1]] = s[n_list[-i-1]], s[n_list[i]]

        return "".join(s)
  
# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1216148335?envType=study-plan-v2&envId=leetcode-75
