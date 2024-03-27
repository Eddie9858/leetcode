class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        m = 0

        for i in range(len(flowerbed)):
            if i < (len(flowerbed)-1) and i > 0:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    m += 1
                    print(m, 1)
            if i == 0 and len(flowerbed) > 2:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    m += 1 
                    print(m, 2)
            if i == len(flowerbed)-1:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    m += 1
                    print(m, 3)

        return m >= n

# https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/can-place-flowers/submissions/1215242583?source=submission-noac
