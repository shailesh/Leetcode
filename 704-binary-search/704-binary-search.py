class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        I search in the bounded interval, so that's why setting right pointer as len(nums) - 1.
Every time compare target value with middle value, we move the the pointers. But next interval is also bounded, which not including middle. That's why mid-1 and mid+1.

Time complexity of binary search is O(logN), where N is length of nums.
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l+(r-l)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
        return -1
                
        