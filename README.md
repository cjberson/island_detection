# Island Detection
Given a grid of strings of 1s and 0s, detect the number of islands where an island is defined as 1s surrounding by 0s.

The best solution I imeplemented is [Breadth-First Search Next Land](https://github.com/cjberson/island_detection/blob/main/BreadthFirstSearchNextLand.py). It cuts down the amount of nodes visited as compared to Leet Code's solution. You can checkout the performance difference by looking at the average stats at the bottom of each approach's associated `.csv` files that are produces by running main (it ran through 1000 randomly generated grids of with minimum and maximum dimensions of 50 to 100 respectively and collected average stats).
