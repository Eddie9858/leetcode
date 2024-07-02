class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  
            elif num <= second:
                second = num   
            else:
                return True  
        
        return False  


# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/increasing-triplet-subsequence/submissions/1306934000?envType=study-plan-v2&envId=leetcode-75
