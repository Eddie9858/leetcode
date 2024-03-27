class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dict for adding num_to_index
        num_to_index = {}
        for i, num in enumerate(nums):
            # target - num to find the number we are looking for 
            # unless need to use two for loops 
            complement = target - num
            # if there is answer of complement in dict return it
            if complement in num_to_index:
                return [num_to_index[complement], i]
            # if not add it to the dict
            num_to_index[num] = i
          
# https://leetcode.com/problems/two-sum/
# https://leetcode.com/problems/two-sum/submissions/1215091038
