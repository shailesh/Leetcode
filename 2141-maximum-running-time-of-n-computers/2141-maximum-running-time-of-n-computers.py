class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        """
        We should look at the n biggest batteries.

We can deal with the rest of battaries as with one big battery, call it accumulator.
What we need to do now is binary search: ask question: given x, can we survive x time. For each batery which is >= x, we are OK. For smaller battaries we need to use our accumulator.
Complexity
It is O(n log M) for time and O(n) for space.
        """
        batteries = sorted(batteries)[::-1]
        small = sum(batteries[n:])
        beg, end = 0, sum(batteries) + 1
        while beg + 1 < end:
            mid = (beg + end)//2
            to_do = sum(max(mid - x, 0) for x in batteries[:n])
            if to_do > small:
                end = mid
            else:
                beg = mid
        return beg
        