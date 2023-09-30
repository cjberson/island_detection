from typing import Tuple, Iterable

from Constants import Grid


def generate_moves(grid: Grid, state: Tuple[int, int]) -> Iterable[Tuple[int, int]]:
    x, y = state

    if x < len(grid) - 1:
        yield x + 1, y

    if x > 0:
        yield x - 1, y

    if y < len(grid[0]) - 1:
        yield x, y + 1

    if y > 0:
        yield x, y - 1


def generate_downward_moves(
    grid: Grid, state: Tuple[int, int]
) -> Iterable[Tuple[int, int]]:
    x, y = state

    if x < len(grid) - 1:
        yield x + 1, y

    if y < len(grid[0]) - 1:
        yield x, y + 1
