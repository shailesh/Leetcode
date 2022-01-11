class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        We simply need to use the current, and last 2 elements to ensure that the             ordering of elements is turbulent. If we see such a case, then we increment           our count by 1. We start count at 2 if we our current element is not the             previous, as any length 2 array with inequal elements must be turbulent. We           finally have a base case that resets count to 1 if we have a single element           array.
        """
        ret = 0
        cnt = 0

        for i in range(len(arr)):
            if i >= 2 and (arr[i-2] > arr[i-1] < arr[i] or arr[i-2] < arr[i-1] > arr[i]):
                cnt += 1
            elif i >= 1 and arr[i-1] != arr[i]:
                cnt = 2
            else:
                cnt = 1
            ret = max(ret, cnt)
        return ret