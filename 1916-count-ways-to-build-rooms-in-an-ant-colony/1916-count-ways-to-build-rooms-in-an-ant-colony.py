class Solution:
    def waysToBuildRooms(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(arr):
            g[pre].append(cur)
            
        def dfs(cur):
            if not g[cur]:
                return 1, 1
            ans, l = 1, 0
            for nxt in g[cur]:
                tmp, r = dfs(nxt)
                ans = (ans * tmp * math.comb(l+r, r)) % MOD
                l += r
            return ans, l + 1
            
        return dfs(0)[0]