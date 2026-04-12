# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if n == 0:
            return []
        
        def build(start, end):
            if start > end:
                return [None]
            
            trees = []
            
            for root in range(start, end + 1):
                left_trees = build(start, root - 1)
                right_trees = build(root + 1, end)
                
                for l in left_trees:
                    for r in right_trees:
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        trees.append(node)
            
            return trees
        
        return build(1, n)