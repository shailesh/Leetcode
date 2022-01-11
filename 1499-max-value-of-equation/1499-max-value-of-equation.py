class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = deque() # (x, y)
        output = float(-inf)
        
        # Keep dequeue such that first and last element x diff is <= k
        # and elements in descending order
        
        for x, y in points:
            # Get to valid subwindow state of k diff
            while queue and x - queue[0][0] > k:
                queue.popleft()
            
            # For this valid window:
            # Calculate max value using this new value against left window value (aka highest value in the window)
            if queue:
                output = max(output, queue[0][1] + y + x)
            
            # A points worth is y-x, not y for the equation calculation.
            while queue and y-x > queue[-1][1]:
                queue.pop()
            
            queue.append((x,y-x))
        
        return output