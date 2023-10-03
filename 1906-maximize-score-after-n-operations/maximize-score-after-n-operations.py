class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}

        def backtrack(index, bit):
            ans = 0
            state = (index, bit)

            if state in memo:
                return memo[state]

            for i in range(len(nums)-1):
                if bit & (1<<i) == 0:
                    for j in range(i+1, len(nums)):
                        if bit & (1<<j) == 0:
                            ans = max(ans, index*(gcd(nums[i], nums[j])) + backtrack(index+1, bit|(1<<i)|(1<<j)))
            
            memo[state] = ans
            return ans
        
        return backtrack(1, 0)
                            
        