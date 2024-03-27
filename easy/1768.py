class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # find shorter length for merge
        shorter_len = min(len(word1), len(word2))
        # merge word1 and word2
        merged_part = [word1[i] + word2[i] for i in range(shorter_len)]
        # join merged_part and add shorter length of word1 or word2
        return ''.join(merged_part) + word1[shorter_len:] + word2[shorter_len:]

# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75
# https://leetcode.com/problems/merge-strings-alternately/submissions/1215093484?envType=study-plan-v2&envId=leetcode-75
