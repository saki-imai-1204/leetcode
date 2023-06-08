#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        letters = set()
        maxlen = 0
        while r < len(s):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            maxlen = max(maxlen, len(letters))
            r += 1
        return maxlen

# Notes (6/7/2023)
# General idea: left and right pointer again
# Add the chars into a set and keep shifting the right pointer
# If the char is already in a set, 
#   then shift the left pointer and remove the element at str[l] 
#   from the set until the duplicate element disappears from the set
# Check the length of the substring and update the max accordingly

# time complexity: O(n) - we only have to go through the array one

# space complexity: O(n) - we are creating a set of length n

# @lc code=end

