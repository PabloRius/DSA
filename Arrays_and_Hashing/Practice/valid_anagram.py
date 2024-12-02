"""
Given two strings s and t, 
    return true if 
        the two strings are anagrams of each other, 
    otherwise return false.

An anagram is a string 
that contains the exact same characters as another string, 
but the order of the characters can be different.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = {}
        for i in s:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        for j in t:
            if j in seen:
                if seen[j] == 1:
                    del seen[j]
                else:
                    seen[j] -= 1
            else:
                return False
        return True
