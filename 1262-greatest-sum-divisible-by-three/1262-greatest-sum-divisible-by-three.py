class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        Explanation
        dp[0] = largest sum which is divisible by 3
        dp[1] = largest sum when divided by 3, remainder = 1
        dp[2] = largest sum when divided by 3, remainder = 2


        Complexity
        Time O(N)
        Space O(1)

        """
        dp = [0, 0, 0]
        for a in nums:
            for i in dp[:]:
                dp[(i + a) % 3] = max(dp[(i + a) % 3], i + a)
        return dp[0]