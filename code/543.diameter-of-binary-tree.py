#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root: return 0
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                res = max(res, left + right)
                return 1 + max(left, right)
        
        dfs(root)
        return res

# Notes (7/2/2023)  
# The diameter of a tree can be calculated by
# Left height + right height
# However, the diameter of a tree is different from the depth of a tree in that we count 1 less for diameter than the depth
# So, we want a function that calculates the left height and the right height -> create a dfs function inside and have a global variable that stores the maximum diameter outside the function

# @lc code=end

