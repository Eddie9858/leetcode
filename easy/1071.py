class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # find GCD
        gcd_length = math.gcd(len(str1), len(str2))

        # GCD algorithm
        # def gcd(a: int, b: int) -> int:
        #     while b:
        #         a, b = b, a % b
        #     return a

        
        
        potential_gcd_str = str1[:gcd_length]
      
        # check potential gcd str is right or not
        if potential_gcd_str * (len(str1) // gcd_length) == str1 and potential_gcd_str * (len(str2) // gcd_length) == str2:
            return potential_gcd_str
        else:
            return ""

# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1215113772?envType=study-plan-v2&envId=leetcode-75
