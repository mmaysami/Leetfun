# """
# Find Maze Path Feasibility [Amazon]
# Imagine we have an n x n grid with each cell taking values of zero for path and 1 for wall/blocked.
# Given an starting point and exit point, find if there is any path from start to end.
# Note: We are only interested to know if there is a path or not, and path's details are not required.
#
# Example of starting and subsequent grid stages:
# maze = [[0, 0, 1, 0, 0],
#         [1, 0, 0, 0, 0],
#         [0, 0, 1, 0, 1],
#         [1, 0, 0, 1, 1],
#         [1, 0, 0, 1, 0]]
# True
# """


import typing

def has_path(maze, pt_a, pt_b, visited=[]):
    """
    Using DFS on Graph of Maze
    TODO Note: We can mark visited cells as 1 to block since all options from there-on will be explored,
            and since we do not care about path details
    :param maze:
    :param pt_a:
    :param pt_b:
    :param visited:
    :return:
    """
    print(maze)
    visited.append(pt_a)
    i, j = pt_a
    maze[i][j] = 1

    n, m = len(maze), len(maze[0])
    for di, dj in [(-1, 0), (+1, 0), (0, -1), (0, +1)]:

        # Alternative to Visited
        # if not any(map(lambda x: [0 for e in x], maze)):
        #     return False

        if 0 <= i + di < n and 0 <= j + dj < m:
            if (i + di, j + dj) == pt_b:
                print('From ({0},{1}) to ({2}, {3})'.format(i, j, i + di, j + dj))
                return True

            if maze[i + di][j + dj] == 0 and (i + di, j + dj) not in visited:
                print('From ({0},{1}) to ({2}, {3})'.format(i, j, i + di, j + dj))

                # Alternative to Visited
                # maze[i + di][j + dj] == 1
                visited.append((i + di, j + dj))
                if has_path(maze, (i + di, j + dj), pt_b, visited):
                    return True
                else:
                    print('Dead End!')

    return False


# ================================================================================
#   Tests
# ================================================================================
maze = [[0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 0, 1, 1],
        [1, 0, 0, 1, 0]]

check = has_path(maze, (2, 3), (4, 1))
print(check)
