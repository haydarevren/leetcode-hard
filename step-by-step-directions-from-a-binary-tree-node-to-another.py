# 2096. Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findPath(node, targetValue, path):
            
            if (node.val == targetValue):
                return True

            # then recur on left subtree
            if node.left and findPath(node.left, targetValue, path):
                path += ["L"]
            # then recur on right subtree
            elif node.right and findPath(node.right, targetValue, path):
                path += ["R"]

            return path

        path_start, path_dest = [], []
        findPath(root, startValue, path_start)
        findPath(root, destValue, path_dest)
        
        def convertDirections(path_start, path_dest):
            while path_start and path_dest and path_start[-1]== path_dest[-1]:
                path_start.pop()
                path_dest.pop()
                
            return "".join("U"*len(path_start)) + "".join(reversed(path_dest))
                
        return convertDirections(path_start, path_dest)
