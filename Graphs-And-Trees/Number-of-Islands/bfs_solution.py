class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        R, C = len(grid), len(grid[0])
        def bfs(r, c):

            # Initialize the BFS queue with the first node.
            Q = [(r, c)]
            while Q:
                i, j = Q.pop(0)

                # DOWN
                if i < R - 1 and grid[i + 1][j] == "1":
                    grid[i + 1][j] = "-1"
                    Q.append((i + 1, j))

                # UP
                if i > 0 and grid[i - 1][j] == "1":
                    grid[i - 1][j] = "-1"
                    Q.append((i - 1, j))

                # RIGHT
                if j < C - 1 and grid[i][j + 1] == "1":
                    grid[i][j + 1] = "-1"
                    Q.append((i, j + 1))

                # LEFT
                if j > 0 and grid[i][j - 1] == "1":
                    grid[i][j - 1] = "-1"
                    Q.append((i, j - 1))

        c = 0
        for i in range(R):
            for j in range(C):
                # If this node is still unprocessed, process it and call BFS.
                if grid[i][j] == "1":
                    grid[i][j] = "-1"
                    bfs(i, j)
                    c += 1

        return c
