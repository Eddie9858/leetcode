class Solution:
    def reverseVowels(self, s: str) -> str:
        # list for vowels 
        # also can try below but slower
        # vowels = sets("aeiou") 
        vowels = ["a", "e", "i", "o", "u"]
        s = list(s)

        # make an list comprehension contains index of vowels in s
        n_list = [i for word in enumerate(s) if word in vowels]

        for i in range(len(n_list)//2):
            s[n_list[i]], s[n_list[-i-1]] = s[n_list[-i-1]], s[n_list[i]]

        return "".join(s)
  

         
        for i in range(len(n_list)//2):
            s[n_list[i]], s[n_list[-i-1]] = s[n_list[-i-1]], s[n_list[i]]

        return "".join(s)
  
# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/1216148335?envType=study-plan-v2&envId=leetcode-75
