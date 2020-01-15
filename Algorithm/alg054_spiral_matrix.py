# 54. Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Init Output
        out = []

        if len(matrix) == 0:
            return out

        m = len(matrix)  # Number of Rows
        n = len(matrix[0])  # Number of Columns

        r0 = 0  # Start Row
        c0 = 0  # Start Col

        while (r0 < m and c0 < n):
            # print("Start:", m,n, r0,c0)
            for c in range(c0, n):
                out.append(matrix[r0][c])
            r0 += 1

            for r in range(r0, m):
                out.append(matrix[r][n - 1])
            n -= 1

            if r0 < m:
                for c in range(n - 1, c0 - 1, -1):
                    out.append(matrix[m - 1][c])
                m -= 1

            if c0 < n:
                for r in range(m - 1, r0 - 1, -1):
                    out.append(matrix[r][c0])
                c0 += 1

                # print("End:", m,n, r0,c0)
        return out


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matrix : ")
    print(mat, "\n")

    print("Spiral : ")
    print(sol.spiralOrder(mat))
