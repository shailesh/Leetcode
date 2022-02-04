class Solution: 
    # we can find these absolute differences much more quickly if we first group by the integer value
    # then prefix sum is used to calculate each interval in O(1) time, giving a total O(n) time complexity
    def getDistances(self, arr: List[int]) -> List[int]:
        m, res = {}, [0] * len(arr)
        for i, v in enumerate(arr):
            if v not in m: m[v] = list()
            m[v].append(i)
            
        for x in m: # iterate through each key in m
            # l is the list of indexes sharing the common integer x
            l = m[x]
            # prefix sum of l, aka the prefix sum all indexes sharing the integer value x
            pre = [0] * (len(l) + 1)
            for i in range(len(l)):
                pre[i + 1] = pre[i] + l[i]
            # given an index v within l, Interval can be found in constant time by:
            # a. absolute difference between index v and all less than v
            # b. absolute difference between index v and all greater than v
            
            # Ex: if the indexes are l = [1, 2, 4, 6] and we want to find abs difference of 4:
            # Brute force would be abs(4 - 1) + abs(4 - 2) + abs(4 - 6) = 3 + 2 + 2 = 7
            
            # Using prefix sum method, we would have:
            # pre = [0, 1, 3, 7, 13], i = 2, v = 4
            # a = (4 * 2) + pre[2] = 8 - 3 = 5
            # b = (pre[4] - pre[2]) - 4 * (4 - 2) = 13 - 3 - 8 = 2
            # a + b = 5 + 2 = 7
            for i, v in enumerate(l):
                a = (v * i - pre[i])
                b = ((pre[len(l)] - pre[i]) - v * (len(l) - (i)))
                res[v] = a + b
        return res