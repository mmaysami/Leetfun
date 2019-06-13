# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Problem:
#   Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# Example:
#   Given nums = [2, 7, 11, 15], target = 9,
#   Because nums[0] + nums[1] = 2 + 7 = 9,
#   return [0, 1]

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

#===============================================================================
#===============================================================================
#===============================================================================
if __name__ == "__main__":
    sol = Solution()
    print (sol.twoSum([2, 7, 11, 15],9))
