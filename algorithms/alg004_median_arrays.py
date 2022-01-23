# 4. Median of Two Sorted Arrays (Hard)
# https://leetcode.com/problems/median-of-two-sorted-arrays/
#
# Problem:
#   There are two sorted arrays nums1 and nums2 of size m and n respectively.
#   Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#   You may assume nums1 and nums2 cannot be both empty.
#
# Example:
#   nums1 = [4, 20, 32, 50, 55, 61]
#   nums2 = [1, 12, 22, 30, 70]
#   median = 30
#
#   nums1 = [16, 20, 23, 50, 54, 60]
#   nums2 = [65, 72, 72, 80, 85, 93]
#   median = 62.5

import typing

class Solution:

    # ---------------------------------------------------------------
    #       Main Solution
    # ---------------------------------------------------------------
    def findMedianSortedArrays(self, nums1, nums2):
        # Get Length of Inputs
        m = len(nums1)
        n = len(nums2)
        if m + n <= 1:
            u = nums1 + nums2
            return u[0]

        half_union = []
        half_len = (m + n) // 2 + 1

        while nums1 and nums2 and len(half_union) <= half_len:
            # Append smallest element until filling to median of half_union
            half_union.append(nums1.pop(0) if nums1[0] < nums2[0] else nums2.pop(0))

        print(half_union)
        # Append non-empty            
        if len(half_union) <= half_len:
            if nums1:
                half_union += nums1
            if nums2:
                half_union += nums2

        # Note: half_len = (m + n) // 2 + 1
        if (m + n) % 2 == 1:
            med = half_union[half_len - 1]
        else:
            # med = 1/2 (half, half-1)
            med = 0.5 * (half_union[half_len - 1] + half_union[half_len - 2])
        return med


    # ---------------------------------------------------------------
    #       Alternate Solution
    # ---------------------------------------------------------------
    def findMedianSortedArrays_alt(self, nums1, nums2) -> float:
        m = len(nums1)
        n = len(nums2)
        if m + n <= 1:
            u = nums1 + nums2
            return u[0]

        # Init Half of half_union, Indices for each array
        half_len = (m + n) // 2 + 1
        i1 = min(half_len, m - 1)
        i2 = min(half_len, n - 1)

        # Find Index of Half for Both Arrays
        while i1 + i2 >= half_len and i1 > 0 and i2 > 0:
            # print(">>> In: %i, %i" % (i1, i2))
            # print(">>> In-Nums1: %s" % nums1[0:i1 + 1])
            # print(">>> In-Nums2: %s" % nums2[0:i2 + 1])
            if nums1[i1] < nums2[i2 - 1]:
                i2 -= 2
            elif nums1[i1 - 1] > nums2[i2]:
                i1 -= 2
            else:
                i1 -= 1
                i2 -= 1

        # print(">>> Out: %i, %i=%i+%i" % (half_len, i1 + i2 + 2, i1 + 1, i2 + 1))
        # print(">>> Out-Nums1: %s" % nums1[0:i1 + 1])
        # print(">>> Out-Nums2: %s" % nums2[0:i2 + 1])

        # Generate List of Half of Both Arrays
        half_list = []
        while (i1 + i2 + 2 >= half_len - 1):  # and i1>=0 and i2>=0:
            # print()
            # print(">>> In: %i, %i" % (i1, i2))
            # print(">>> In-Nums1: %s" % nums1[0:i1 + 1])
            # print(">>> In-Nums2: %s" % nums2[0:i2 + 1])
            if i1 < 0:
                half_list.append(nums2[i2])
                i2 -= 1
            elif i2 < 0:
                half_list.append(nums1[i1])
                i1 -= 1
            elif nums1[i1] < nums2[i2]:
                half_list.append(nums2[i2])
                i2 -= 1
            elif nums1[i1] > nums2[i2]:
                half_list.append(nums1[i1])
                i1 -= 1
            # print("<<< half_list :", half_list)

        # half_len, i1 + i2 + 2
        if (m + n) % 2 == 1:
            med = half_list[-2]

        else:
            # med = 1/2 (half, half-1)
            med = 0.5 * (half_list[-1] + half_list[-2])
        return med

# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    nums1 = [4, 20, 32, 50, 55, 61]
    nums2 = [1, 12, 22, 30, 70]
    med12 = 30

    # nums1 = [16, 20, 50, 54, 60]
    # nums2 = [65, 72, 72, 85, 93]
    # med12 = 62.5
    #
    # nums1 = [1, 2]
    # nums2 = [3, 4]
    # med12 = 2.5
    #
    # nums2 = [1]
    # nums1 = [1]
    # med12 = 1

    print("Num1 : ", nums1)
    print("Num2 : ", nums2)
    union = nums1 + nums2
    union.sort()
    print("Full union: ", union)
    print("Len  : ", len(union))
    print("Med12: ", med12)
    # print(sol.findMedianSortedArrays(nums1, nums2))
    print(sol.findMedianSortedArrays(nums1, nums2))
