#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = 0
        maxl, maxr = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                maxl = max(maxl, height[l])
                ans += maxl - height[l]
            else:
                r -= 1
                maxr = max(maxr, height[r])
                ans += maxr - height[r]
            
        return ans


# Notes (6/6/2023)
# Solution 1: with space complexity O(n)
# Idea: the amount of water that can be trapped at spot i is calculated by min(l, r)-h[i] where l is the max height on the left of i and r is the max height on the right of i
# Use arrays to store the maxleft, maxright, and min(l, r)
# Then, compute min(l, r)-h[i]

# Solution 2: with space complexity O(1)
# Idea: We don’t really have to store the maxL and maxR because all we need is the minimum of the two so if we have pointers on both sides and if one pointer is smaller than the other then we will take that as a min(l, r)
# Take two pointers l, r
# While l  < r:
#   Increment l if max[l] < max[r]
#   Decrement r if max[l] < max[r]
#   The calculation of res is done after the leftmax, rightmax is updated

# time complexity: O(n) -- iterating through the list of length n once

# space complexity: O(1) -- memory for pointers maxl, maxr and ans

# @lc code=end

