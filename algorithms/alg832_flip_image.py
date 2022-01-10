# 832. Flipping an Image (Easy)
# https://leetcode.com/problems/flipping-an-image/
#
# Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
# To flip an image horizontally means that each row of the image is reversed.
#   For example, flipping [1,1,0] horizontally results in [0,1,1].
# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.
#   For example, inverting [0,1,1] results in [1,0,0].
#
# Example 1:
#   Input: image = [[1,1,0],[1,0,1],[0,0,0]]
#   Output: [[1,0,0],[0,1,0],[1,1,1]]
#   Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
#   Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
#
#   Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
#   Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#   Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
#   Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
# Constraints:
#     n == image.length
#     n == image[i].length
#     1 <= n <= 20
#     images[i][j] is either 0 or 1.

import typing
from functools import reduce


class Solution:
    def flipAndInvertImage(self, image):  # List[List[int]]) -> List[List[int]]
        res = [list(map(lambda b: 1 - b, e[-1::-1])) for e in image]
        return res

# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    in1 = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    out1 = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]

    in2 = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
    out2 = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]

    my_in, my_out = in2, out2
    print("Input    : %s" % (my_in))
    print("Expected : %s" % (my_out))

    out = sol.flipAndInvertImage(my_in)
    print("Output   : %s" % (out))
