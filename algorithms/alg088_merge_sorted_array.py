# 88. Merge Sorted Array (Easy)
# https://leetcode.com/problems/merge-sorted-array/
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Note:
#     The number of elements initialized in nums1 and nums2 are m and n respectively.
#     You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
#
# Example:
#   nums1 = [1,2,3,0,0,0], m = 3
#   nums2 = [2,5,6],       n = 3
#   Output: [1,2,2,3,5,6]


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0:
            # If nums1: empty, in-place assign nums2
            nums1[:] = nums2[:]
        elif n == 0:
            # if nums2:empty, nums1 is unchanged
            pass
        else:
            # if nums1, nums2 are non empty
            # Use Empty Space at End and work your way backward
            i1, i2 = m - 1, n - 1
            i = m + n - 1
            while i1 >= 0 and i2 >= 0:
                if nums1[i1] <= nums2[i2]:
                    nums1[i] = nums2[i2]
                    i2 -= 1
                    i -= 1
                else:
                    nums1[i] = nums1[i1]
                    i1 -= 1
                    i -= 1

            # if elements left in nums2, move them to start of nums1
            while i2 >= 0:
                nums1[i] = nums2[i2]
                i2 -= 1
                i -= 1


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    out = [1, 2, 2, 3, 5, 6]
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3

    nums1 = [5, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3]
    n = 3

    print("List1, %s: %s" % (m, nums1))
    print("List2, %s: %s" % (n, nums2))
    print()
    print("Expected: ", out)

    sol.merge(nums1, m, nums2, n)
    print("Merged: ", nums1)
