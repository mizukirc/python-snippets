# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


# %%
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """    
        di = {}
        for idx, elem in enumerate(nums):
            di[elem] = idx

        for idx, elem in enumerate(nums):
            diff = target - nums[idx]
            if diff in di.keys() and di[diff] != idx:
                return [idx,di[diff]]
        return []


# %%
# test code
if __name__ == '__main__':
    nums = [11,2,7,15]
    target = 9
    sol = Solution()
    print(sol.twoSum(nums, target))


# %%



