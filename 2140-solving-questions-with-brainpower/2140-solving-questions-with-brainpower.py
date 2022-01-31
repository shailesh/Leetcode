class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """
        This is a typical dynamic programming problem.
For each index i we have 2 options:

Take pointsi and jump the next brainpoweri indexes
Skip the current index(do not collect pointsi) and move to the next index
We need to find the maximum points we can collect given the above mentioned constraints

Note: dp[i] denotes the max points that can be collected for the subarray: questions[i... questions.size() - 1]. So we only need to compute it once for each i

Time Complextity: O(n)
Space Complexity: O(n)
        """
        dp = [0] * (len(questions) + 1) 
        for i in range(len(questions) - 1, -1, -1):
            points, jump = questions[i][0], questions[i][1]
            dp[i] = max(points + dp[min(jump + i + 1, len(questions))], dp[i + 1])
        return dp[0];
        