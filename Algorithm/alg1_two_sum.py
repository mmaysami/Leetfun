# 1. Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        # Hash (Faster than Brute-Force,
        #                       but not Memory Efficient)
        hseen = dict()
        for i, num in enumerate(nums):
            if target - num not in hseen.keys():
                hseen[num] = i
            else:
                return [hseen[target - num], i]
