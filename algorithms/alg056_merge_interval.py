# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and
# return an array of the non-overlapping intervals that cover all the intervals in the input.
#

# Example 1:
#   Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#
# Example 2:
#   Input: intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
#
#
# Constraints:
#     1 <= intervals.length <= 104
#     intervals[i].length == 2
#     0 <= starti <= endi <= 104


class Solution:
    def merge(self, arr):
        arr.sort(key=lambda x: x[0])

        out = []
        i = 0
        while i < len(arr) - 1:
            temp_end = arr[i][1]
            j = 1

            while temp_end >= arr[j][0] and j < len(arr):
                # print(i,j)
                temp_end = max(arr[i][1], arr[j][1])
                j += 1

            out.append([arr[i][0], temp_end])
            i = j

        if i == len(arr) - 1:
            out.append([arr[i][0], arr[i][1]])
        return out


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()

    intervals = [[1, 6], [2, 3], [7, 9], [8, 10], [15, 18]]
    # intervals = [[1, 3], [2, 6], [7, 10], [15, 18]]
    expected = [[1, 6], [8, 10], [15, 18]]

    out = sol.merge(intervals)
    print('Intervals: ', intervals)
    print('Expected : ', expected)
    print('Output   : ', out)

