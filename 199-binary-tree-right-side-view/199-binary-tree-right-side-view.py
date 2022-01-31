# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        we need to somehow traverse our tree, using dfs (inorder, preorder or postorder) or bfs. I use almost inorder traversal, with just one small change: instead of going Left -> Node -> Right, we will go Right -> Node -> Left. In this way we first visit nodes on the right side of our tree. Algorithm will look like this:

Create ans dictionary, which for each level H will keep the rightest node.
Traverse tree: first visit right children and if we do not have this H in ans yet, we put it there, then visit left children. Note again that with this order of traversal we always will put the rightest node for each level and next time we visit this level we will do nothing.
Finally, create list from our dictionary.
Complexity: time complexity is O(n) for classical dfs, space is O(h), again classical complexity for dfs as well as this amount of space we need to keep in our answer.

Since dictionaries are ordered, we can store the rightmost nodes in order and just return the dict values. Just a minor tweak
        """
        ans = {}
        def dfs(node, H):
            if not node: return 
            
            if H not in ans: ans[H] = node.val
            dfs(node.right, H + 1)
            dfs(node.left, H + 1)
            
        dfs(root, 0)
        return ans.values()
        