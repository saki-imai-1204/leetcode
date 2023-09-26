#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    # Solution 1
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum(): newstr += c.lower()
        return newstr == newstr[::-1]

    # Solution 2
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphanum(s[l]): l += 1
            while l < r and not self.alphanum(s[r]): r -= 1
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True
    
    def alphanum(self, char):
        return ord('a') <= ord(char.lower()) <= ord('z') or \
                ord('0') <= ord(char) <= ord('9')
    

# Notes (6/5/2023)
# Solution 1: Use built-in string methods
# Create a new string that adds non-alphanumeric numbers using following functions
# isalnum() – returns True if all characters in the string are alphanumeric (either alphabets or numbers)
# str == str[::-1] – to check if it is a palindrome
# time complexity: O(n) - for iterating through a string once
# space complexity: O(n) for creating a new string of size n

# Solution 2: O(1) space complexity solution
# Use ascii values to determine if a character is alphanumeric or not
# Use two pointers
# time complexity: O(n) - for iterating through a string once with pointer l and r
# space complexity: O(1) - space used for variables l and r

# @lc code=end

