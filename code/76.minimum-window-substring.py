#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        t_dict, window = {}, {}
        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)

        need, have = len(t), 0
        l = 0
        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in t_dict and t_dict[c] >= window[c]:
                have += 1

            while need == have:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in t_dict and window[s[l]] < t_dict[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""


# Notes (6/9/2023)
# General idea:
# Keep a dictionary for both the substring and a current window
# Use a sliding window l, r
# Iterate through string s with a right pointer of the sliding window
#   Add the character at the right pointer to the window dictionary
#   Check if the character is in the substring dictionary as well as
#       if the number of characters in the substring dictionary is 
#       more or equal to the current count 
#   While the number of characters in the substring is equal to the 
#   number of characters that satisfies the condition in the window,
#   slide the window to the right (by shifting the left pointer &
#   removing the character from the window dictionary)
# 
# time complexity: O(n) 
# 
# space complexity: O(n) -- two dictionaries of size at most n
         
# @lc code=end

