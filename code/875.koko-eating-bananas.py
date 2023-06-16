#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hour = 0
            for pile in piles:
                hour += math.ceil(pile/k)
            if hour <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k+1
        
        return res

# Notes (6/15/2023)
# Idea: we know that the result k is in range of 1 <= k <= max(list)
# Run binary search on the number of k

# Tip: to round up the division solution, use math.ceil(a/b)
# While l <= r:
#   If the number of hours taken with a given k <=  target hour (meaning our k is either too large or just right):
#       Then store the minimum number of k
#       Update the right pointer to k - 1
#   Else: 
#       Update the left pointer to k + 1

# time complexity:
# The time complexity of brute force solution (aka solution without binary search): O(max(pile)*p)
# Using binary search, the complexity would be: O(log(max(pile))*p)

# @lc code=end

