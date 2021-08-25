# 2D Spiral Array
# https://www.facebook.com/careers/life/sample_interview_questions/Af8BaL90PrQGVj_YuGqVdJhmgdeuj-dq1vO9gy4HAmrDRNAglybwgdtN55L5_rICwCY

import numpy as np


def spiral2d(n, start=1):
    """
    Print Spiral Range of Numbers in Matrix of n*n
    input = 3
    123
    894
    765

    input = 4
    01 02 03 04
    12 13 14 05
    11 16 15 06
    10 09 08 07
    """
    # Find max numbers and string characters
    max_num = start - 1 + n ** 2
    max_char = len(str(max_num))

    # Init String Array
    # m = np.empty((n, n), dtype='U%s' %max_char)
    m = np.chararray((n, n), itemsize=max_char, unicode=True)

    if n < 1:
        return None
    elif n == 1:
        m[0, 0] = str(start).zfill(max_char)
        m = m.ravel()
    else:
        start1 = start
        start2 = start1 + n
        start3 = start2 + (n - 1)
        start4 = start3 + (n - 1)
        start5 = start4 + (n - 2)

        m[0, :] = np.array([str(e).zfill(max_char) for e in range(start1, start2)])
        m[1::, n - 1] = np.array([str(e).zfill(max_char) for e in range(start2, start3)])
        m[n - 1, 0:n - 1] = np.array([str(e).zfill(max_char) for e in range(start4 - 1, start3 - 1, -1)])
        m[1:n - 1, 0] = np.array([str(e).zfill(max_char) for e in range(start4 + n - 2 - 1, start4 - 1, -1)])

    if n > 2:
        m_inner = spiral2d(n - 2, start=start5)
        # print(m_inner)
        m[1:n - 1, 1:n - 1] = m_inner

    return m


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    for n in range(8, 9):
        sol = spiral2d(n)
        print(str(sol))
