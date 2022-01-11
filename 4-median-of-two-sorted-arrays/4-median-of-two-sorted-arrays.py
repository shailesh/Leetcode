class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = sorted(nums1+nums2)
        return median(l1)
        