# 215. Kth Largest Element in an array [FB] (Medium)
# https://leetcode.com/problems/kth-largest-element-in-an-array/
#
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example:
#   Input: nums = [3,2,1,5,6,4], k = 2
#   Output: 5
#
#   Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#   Output: 4
#
# Constraints:
#     1 <= k <= nums.length <= 104
#     -104 <= nums[i] <= 104

import typing
import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        """
        heapq is a binary heap, O(N) heapify, O(log N) push and O(log N) pop. See the heapq source code.
        https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library/38833175
        """
        # K-Restricted heapq
        # time complexity: O(N * log K), space : O(K)

        if not nums or not (0 < k <= len(nums)): return -1
        q = nums[:k]
        heapq.heapify(q)    # O(Log K)

        for num in nums[k::]:
            # print('element {:2},  heap: {}'.format(num, q))
            heapq.heappushpop(q, num)   # Push new value, Pop smallest      O((N-K).Log K)

        # Root = K-th Largest Number
        return q[0]

    def findKthLargest_heap(self, nums: list, k: int) -> int:
        """
        A proxy to find array of K largest elements

        Time  Complexity O(N+K LogN)
        Space Complexity O(K)

        :param k:
        :return:
        """

        if not nums or not (0 < k <= len(nums)): return -1
        temp = []
        nums_neg = [-e for e in nums]
        heapq.heapify(nums_neg)  # O(n)
        for i in range(k):
            temp.append(-heapq.heappop(nums_neg))  # O(K LogN)

        return temp[-1]

    def findKthLargest_selection(self, nums: list, k: int) -> int:
        """
        Use Selection Sort for loop K times

        Time Complexity O(K.N)
        Space Complexity O(1)

        :param k:
        :return:
        """

        if not nums or not (0 < k <= len(nums)): return -1

        for i in range(k):  # O(K)
            j_max = i
            for j in range(i + 1, len(nums)):  # O(N)
                if nums[j] > nums[j_max]:
                    j_max = j

            nums[i], nums[j_max] = nums[j_max], nums[i]

        return nums[k - 1]

    def findKthLargest_bubble(self, nums: list, k: int) -> int:
        """
        Use Bubble Sort while running outer look K times

        Time Complexity O(K.N)
        Space Complexity O(1)

        :param k:
        :return:
        """
        if not nums or not (0 < k <= len(nums)): return -1

        for i in range(k):  # O(K)
            for j in range(len(nums) - 1):  # O(N)
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        return nums[-k]


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    my_in = [13, 2, 21, 8]
    k = 2
    out = 13

    d1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    d2 = d1[::-1].copy()
    d3 = [3, 1, 9, 7, -2, 14, 9, 8, 7, 6]
    d4 = [-9, 1, 2, -4, 3, -2, -14, 0, 2, 3, 6]

    k = 4
    cases = [d1, d2, d3, d4]

    for d in cases:
        print("\nInput  : %s" % d)
        print("Expected : %s" % sorted(d)[-k])
        print('---')

        kth_out = sol.findKthLargest(d, k)
        kth_selection = sol.findKthLargest_selection(d, k)
        kth_bubble = sol.findKthLargest_bubble(d, k)
        kth_heap = sol.findKthLargest_heap(d, k)
        print('Top K-MHP: %s' % kth_out)
        # print('Top K-SEL: %s' % kth_selection)
        # print('Top K-BBL: %s' % kth_bubble)
        # print('Top K-HIP: %s' % kth_heap)

