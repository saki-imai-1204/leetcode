#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open, close):
            if open == close == n: res.append("".join(stack))
            if open < n:
                stack.append("(")
                backtrack(open+1, close)
                stack.pop()
            if close < open:
                stack.append(")")
                backtrack(open, close+1)
                stack.pop()
        
        backtrack(0, 0)
        return res

# Notes (6/11/2023)
# Idea: Generate all the set of parentheses recursively by 
# defining a backtracking function inside 
# 
# Algorithm:
# Define a stack and a result list
# In the backtracking function with two parameters openN and closeN, there are basically three different cases
#   If the number of open bracket and close bracket are equal to n
#       Join all the elements in the stack list into a string and append to result
#       “”.join(stack)
#   If the number of open bracket is less than n
#       Append the open bracket
#       Call the backtracking function again with the number of open brackets incremented by 1
#   If the number of closed brackets are less than the number of open brackets
#       Append the close bracket
#       Call the backtracking function again with the number of closed brackets incremented by 1
# Call the backtracking function with parameter openN=0 and closeN=0
# Return the result list

# @lc code=end

