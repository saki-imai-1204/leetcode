#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
            

# Notes (6/6/2023)
# General idea:
# Use two pointers
# If the sum of the two pointers is less than the target, shift the left pointer to the right
# If the sum of the two pointers is greater than the target, shift the right pointer to the left
# Else, return the pointers +1

# time complexity: O(n)
# - potentially iterate through the array once

# space complexity: O(1)
#   - memory for variables l and r
# @lc code=end

