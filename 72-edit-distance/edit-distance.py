class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def dp(i, j):

            if i == len(word1) and j == len(word2):
                return 0

            if i >= len(word1) or j >= len(word2):
                return max(len(word1)-i, len(word2)-j)
            
            
            if word1[i] == word2[j]:
                return dp(i+1, j+1)
            
            return min(1+dp(i, j+1), 1+dp(i+1, j), 1+dp(i+1, j+1))
        
        return dp(0, 0)