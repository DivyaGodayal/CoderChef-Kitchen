class UnionFind:
    def __init__(self, grid, R, C):

        # The parent array for each cell in the matrix
        self.parent = [i for i in range(R*C)]

        # rank array to be used by 'Union-by-Rank'
        self.rank = [0 for _ in range(R*C)]
        self.C = C

        # Initial number of components. The number of components reduce by 1
        # everytime a union is performed
        self.components = sum([int(grid[i][j]) for i in range(R) for j in range(C)])

    """
        returns the index for a cell given it's row and column num.
    """
    def get_index(self, r, c):
        return r*self.C + c

    """
        returns the parent of a cell recursively.
        Employs path compression for optimization
    """
    def get_parent(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.get_parent(self.parent[i])
        return self.parent[i]

    """
        Perform union of two disjoint sets.
        Used Union-by-Rank for optimization
    """
    def union(self, A, B):
        pA, pB = self.get_parent(A), self.get_parent(B)

        # Only perform union of disjoint sets.
        if pA == pB:
            return

        # Get the rank of two sets.
        # Add shorter set to larger set. This won't affect the overall
        # "height"
        rA, rB = self.rank[pA], self.rank[pB]
        if rA > rB:
            self.parent[pB] = pA
        elif rA < rB:
            self.parent[pA] = pB
        else:
            self.parent[pA] = pB
            self.rank[pB] = rB + 1

        # Reduce the number of components.
        self.components -= 1

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if not grid:
            return 0

        R, C = len(grid), len(grid[0])
        uf = UnionFind(grid, R, C)
        for i in range(R):
            for j in range(C):
                # for each valid cell, perform union with the neighbors.
                # This is not a recursive process. Hence, we don't mark the nodes
                # as processed per-say.
                if grid[i][j] == "1":
                    I = uf.get_index(i, j)
                    if i < R - 1 and grid[i + 1][j] == "1":
                        uf.union(I, uf.get_index(i + 1, j))
                    if i > 0 and grid[i - 1][j] == "1":
                        uf.union(I, uf.get_index(i - 1, j))
                    if j < C - 1 and grid[i][j + 1] == "1":
                        uf.union(I, uf.get_index(i, j + 1))
                    if j > 0 and grid[i][j - 1] == "1":
                        uf.union(I, uf.get_index(i, j - 1))
        return uf.components
