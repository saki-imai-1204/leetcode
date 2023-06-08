#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_prof = 0
        while (r < len(prices)):
            if prices[l] <= prices[r]:
                max_prof = max(max_prof, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_prof
        

# Notes (6/7/2023)
# General idea: 
# Sliding window using left and right pointers
# since time moves in one direction (left -> right)

# Algorithm:
# Initialize left pointer all the way to the left, 
# and right pointer one position to the right of left pointer
# While the right pointer is less than the length of the array:
#   If a current left and right pointer is making profit, then no need to change the left pointer 
#       We will calculate the profit and compare with the max profit
#   If a current left and right pointer is making loss, then we will shift the left pointer to where the right pointer is, 
#   Regardless of the case, we will always increment the right pointer by 1

# time complexity: O(n) – using two pointers and going through the list of length n
# space complexity: O(1) – memory for pointers l, r and max_prof

# @lc code=end

