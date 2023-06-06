#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            product[i] = product[i-1] * nums[i-1]
        right = 1
        for i in range(len(nums)-2, -1, -1):
            right *= nums[i+1]
            product[i] *= right
        
        return product
    

# Notes (6/5/2023)
# General idea:
# Idea: the product of the array except for the ith element can be
#  calculated by multiplying the prefix and the postfix 
# However, to save the space complexity, we do not even have to have
#  arrays for prefix and postfix 

# time complexity: O(n)
# - iterate through the array twice
#   - calculating the prefixes
#   - calculating the postfixes

# space complexity: O(1)
#   - we are not using extra space as we are calculating the products
#       in the returning array itself

        
# @lc code=end

