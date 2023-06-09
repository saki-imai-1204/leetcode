#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        else:
            tmp = root.right
            root.right = self.invertTree(root.left)
            root.left = self.invertTree(tmp)
            return root

# Notes (6/8/2023)
# Visit every node and swap its left and right root
# Call the same function again to its left and right subtrees
# Base case – if the root is None then return None

# @lc code=end

