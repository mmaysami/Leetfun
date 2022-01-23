# """
# Conway’s Game of Life [Shopify]
# Imagine we have an n x n grid (n>=4) with each cell containing an organism.
# At any stage a cell can be alive or dead; where 0 and 1 represent dead and live organisms, respectively.
# The cell’s lifecycle is determined by its state (alive or dead) in the previous stage.
#
# Rules for Subsequent stages:
#     Any live cell (1) with fewer than two live neighbours dies, as if caused by underpopulation.
#     Any live cell (1) with two or three live neighbours lives on to the next generation.
#     Any live cell (1) with more than three live neighbours dies, as if by overpopulation.
#     Any dead cell (0) with exactly three live neighbours becomes a live cell, as if by reproduction.
#     Every cell interacts with its 8 neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.
#
# Example of starting and subsequent grid stages:
# T=0
#     0 0 0 0
#     0 1 1 0
#     0 0 0 0
#     0 0 1 0
# T=1
#     0 0 0 0
#     0 0 0 0
#     0 1 1 0
#     0 0 0 0
#
# T=2
#     0 0 0 0
#     0 0 0 0
#     0 0 0 0
#     0 0 0 0
#
# Problem statement
#     Implement a simulation of the Conway's Game of Life, where the only inputs are the initial board, and a maximum number of stages.
#     At each stage, print the current board.
#     Stop the simulation as soon as the maximum number of stages is reached.
# """

from copy import deepcopy

def get_neighbors(i, j, n):
    """
    Pass Cell i,j index, Get List of Pairs of [k,p] of valid neighbors
    """
    list_neighbors = []

    #     if (i in [0,n-1]) and (j in [0,n-1]):
    #         n_neighbors = 3

    #     elif (i in [0,n-1]) or (j in [0,n-1]):
    #         n_neighbors = 5

    #     else:
    #         n_neighbors = 8

    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if i + di < 0 or i + di >= n:
                # Out of Bound along axis 0
                continue

            if j + dj < 0 or j + dj >= n:
                # Out of Bound along axis 1
                continue

            if di == 0 and dj == 0:
                # Cell itself (i,j)
                continue
            list_neighbors.append([i + di, j + dj])

    return list_neighbors


def evolve(state):
    """
    state: list[list]


    Any live cell with fewer than two live neighbours dies
    Any live cell with more than three live neighbours dies
    Any live cell with two or three live neighbours lives on to the next generation.

    Any dead cell with exactly three live neighbours becomes a live cell.
        T=0
            0 0 0 0
            0 1 1 0
            0 0 0 0
            0 0 1 0

        T=1
            0 0 0 0
            0 0 0 0
            0 1 1 0
            0 0 0 0

        T=2
            0 0 0 0
            0 0 0 0
            0 0 0 0
            0 0 0 0
    """
    n = len(state[0])
    # Use looped comprehension or deepcopy
    evolution = [[-1 for x in range(n)] for y in range(n)]
    # evolution = deepcopy(state)

    for i in range(n):
        for j in range(n):
            list_neighbors = get_neighbors(i, j, n)

            # Sum over Neighbors
            sum_neighbors = 0
            for neighbor in list_neighbors:
                sum_neighbors += state[neighbor[0]][neighbor[1]]

            # print('i,j, state, neighbors', i,j, state[i][j], sum_neighbors)
            # Apply Logic
            if state[i][j] == 0:
                # Dead Cell
                evolution[i][j] = int(sum_neighbors == 3)
            else:
                # Alive Cell
                evolution[i][j] = int(sum_neighbors in [2, 3])

    return evolution


def simulate(state, t):
    """
        state: list[list]
        t: number of timesteps / evolutions
    """

    for step in range(t):
        state = evolve(state)
        print('Generation {}:'.format(1 + step))
        print(*state, sep='\n')

    return state


# =============================================================================
if __name__ == '__main__':
    test_neighbors = False
    test_simulate = True

    caste_state0= [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 1, 0]]

    if test_simulate:
        # Test Evolution Simulation
        simulate(caste_state0, 2)

    if test_neighbors:
        # Test Neighbors
        cases = [([0, 0], 3),
                 ([3, 0], 3),
                 ([0, 3], 3),
                 ([3, 3], 3),
                 ([0, 2], 5),
                 ([1, 0], 5),
                 ([3, 2], 5),
                 ([1, 3], 5),
                 ([1, 1], 8),
                 ]

        for c, case in enumerate(cases):
            n = len(caste_state0[0])
            [i, j], expected = case


            list_neighbors = get_neighbors(i, j, n)
            print('({},{}):  {} vs. {} (Neighbors vs. Expected)'.format(i,j, len(list_neighbors), expected))
            # print('Output {}'.format(list_neighbors))
