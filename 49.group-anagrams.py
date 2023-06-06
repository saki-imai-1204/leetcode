#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We will define defaultdict() at first instead of a normal 
        # dictionary so that it wouldn’t given an error when the 
        # count does not exist yet
        groups = defaultdict(list)
        for str in strs:
            counts = [0 for i in range(26)]
            for char in str:
                counts[ord(char) - ord('a')] += 1
            # Lists are not allowed as a key for hashmap in Python 
            # and this is why we are converting to tuple
            groups[tuple(counts)].append(str) 
        return groups.values()
    
    
# Notes (6/5/2023)
# Potential solution: sort each word and group them 
#   However, sorting each word is O(nlogn) where n is the length of a word
#   So, the overall complexity is O(m*nlogn) where m is the number of words in a list

# Better solution?
#   Use hashmap!
#   Time complexity: O(m*n*26) -> O(m*n)
#       where m is the total number of input strings we are given
#             n is the average length of a string

        
# @lc code=end

