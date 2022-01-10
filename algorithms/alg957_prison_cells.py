# 957. Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/
#
# here are 8 prison cells in a row, and each cell is either occupied or vacant.
# Each day, whether the cell is occupied or vacant changes according to the following rules:
#   - If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
#   - Otherwise, it becomes vacant.
#   - That because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors and will set to Empty!?
#
# We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
# Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
#
# Constraints:
#     cells.length == 8
#     cells[i] is in {0, 1}
#     1 <= N <= 10^9
#
# Examples:
#
#   Input:  [0,1,0,1,1,0,0,1], N = 7
#   Output: [0,0,1,1,0,0,0,0]
#       Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
#       Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
#       Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
#       Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
#       Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
#       Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
#       Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
#       Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
#
#   Input:  [1,0,0,1,0,0,1,0], N = 1000000000
#   Output: [0,0,1,1,1,1,1,0]


class Solution:
    """
    #   Input:  [0, 1, 0, 1, 1, 0, 0, 1], N = 7
    #   Output: [0, 0, 1, 1, 0, 0, 0, 0]
    #       Day 0:  [0, 1, 0, 1, 1, 0, 0, 1]
    #       Day 1:  [0, 1, 1, 0, 0, 0, 0, 0]    Cycle Start
    #       Day 2:  [0, 0, 0, 0, 1, 1, 1, 0]
    #       Day 3:  [0, 1, 1, 0, 0, 1, 0, 0]
    #       Day 4:  [0, 0, 0, 0, 0, 1, 0, 0]
    #       Day 5:  [0, 1, 1, 1, 0, 1, 0, 0]
    #       Day 6:  [0, 0, 1, 0, 1, 1, 0, 0]
    #       Day 7:  [0, 0, 1, 1, 0, 0, 0, 0]
    #       Day 8:  [0, 0, 0, 0, 0, 1, 1, 0]
    #       Day 9:  [0, 1, 1, 1, 0, 0, 0, 0]
    #       Day 10: [0, 0, 1, 0, 0, 1, 1, 0]
    #       Day 11: [0, 0, 1, 0, 0, 0, 0, 0]
    #       Day 12: [0, 0, 1, 0, 1, 1, 1, 0]
    #       Day 13: [0, 0, 1, 1, 0, 1, 0, 0]
    #       Day 14: [0, 0, 0, 0, 1, 1, 0, 0]
    #       Day 15: [0, 1, 1, 0, 0, 0, 0, 0]    Cycle Start
    """

    def prisonAfterNDays(self, cells: list, n: int) -> list:
        if n == 0:
            return cells

        status = cells
        dict_states = {str(status): 0}  # items = {states: Day}
        cycle_end = None

        # Loop over days until finding a cycle
        for m in range(1, n + 1):
            # Switch States based on rules
            status = [0] + [1 if status[i - 1] == status[i + 1] else 0 for i in range(1, len(status) - 1)] + [0]

            if not str(status) in dict_states.keys():
                dict_states[str(status)] = m
            else:
                cycle_start, cycle_end = dict_states[str(status)], m
                break

        if cycle_end:
            # Status = state at Cycle End
            for c in range((n - cycle_start) % (cycle_end - cycle_start)):
                status = [0] + [1 if status[i - 1] == status[i + 1] else 0 for i in range(1, len(status) - 1)] + [0]
        return status


# ===============================================================================
# ===============================================================================
# ===============================================================================
if __name__ == "__main__":
    sol = Solution()
    N1 = 7
    in1 = [0, 1, 0, 1, 1, 0, 0, 1]
    out1 = [0, 0, 1, 1, 0, 0, 0, 0]

    N2 = 8
    in2 = [0, 0, 1, 1, 1, 1, 0, 0]
    out2 = [0, 0, 0, 1, 1, 0, 0, 0]

    my_in, my_out, my_N = in2, out2, N2
    out = sol.prisonAfterNDays(my_in, my_N)

    print("Input    : %s" % (my_in))
    print("N days   : %s" % (my_N))
    print("Expected : %s" % (my_out))
    print("Output   : %s" % (out))

