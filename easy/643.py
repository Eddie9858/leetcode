class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # use Sliding Window Technique pass the time limit
      
        for i in range(len(nums) - k):
            window_sum = window_sum - nums[i] + nums[i+k]
            max_sum = max(max_sum, window_sum)

        return max_sum / k

        # This will not pass the time limit 
        # window_sum = []
        # for i in range(len(nums)):
        #     if i+k < len(nums)+1:
        #         window_sum.append(sum(nums[i:i+k]))
        # print(window_sum)
        # return max(window_sum) / k
      

  # https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75
  # https://leetcode.com/problems/maximum-average-subarray-i/submissions/1222815992?envType=study-plan-v2&envId=leetcode-75
