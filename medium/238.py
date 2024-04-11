class Solution:
    def productExceptSelf(self, nums):
        length = len(nums)
        answer = [1] * length

        # Calculate the products of all elements to the left of each element
        left_product = 1
        for i in range(length):
            answer[i] = left_product
            left_product *= nums[i]

        # Calculate the products of all elements to the right of each element
        right_product = 1
        for i in reversed(range(length)):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer

# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/product-of-array-except-self/submissions/1229259034?envType=study-plan-v2&envId=leetcode-75
