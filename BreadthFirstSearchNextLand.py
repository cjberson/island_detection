"""
This is the best approach I could implement without making an agent
that learns. It keeps track of the farthest index it has
seen in each row. It generates new states only downward in right rather than in
four directions like the other approaches. Whenever the queue of states is
emptied, it finds the next land by iterating over each row starting at the
farthest index it has seen previously. Using a smarter generator and having the
ability easily find the next land to explore, greatly reduces the search space
and as a result greatly improves performance. In my testing on large grids, with
minimum and maximum dimensions of 50 and 100 respectively, this method visits less
than half the number of nodes and finds the solution in half the time.
"""
from collections import deque
from typing import Tuple, Dict

from Constants import Grid, LAND, WATER
from Generator import generate_downward_moves


def bfs_next_land(grid: Grid) -> int:
    return bfs_next_land_with_node_count(grid)[0]


def bfs_next_land_with_node_count(grid: Grid) -> Tuple[int, int]:
    row_to_farthest: Dict[int, int] = {i: -1 for i in range(len(grid))}
    first_land = find_next_land(grid, row_to_farthest)
    q = deque()
    q.appendleft(first_land)
    visited = set()
    island_count = 0

    while True:
        if len(q) == 0:
            island_count += 1
            next_land = find_next_land(grid, row_to_farthest)

            if next_land is None:
                break
            else:
                q.appendleft(next_land)

        state = q.pop()
        x, y = state

        if state not in visited:
            visited.add(state)

            if y > row_to_farthest[x]:
                row_to_farthest[x] = y

            if grid[x][y] == LAND:
                grid[x][y] = WATER

                for new_state in generate_downward_moves(grid, state):
                    q.appendleft(new_state)

    return island_count, len(visited)


def find_next_land(grid: Grid, row_to_farthest: Dict[int, int]):
    for i, farthest_j in row_to_farthest.items():
        # Start one past the farthest we have been
        j = farthest_j + 1
        while j < len(grid[0]):
            if grid[i][j] == LAND:
                return i, j
            j += 1

    return None
