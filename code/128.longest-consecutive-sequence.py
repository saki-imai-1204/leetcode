#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0
        for num in nums:
            if num-1 not in numset:
                k = 1
                while num + k in numset:
                    k += 1
                ans = max(ans, k)
        return ans
    
    
# Notes (6/5/2023)
# General idea:
# Convert a list of numbers into a set
# (since sets are significantly faster when it comes to determining if an object is present in the set)
# For each number in a list, detect if number is a start of a sequence or not 
#   (can be checked by seeing if there is a number that comes before the number in a set)
#   If it is, then count the length of the sequence and store if it is greater than the current max

# time Complexity: O(n) - we are visiting each element at most twice

# space Complexity: O(n) - since we created a set which uses additional memory

        
# @lc code=end

