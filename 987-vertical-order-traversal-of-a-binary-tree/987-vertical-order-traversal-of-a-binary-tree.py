# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        vertical_levels = collections.defaultdict(list)
        def dfs(node,x=0,y=0):
            if node is None: return None
            dfs(node.left  ,x-1,y+1)
            dfs(node.right ,x+1,y+1)
            vertical_levels[x].append([y,node.val])
            
        dfs(root)
        return [[node_value for y_value,node_value in sorted(values)] for x_value,values  in sorted(vertical_levels.items())]