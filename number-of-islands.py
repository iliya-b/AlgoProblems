from random import randint
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        p = [0] * (m * n)

        def make_set(x):
            p[x] = x

        def find(x):
            if p[x] == x:
                return x
            p[x] = find(p[x])
            return p[x]

        def unite(x, y):
            x = find(x)
            y = find(y)
            if randint(0, 1) == 0:
                p[x] = y
            else:
                p[y] = x

        for i in range(m):
            for j in range(n):
                x = i * n + j
                if grid[i][j] == '0':
                    p[x] = n * m + 1
                    continue
                make_set(x)

                if i > 0 and grid[i - 1][j] == '1':
                    unite(x, (i - 1) * n + j)
                if j > 0 and grid[i][j - 1] == '1':
                    unite(x, i * n + j - 1)

        roots = 0
        for i, x in enumerate(p):
            if i == x:
                roots += 1
        return roots
