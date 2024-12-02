"""
Given an array of strings strs, 
    group all anagrams together into sublists. 
    You may return the output in any order.

An anagram is a string 
that contains the exact same characters as another string, 
but the order of the characters can be different.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-ord("a")] += 1
            sol[tuple(count)].append(i)
        return list(sol.values())
