class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n = len(recipes)
        # DAG: ingredients --> recipes
        g = defaultdict(list)
        # default indegree is 0
        indegree = defaultdict(int)

        # Create Gragh and add indegree
        for i in range(n):
            for ing in ingredients[i]:
                indegree[recipes[i]] += 1
                g[ing].append(recipes[i])

        # initally queue has all supplies 
        # assuming only ingredients provided
        q = deque(supplies)

        while q:
            curr = q.popleft()
            for nei in g[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        res = []
        # for all recipes, it would have indegree of 0 
        # so that it can be cooked
        for rec in recipes:
            if indegree[rec] == 0:
                res.append(rec)

        return res
        