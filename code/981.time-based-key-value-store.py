#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#

# @lc code=start
class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# Notes (6/22/2023)
# 
# Idea: the time stamps are in ascending order
# So, we do not think about sorting the list when adding them, we simply have to append to the last element of the list and the list will be automatically sorted
# Given a key, we will run a binary search
# While l <= r:
# If the element at the middle index is less than or equal to the target timestamp, 
# then we will store the value since it is valid
# Update the left pointer to mid + 1
# Else
# It is invalid so we will simply update the right pointer to mid - 1
# Return the value

# time complexity: O(log n) 

# @lc code=end

