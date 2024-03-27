class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = [True if i + extraCandies >= max(candies) else False for i in candies]
        return result

  # https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/?submissionId=1215140003
  # https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1215144045?submissionId=1215140003
