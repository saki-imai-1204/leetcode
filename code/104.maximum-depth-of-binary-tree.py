#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS Solution
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        # BFS Solution
        if not root: return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return level
    
        # Iterative DFS Solution
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(depth, res)
                stack.append([node.left, depth+1])
                stack.append([node,right, depth+1])
        return res

# Notes (6/18/2023)
# DFS solution:
# For each root, if the root is None then return 0
# If not, return 1 + max(self.func(root.left), self.func(root.right))
# time complexity: O(n)
# space complexity: O(n) – equals to the height of the tree

# BFS solution:
# Use a queue and keep a count for the levels

# Iterative DFS solution:
# Use stack that stores the node and its depth
#   pop the top element and if that node is not None, then 
#       Update the maximum depth
#       add its child nodes

# @lc code=end

