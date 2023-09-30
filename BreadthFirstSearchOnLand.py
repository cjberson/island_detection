"""
This is the approach that Leet code provides as a solution. It solves
the problem, but in a less than elegant fashion. In particular, the
iteration of the grid and the breadth-first search used to replace
land with water do not communicate. This becomes an issue as the problem
grows since there the unnecessary iterations will cause a performance dip.
This can be solved by preventing revisiting of coordinates.
"""
from collections import deque
from typing import List, Tuple

from Constants import WATER, LAND, Grid
from Generator import generate_downward_moves


def bfs_on_land(grid: Grid) -> int:
    return bfs_on_land_with_node_count(grid)[0]


def bfs_on_land_with_node_count(grid: Grid) -> Tuple[int, int]:
    """
    Iterate over the whole grid. Whenever land is found, increase the island count by 1.
    Then perform a BFS to remove all land that can be walked to via the land with water
    to avoid double counting in the next iterations

    :param grid: the grid we are counting islands for
    :return: the number of islands and the number of nodes visited
    """
    island_count = 0
    nodes_visited = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == LAND:
                island_count += 1
                nodes_visited += bfs_land_to_water(grid, (i, j))

    return island_count, nodes_visited


def bfs_land_to_water(grid: Grid, coordinate: Tuple[int, int]) -> int:
    """
    Starting from the given coordinate of land, replace all water that can be
    navigated to in by traveling up, down, left or right with land

    :param grid: the grid we are navigating
    :param coordinate: the coordinate we are starting at
    :return: the number of nodes visited for statistics
    """
    i, j = coordinate

    q = deque()
    q.appendleft((i, j))
    visited = set()

    # Via a breadth first search replace all land with water
    while len(q) > 0:
        state = q.pop()

        if state not in visited:
            visited.add(state)
            x, y = state

            if grid[x][y] == LAND:
                grid[x][y] = WATER
                for new_state in generate_downward_moves(grid, state):
                    q.appendleft(new_state)

    return len(visited)
