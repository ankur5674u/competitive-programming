__author__ = "Ankur Prakash Singh"
# Date format "%m-%d-%Y"
__date__ = '08-09-2020'

from collections import deque


class Solution:
    @staticmethod
    def is_cell_valid(row, col, cell_i, cell_j):
        return (0 <= cell_i <= row - 1) and (0 <= cell_j <= col - 1)

    def orangesRotting(self, grid) -> int:
        q = deque()
        n, m = len(grid), len(grid[0])
        seen_fresh = 0
        longest_time = 0

        # Seeding queue and fresh counter
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))

                elif grid[i][j] == 1:
                    seen_fresh += 1

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            cell_i, cell_j, time = q.popleft()

            if grid[cell_i][cell_j] == 1:
                seen_fresh -= 1
                grid[cell_i][cell_j] = 2
                longest_time = max(longest_time, time)

            for nei_i, nei_j in neighbors:
                new_i, new_j = cell_i + nei_i, cell_j + nei_j

                if Solution.is_cell_valid(n, m, new_i, new_j) and grid[new_i][new_j] == 1:
                    q.append((new_i, new_j, time + 1))

        return longest_time if not seen_fresh else -1
