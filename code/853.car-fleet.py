#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)

# Notes (6/12/2023)
# Idea: Whether if car will collide with the succeeding car will be 
# determined by the time that the car reaches the destination
# After that, the car speed will be reduced to the succeeding car so that
#  means we can disregard the car 
# It is important that we go through from the end since the car speed of 
# the car depends on the succeeding car

# Algorithm:
# Define a speed and position pair sorted by speed in a reverse order
# Iterate through the elements and calculate the time that it reaches 
# the destination and add the destination time to stack
# If the stack has more than two elements and if the destination time 
# of the top element is less or equal to the second, the pop the first 
# element (indicating that it will be one fleet and we can disregard
#  this car moving on)

# time complexity: O(nlogn) 
# Since we first sort the array and then go through each element to add and pop from the stack

# space complexity: O(n)
# Since we create a stack that we potentially add every item to it

# @lc code=end

