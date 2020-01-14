# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = len(nums) != len(set(nums))
        return result
    
in1 = [1,2,3,1]
in2 = [1,2,3,4]
in3 = [1,1,1,3,3,4,3,2,4,2]

s = Solution()
s.containsDuplicate(in1) # True
s.containsDuplicate(in2) # False
s.containsDuplicate(in3) # True