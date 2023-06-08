#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        maxlen = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            maxlen = max(maxlen, r-l+1)

        return maxlen

# Notes (6/7/2023)
# Main idea: for each given sliding window, calculate the number of the 
#   most frequent character count and subtract that number from the length of the window
# If the difference is less than or equal to k, then update the max length
# If not, slide the left pointer to the left
# time complexity of this approach: O(26*n)


# More sophisticated idea: we actually do not need to update the most frequent 
# character count for every sliding window (decrementing the count), 
# but simply keep the most frequent character at any given time
# Because what we are essentially calculating is length - maxF <= k 
# and this will not improve unless the count increases

# time complexity: O(n)

# @lc code=end

