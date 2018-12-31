class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # Empty grid
        if not grid:
            return 0

        R, C = len(grid), len(grid[0])
        def dfs(r, c):

            # Cell within boundary and has a value of "1" implying an island
            if r >= 0 and r < R and c >= 0 and c < C and grid[r][c] == "1":

                # Mark it as processed
                grid[r][c] = "-1"

                # Recurse on 4 directions
                dfs(r + 1, c) # DOWN
                dfs(r - 1, c) # UP
                dfs(r, c + 1) # RIGHT
                dfs(r, c - 1) # LEFT

        c = 0
        for i in range(R):
            for j in range(C):

                # If we have an unprocessed node, call dfs, record it as a
                # connected component
                if grid[i][j] == "1":
                    dfs(i, j)
                    c += 1

        return c
