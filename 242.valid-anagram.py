#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1
        return sorted(s) == sorted(t)
    
        # Time complexity: O(n log n) -- using a sorting algorithm such as quick sort
        # Space complexity: O(1) -- under the assumption that sorting does not take any extra space
    
        # Solution 2
        if len(s) != len(t): return False
        s_char, t_char = {}, {}
        for i in range(len(s)):
            s_char[s[i]] = s_char.get(s[i], 0) + 1
            t_char[t[i]] = t_char.get(t[i], 0) + 1
        
        for i in range(len(s)):
            if s_char[s[i]] != t_char.get(s[i], 0): return False
        return True
    
        # Time complexity: O(n)
        #   - iterating through the string s, t with length n 
        #       - adding a character count to the hashset: O(1)
        #   - iterating through the string s with length n
        #       - checking if the character counts are equal O(1)
    
# @lc code=end

