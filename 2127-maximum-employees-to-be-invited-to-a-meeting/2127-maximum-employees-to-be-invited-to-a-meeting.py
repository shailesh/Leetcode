class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        # ***PART 1: cycle decomposition to get the maximum cycle length + collect 2-cycles + reverse edges for BFS later***
        n = len(favorite)
        reversed_edges, visited, two_cycle_nodes = defaultdict(list), {}, []
        max_cycle_length = 0
        for person in range(n): # NOTE: need to keep track of a path_index, since you may run into a loop in the middle
            reversed_edges[favorite[person]].append(person)
            path_indices, path_index = {}, 1
            curr = person
            while curr not in visited:
                visited[curr], path_indices[curr] = 1, path_index
                path_index += 1
                curr = favorite[curr]
            if curr in path_indices and path_indices[curr] > 0:
                cycle_length = path_index - path_indices[curr]
                max_cycle_length = max(max_cycle_length, cycle_length)
                if cycle_length == 2: # append both nodes
                    two_cycle_nodes.append(curr) 
                    two_cycle_nodes.append(favorite[curr])
                    
        # ***PART 2: BFS on all 2-cycle starts using reversed edges to get all extensions***
        two_cycle_extension_total = 0
        def bfs(start): # returns maximum NON-CYCLE path length, including start
            ans = 1
            visited = {}
            forbidden = favorite[start]
            q = deque([(start, 1)])
            while q:
                node, level = q.popleft() # assumed unvisited
                visited[node] = 1
                if node != forbidden:
                    ans = max(ans, level)
                    for neighbor in reversed_edges[node]:
                        if neighbor not in visited:
                            q.append((neighbor, level+1))
            return ans
        
        for partner in two_cycle_nodes:
            two_cycle_extension_total += bfs(partner)
            
        # ***ANSWER: max of (maximum cycle length) and (sum of all 2-cycles with extensions)***
        return max(max_cycle_length, two_cycle_extension_total)