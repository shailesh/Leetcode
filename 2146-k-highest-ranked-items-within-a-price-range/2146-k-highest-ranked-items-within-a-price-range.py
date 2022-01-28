class Solution:
    def highestRankedKItems(self, grid: List[List[int]], pricing: List[int], start: List[int], k: int) -> List[List[int]]:
        """
        This is a BFS solution.
First, we want to calculate the distance from the start position for every reachable grid. After getting the distance, we just put the tuple data (distance, price, row, col) into a list, and just sort. This automatically sorts the data into desirable order. Note that the (distance == infinity) means that the cell in not reachable from the start position and we don't want to include that in the answer.

Time: O(NlogN) (N = R * C)
Space: O(N)
        """
        def in_range(i, j):
            return 0 <= i < R and 0 <= j < C and grid[i][j] != 0
        
        R, C = len(grid), len(grid[0])
        dist = [[float('inf') for _ in range(C)] for _ in range(R)]
        
        queue = deque()
        queue.append((0, start))
        dist[start[0]][start[1]] = 0
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        get_items = 0
        farthest_dist = 0
        dist_dict = defaultdict(list)
        low, high = pricing
        
        while queue:
            curr_dist, (i, j) = queue.popleft()
            if grid[i][j] != 1 and low <= grid[i][j] <= high:
                get_items += 1
                dist_dict[curr_dist].append((grid[i][j], i, j))
                if get_items == k:
                    farthest_dist = curr_dist
            if farthest_dist != 0 and curr_dist > farthest_dist:
                break
            for move_i, move_j in moves:
                new_i, new_j = i + move_i, j + move_j
                if in_range(new_i, new_j) and dist[new_i][new_j] == math.inf:
                    dist[new_i][new_j] = curr_dist + 1
                    queue.append((curr_dist + 1, (new_i, new_j)))
        
        res = []
        cnt = 0
        
        for d in sorted(dist_dict.keys()):
            data = dist_dict[d]
            for price, i, j in sorted(data):
                res.append([i, j])
                cnt += 1
                if cnt == k:
                    return res
        return res
        