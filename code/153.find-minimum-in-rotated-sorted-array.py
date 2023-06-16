#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])
            
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res

# Notes (6/15/2023)
# Idea: We want to figure out if a mid value belongs to the left
# portion of the sorted array or the right portion
# If the mid number is greater than the left number,
#   then the middle index belong to the left portion of the array
# Else
#   then the middle index belong to the right portion of the array

# time complexity: log n -- binary search

# @lc code=end

