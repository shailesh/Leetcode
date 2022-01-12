class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Fix one of the pointers at index i then do the typical two-sum problem with           indices j and k on the remaining elements that is not at index i. After i             loops through the entire array once or when you find a difference of 0, then         you have the 3sum solution.
        """
        nums = sorted(nums)
        smallestDiff = 10001
        closestSum = 0
        
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                threeSum = nums[i] + nums[j] + nums[k]
                if abs(threeSum - target) < smallestDiff:
                    smallestDiff = abs(threeSum - target)
                    closestSum = threeSum 
                if threeSum < target:
                    j += 1
                elif threeSum > target:
                    k -= 1
                else:
                    return threeSum
        return closestSum
        