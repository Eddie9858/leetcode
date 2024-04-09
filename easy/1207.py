class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        element_counts = Counter(arr)
        
        # counts = list(element_counts.values())
        # return len(counts) == len(set(counts))
        
        return len(element_counts.values()) == len(set(element_counts.values()))
            
# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/unique-number-of-occurrences/submissions/1227563120?envType=study-plan-v2&envId=leetcode-75





