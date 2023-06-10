#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if i == "+":
                    stack.append(num1 + num2)
                elif i == "-":
                    stack.append(num1 - num2)
                elif i == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
        return stack[0]

# Notes (6/10/2023)
# General idea:
# Use stack to add values and store the results
# 

# time complexity: O(n)
# - iterate through the tokens of size n

# space complexity: O(n)
#   - stack of size at most n
        
# @lc code=end