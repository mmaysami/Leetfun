# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/
#
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
#
# Note:
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Flip Horizontal
        # self.hflip(matrix)
        matrix.reverse()

        # Swap versus Diagonal
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        return None

    # # Horizontal flip of rows
    # def hflip(self, matrix):
    #     n = len(matrix)
    #     r = 0
    #     while r < n // 2:
    #         matrix[r], matrix[n - 1 - r] = matrix[n - 1 - r], matrix[r]
    #         r += 1


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Matrix : \n", matrix)

    sol.rotate(matrix)
    print("Rotated Matrix : \n", matrix)
