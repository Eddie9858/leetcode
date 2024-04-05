class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = 0

        for i in range(len(nums)):
            
            left = sum(nums[:i])
            right = sum(nums[i+1:])

            if left == right:
                return i
        if left != right:
            return -1

# https://leetcode.com/problems/find-pivot-index/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/find-pivot-index/submissions/1223551781?envType=study-plan-v2&envId=leetcode-75
