#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}
        for char in s:
            if not stack: stack.append(char)
            else:
                if char not in pairs: 
                    stack.append(char)
                elif stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
        return not stack

# Notes (6/10/2023)
# General idea:
# Use a stack to keep track of parantheses and a dictionary to
# store the valid parantheses pairs
# 
# 
# time complexity: O(n) - going through a parantheses of length n
# 
# space complexity: O(n) -- stack of size at most n, constant memory for the dictionary
# @lc code=end

