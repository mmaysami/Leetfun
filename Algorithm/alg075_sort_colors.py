# 75. Sort Colors
# https://leetcode.com/problems/sort-colors/

# Given an array with n objects color red, white, or blue, sort them in-place so that objects of the same color are adjacent,
# with the colors in the order ir, iw and ib.
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this problem.
#     A rather straight forward solution is a two-pass algorithm using counting sort.
#     First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
#     Could you come up with a one-pass algorithm using only constant space?
#
# Example:
#   Input:  [2,0,2,1,1,0]
#   Output: [0,0,1,1,2,2]


class Solution:

    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        ind = [0, 0, 0]
        for i in range(len(nums)):
            # print(40 * '-')
            # print("Indices: ", ind)
            # print("Nums @ (i,e): ", nums, (i, nums[i]))
            self.sortElement(nums, ind, i)

    # ---------------------------------------------------------------
    #       Main Solution
    # ---------------------------------------------------------------
    def sortElement(self, nums, ind, i):
        if nums[i] == 2:
            nums[i] = nums[ind[2]]
            nums[ind[2]] = 2
            ind[2] += 1

        elif nums[i] == 1:
            nums[i] = nums[ind[1]]
            nums[ind[1]] = 1

            ind[1] += 1
            ind[2] += 1

        elif nums[i] == 0:
            nums[i] = nums[ind[1]]
            nums[ind[1]] = nums[ind[0]]
            nums[ind[0]] = 0

            ind[0] += 1
            ind[1] += 1
            ind[2] += 1

    # ---------------------------------------------------------------
    #       Lomuto partition algorithm
    # ---------------------------------------------------------------
    def sortColors_alt1(self, nums):
        ir, iw = 0, 0
        for n in range(len(nums)):
            val, nums[n] = nums[n], 2

            # practically effective ONLY if val=1
            if val < 2:
                nums[iw] = 1
                iw += 1

            # Overwrite val < 2 if val=0
            if val == 0:
                nums[ir] = 0
                ir += 1

    # ---------------------------------------------------------------
    #       Dutch Partitioning Solution
    #       https://en.wikipedia.org/wiki/Dutch_national_flag_problem
    # ---------------------------------------------------------------
    def sortColors_alt2(self, nums):
        """
        classifying the array into four groups: ir, iw, unclassified, and ib.
        Initially we group all elements into unclassified.
        We iterate from the beginning as long as the iw pointer is less than the ib pointer.
        """
        ir, iw, ib = 0, 0, len(nums) - 1

        while iw <= ib:
            if nums[iw] == 0:
                nums[ir], nums[iw] = nums[iw], nums[ir]
                iw += 1
                ir += 1
            elif nums[iw] == 1:
                iw += 1
            else:
                nums[iw], nums[ib] = nums[ib], nums[iw]
                ib -= 1


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    # nums = [2, 0, 2, 1, 1, 0]
    # out =  [0, 0, 1, 1, 2, 2]
    # print("Nums: ", nums)
    # print("Expected: ", Output)
    #
    # sol.sortColors(nums)
    # print("Sorted: ", nums)

    nums0 = (1, 0, 1, 1, 0)
    nums = list(nums0)
    sol.sortColors_alt1(nums)
    print("Sorted: ", nums)
    #
    # nums = list(nums0)
    # sol.sortColors_alt2(nums)
    # print("Sorted: ", nums)
