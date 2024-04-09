class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """



        nums1 = set(nums1)
        nums2 = set(nums2)

        a = [num for num in nums1 if num not in nums2]
        b = [num for num in nums2 if num not in nums1]

        return [a, b]

# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1227530368?envType=study-plan-v2&envId=leetcode-75
