class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        Explanation: Suppose we already have array of prefix sum, and we are at index i-th of prefix_sum. There are two possible ways to find maximum result:
(1) maxL + the last sum of nums's subarray of length == secondLen. maxL:= maximum sum of nums's subarray of length == firstLen, before the ending at i, and the last subarray with length == secondLen.

(2) maxM + the last sum of nums's subarray of length == firstLen. maxM:= maximum sum of nums's subarray of length == secondLen, before the ending at i, and the last subarray with length == firstLen.

Complexity: Time O(N), N is len(nums). Space O(1)
        """
        if len(nums) < firstLen + secondLen: return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        res, maxL, maxM = nums[firstLen + secondLen - 1], nums[firstLen - 1], nums[secondLen - 1]
        for i in range(firstLen + secondLen, len(nums)):
            maxL = max(maxL, nums[i - secondLen] - nums[i - secondLen - firstLen])
            maxM = max(maxM, nums[i - firstLen] - nums[i - firstLen - secondLen])
            res = max(res, maxL + nums[i] - nums[i - secondLen], maxM + nums[i] - nums[i - firstLen])
        return res
        