#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev:
                return [i, prev[diff]]
            prev[nums[i]] = prev.get(nums[i], i)
 

# Notes (6/5/2023)
# General idea:
# Use hashmap to store the key: numbers, values: indices pair.
# For each entry, check if the other pair that sum to the target exists in the hashmap.

# time complexity: O(n)
# - iterate through the array once
#   - adding an element to the hashmap: O(1)
#   - checking if a value exists in a hashmap: O(1)

# space complexity: O(n)
#   - we can potentially add all the elements to the hashmap


# @lc code=end

