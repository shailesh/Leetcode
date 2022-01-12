class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        g = defaultdict(list)
        for i in range(1, len(prevRoom)):
            g[prevRoom[i]].append(i)
        mod = 10 ** 9 + 7

        def dfs(i):
            number_of_edges = 0
            res = 1
            for j in g[i]:
                number_of_child_edges, number_of_perm = dfs(j)
                number_of_edges += number_of_child_edges
                res = (res * comb(number_of_edges, number_of_child_edges) * number_of_perm) % mod
            return (number_of_edges + 1, res)

        return dfs(0)[1]