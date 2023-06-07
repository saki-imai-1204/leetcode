#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height)-1
        while l < r:
            res = max(res, min(height[l], height[r])*(r-l))
            if height[l] < height[r]: l += 1
            else: r -= 1
        return res


# Notes (6/6/2023)
# Idea 1: Brute force
# O(n^2) – runtime exceeded

# Idea 2: Use two pointers
# While left pointer < right pointer:
#   Compute the area and store the max area
#   Increment the left pointer if the left pointer height is smaller than the right pointer height
#   Else, decrement the right pointer

# time complexity: O(n)

# space complexity: O(1) -- memory for pointers l and r
        
# @lc code=end

