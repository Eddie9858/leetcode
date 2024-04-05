class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # left = 0
        # right = 0

        # for i in range(len(nums)):
            
        #     left = sum(nums[:i])
        #     right = sum(nums[i+1:])

        #     if left == right:
        #         return i
        # if left != right:
        #     return -1
        # code above will mostly fail beacuse of runtime limit
        
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        
        return -1

# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/find-pivot-index/submissions/1223551781?envType=study-plan-v2&envId=leetcode-75
