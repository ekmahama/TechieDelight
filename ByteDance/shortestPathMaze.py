from collections import deque, defaultdict


class Solution:
    def shortestPath(self, grid, k):
        # if empty grid
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        visited = defaultdict(lambda: -1)
        visited[(0, 0)] = k
        queue = deque()
        queue.append((0, 0, k))
        steps = 0

        while queue:
            level_len = len(queue)
            for _ in range(level_len):
                x, y, k = queue.popleft()

                if x == row - 1 and y == col - 1:
                    return steps

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    nk = k - grid[x][y]

                    if nk < 0:
                        continue
                    # out of bounds
                    if nx < 0 or ny < 0 or nx == row or ny == col:
                        continue

                    if nk <= visited[(nx, ny)]:
                        continue

                    queue.append((nx, ny, nk))
                    visited[(nx, ny)] = nk
            steps += 1
        return -1


k = 1
examp = Solution()

arr = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
res = examp.shortestPath(arr, k)
