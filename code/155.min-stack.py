#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        min_val = min(val, self.min[-1] if self.min else val)
        self.min.append(min_val)
        self.stack.append(val)

    def pop(self) -> None:
        self.min.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Notes (6/10/2023)
# General idea:
# Keep two stacks to keep track of the numbers added to stack,
# as well as the minimum of the stacks
# 
# @lc code=end

