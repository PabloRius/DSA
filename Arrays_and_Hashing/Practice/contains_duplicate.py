""" 
Given an integer array nums, 
  return true if 
    any value appears more than once in the array, 
  otherwise return false 
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = {}
        for i in nums:
            if i in check:
                return True
            check[i] = True
        return False

