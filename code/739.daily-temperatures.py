#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []*len(temperatures)
        stack = [] # temp, index pair
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] > temp:
                t, ind = stack.pop()
                answer[ind] = i - ind
            stack.append([temp, i])
        
        return answer
    
# Notes (6/11/2023)
# Idea: Add the temperatures in stack and if you found a temperature 
# greater than itself, the pop the temperature and append to the 
# corresponding index of the result array
# The stack will be in monotonic decreasing order 
# -> because it will be popped if found a temperature greater than itself
# 
# time complexity: O(n)
# Going through the temperature array one
# 
# space complexity: O(n)
# For defining a stack and a result array of length at most n

# @lc code=end

