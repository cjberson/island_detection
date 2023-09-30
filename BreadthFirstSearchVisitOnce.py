"""
This is my first attempt in trying to write a more efficient algorithm. The idea
was to find all the land upfront and then perform a BFS starting at the land
coordinates. This strategy searches fewer nodes during the BFS stage than the
leet code approach, but the extra iterations that must be done up front is causes
worse performance overall.
"""
from collections import deque
from typing import Tuple

from Constants import Grid, LAND, WATER
from Generator import generate_moves


def bfs_visit_once(grid: Grid) -> int:
    return bfs_visit_once_with_node_count(grid)[0]


def bfs_visit_once_with_node_count(grid: Grid) -> Tuple[int, int]:
    """
    Find all the land then perform a breadth first search starting from each land
    coordinate until all land has been visited.

    :param grid: the grid we are navigating
    :return: the number of islands and the number of nodes visited
    """
    island_count = 0
    unvisited_land = {
        (i, j)
        for i in range(len(grid))
        for j in range(len(grid[0]))
        if grid[i][j] == LAND
    }

    if len(unvisited_land) == 0:
        return 0, 0

    start = next(iter(unvisited_land))
    visited = set()

    q = deque()
    q.appendleft(start)

    while len(unvisited_land) > 0:
        if len(q) == 0:
            island_count += 1
            q.appendleft(next(iter(unvisited_land)))

        state = q.pop()

        if state not in visited:
            x, y = state

            visited.add(state)

            if grid[x][y] == LAND:
                unvisited_land.remove(state)
                grid[x][y] = WATER

                for new_state in generate_moves(grid, state):
                    q.appendleft(new_state)

    # Finished looking at all the land, but queue wasn't emptied so one island wasn't accounted for
    if len(q) > 0:
        island_count += 1

    return island_count, len(visited)
