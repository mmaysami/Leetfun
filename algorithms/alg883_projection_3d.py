# 886. Projection Area of 3D Shapes (Easy)
# https://leetcode.com/problems/projection-area-of-3d-shapes/
#
# You are given an n x n grid where we place some 1 x 1 x 1 cubes that are axis-aligned with the x, y, and z axes.
# Each value v = grid[i][j] represents a tower of v cubes placed on top of the cell (i, j).
# We view the projection of these cubes onto the xy, yz, and zx planes.
# A projection is like a shadow, that maps our 3-dimensional figure to a 2-dimensional plane. We are viewing the "shadow" when looking at the cubes from the top, the front, and the side.
#
# Return the total area of all three projections.
#
# Examples:
#   Input: grid = [[1,2],[3,4]]
#   Output: 17
#   Explanation: Here are the three projections ("shadows") of the shape made with each axis-aligned plane.
#
#   Input: grid = [[2]]
#   Output: 5

import typing
from functools import reduce


class Solution:
    def projectionArea(self, grid):  # list[list[int]]) -> int
        # XY: 1s for each block
        proj_xy = sum(map(lambda b: sum([h > 0 for h in b]), grid))

        # Max i-th element along all rows
        proj_yz = sum(reduce(lambda b1, b2: [max(b1[i],b2[i]) for i in range(len(b1))], grid))

        # Max element in each row
        proj_xz = sum(map(lambda b: max(b), grid))

        # print(proj_xy, proj_yz, proj_xz)
        return proj_xy+proj_yz+proj_xz


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    in1 = [[1, 2], [3, 4]]
    out1 = 17

    in2 = [[2]]
    out2 = 5

    my_in, my_out = in2, out2
    print("Input    : %s" % (my_in))
    print("Expected : %s" % (my_out))
    print()

    out = sol.projectionArea(my_in)
    print("Output : %s" % (out))
