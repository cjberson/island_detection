import csv
import random
import time
from copy import deepcopy
from typing import Callable, Tuple, List

from BreadthFirstSearchNextLand import bfs_next_land, bfs_next_land_with_node_count
from BreadthFirstSearchVisitOnce import (
    bfs_visit_once,
    bfs_visit_once_with_node_count,
)
from Constants import WATER, LAND, Grid
from BreadthFirstSearchOnLand import (
    bfs_on_land,
    bfs_on_land_with_node_count,
)


def test():
    name_to_method = {
        "bfs_on_land": bfs_on_land,
        "bfs_visit_once": bfs_visit_once,
        "bfs_next_land": bfs_next_land,
    }

    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    grid3 = [
        ["1", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "1"],
        ["0", "0", "0", "0", "1"],
        ["0", "0", "0", "0", "1"],
    ]
    grid4 = [
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "1"],
        ["0", "0", "0", "0", "1"],
        ["0", "0", "0", "0", "1"],
    ]
    grid5 = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"],
    ]
    grid6 = [
        ["1", "1", "1", "0", "0"],
        ["0", "1", "0", "1", "1"],
        ["0", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
    ]
    grids = [grid1, grid2, grid3, grid4, grid5, grid6]

    for name, method in name_to_method.items():
        print("--- " + name + " ---")
        for grid in grids:
            print(method(deepcopy(grid)))


def random_tests_with_stat_collection_for_all(
    num_tests: int, min_size: int, max_size: int
):
    name_to_method = {
        "bfs_on_land": bfs_on_land_with_node_count,
        "bfs_visit_once": bfs_visit_once_with_node_count,
        "bfs_next_land": bfs_next_land_with_node_count,
    }

    for name, method in name_to_method.items():
        random_tests_with_stat_collection(num_tests, min_size, max_size, name, method)


def random_tests_with_stat_collection(
    num_tests: int,
    min_size: int,
    max_size: int,
    filename: str,
    solve_with_node_count: Callable[[List[List[str]]], Tuple[int, int]],
):
    tests_file = open(filename + ".txt", "w")

    with open(filename + ".csv", "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(
            [
                "Problem Number" "Width",
                "Height",
                "Number Islands",
                "Nodes Visited",
                "Time (ms)",
                "Max Memory (MiB)",
            ]
        )

        total_width = 0
        total_height = 0
        total_num_islands = 0
        total_num_nodes_visited = 0
        total_time = 0

        test_num = 1

        while test_num <= num_tests:
            width = random.randint(min_size, max_size)
            height = random.randint(min_size, max_size)
            grid = generate_random_grid(width, height)
            tests_file.write("Test " + str(test_num) + "\n")
            tests_file.write(
                "\n".join(["".join([cell for cell in row]) for row in grid])
            )
            tests_file.write("\n\n")

            t0 = time.time_ns() / 1000000
            num_islands, num_nodes = solve_with_node_count(grid)
            t1 = time.time_ns() / 1000000
            t = t1 - t0

            total_width += width
            total_height += height
            total_num_islands += num_islands
            total_num_nodes_visited += num_nodes
            total_time += t

            csvwriter.writerow([test_num, width, height, num_islands, num_nodes, t])

            test_num += 1

        csvwriter.writerow([])
        csvwriter.writerow(
            [
                "Total Tests",
                "Average Width",
                "Average Height",
                "Average Number Islands",
                "Average Nodes Visited",
                "Average Time (ms)",
            ]
        )

        csvwriter.writerow(
            [
                num_tests,
                total_width / num_tests,
                total_height / num_tests,
                total_num_islands / num_tests,
                total_num_nodes_visited / num_tests,
                total_time / num_tests,
            ]
        )
    tests_file.close()


def generate_random_grid(width: int, height: int) -> Grid:
    grid = [[WATER] * width for _ in range(height)]

    chance_for_land = random.random()

    for i in range(height):
        for j in range(width):
            r = random.random()
            if r <= chance_for_land:
                grid[i][j] = LAND

    return grid


if __name__ == "__main__":
    random_tests_with_stat_collection_for_all(1000, 50, 100)
