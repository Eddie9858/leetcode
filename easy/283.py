class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0  # Keep track of the last non-zero found.
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt], nums[i] = nums[i], nums[lastNonZeroFoundAt]
                lastNonZeroFoundAt += 1

              
        # initial answer 
        # for i in nums:
        #   if i == 0:
        #     nums.remove(i)
        #     nums.append(i)

              
# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/move-zeroes/submissions/1221717732?envType=study-plan-v2&envId=leetcode-75
