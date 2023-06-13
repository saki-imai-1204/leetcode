#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)

    def binary_search(self, nums, target, left, right):
        if left > right: return -1
        mid = left + (right - left) // 2
        if nums[mid] == target: return mid
        elif nums[mid] > target: return self.binary_search(nums, target, left, mid-1)
        else: return self.binary_search(nums, target, mid+1, right)
    
# time complexity - O(log n)
# In each iteration of the binary search, the algorithm reduces the 
# search space by half. It compares the target value with the middle 
# element and determines whether to search in the left half or the right 
# half of the array. 
# By repeatedly dividing the search space in half, the algorithm can 
# quickly converge to the target element.
# @lc code=end

