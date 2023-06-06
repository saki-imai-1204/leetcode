#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # solution 1
        # return len(nums) != len(set(nums))
    
        # solution 2
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
    

# Notes (6/5/2023)
# General idea:
# Solution 1: if the length of set is equal to the length of list then the values are unique

# Solution 2: create a hashset and check if an element is already in the set or not

# time complexity: O(n)
# - iterate through the array of length n once
#   - checking if a value exists in a hashmap: O(1)
#   - adding an element to the hashset: O(1)

# space complexity: O(n)
#   - we can potentially add all the elements to the hashmap

# @lc code=end

