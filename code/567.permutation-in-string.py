#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: return True
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]: matches += 1
            elif s1Count[index] + 1 == s2Count[index]: matches -= 1
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]: matches += 1
            elif s1Count[index] == s2Count[index] + 1: matches -= 1
            l += 1

        return matches == 26

# Idea: Take a sliding window as long as the length of the s1 string. 
#   Do not need to update hashmap every time but can simply disregard the 
#   left most character and regard the new right most character for every 
#   shift, and check the number of matches of the hashmap/array
#       If the matches are 26, then that means it is a permutation

# Algorithm:
# Put two strings into hashmap or an array
# Count the number of matches
# Shift the sliding window up until the end of s2 string
#   Check the number of matches
#   Calculate the index of the left and the right of window and update it
#    on the hashmap
#   Update the count of number of matches

# time Complexity: O(n) - single iteration of string

# @lc code=end

