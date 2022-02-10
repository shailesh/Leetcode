# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        Put TreeNode into list not their values
Use start and end pointers to avoid recreating new array - saves both time and space complexity
time complexity is O(N)


        """
        def inorder(node, li):
            if not node:
                return
            inorder(node.left, li)
            li.append(node)
            inorder(node.right, li)
        
        def buildBst(li, start, end):
            if not li or start > end:
                return None
            mid = start + (end - start) // 2
            root = li[mid]
            root.left = buildBst(li, start, mid - 1)
            root.right = buildBst(li, mid + 1, end)
            return root
        if not root:
            return None
        nodes = []
        inorder(root, nodes)
        return buildBst(nodes, 0, len(nodes) - 1)