#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif not p or not q: return False
        else:
            return self.isSameTree(p.left, q.left) and \
                    self.isSameTree(p.right, q.right) and \
                    p.val == q.val


# Notes (6/28/2023)
# Base cases we want to consider:
#   If both trees are null, then true
#   If one of the trees are null or if the values do not match, then false
# Recursive step:
#   If the p’s left subtree and q’s left subtree is the same AND 
#   If the p’s right subtree and q’s right subtree is the same 

# time complexity: O(p+q) 
#   Because in the worst case we have to visit every single nodes

# @lc code=end

