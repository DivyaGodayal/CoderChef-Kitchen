class Solution:
    
    # If the cell (r,c) is within boundaries, is not visited and has a value = 1, it is valid
    def is_valid(self, r, c, x, y, visited, grid):
        if x >= 0 and x < r:
            if y >= 0 and y < c:
                if (x, y) not in visited:
                    if grid[x][y] == 1:
                        return True
        return False    
    
    # Dfs recurses on all 4 sides
    def dfs(self, grid, x, y, visited, dfs_number):
        if self.is_valid(len(grid), len(grid[0]), x, y, visited, grid):
            visited[(x, y)] = dfs_number
            self.dfs(grid, x + 1, y, visited, dfs_number)
            self.dfs(grid, x, y + 1, visited, dfs_number)
            self.dfs(grid, x - 1, y, visited, dfs_number)
            self.dfs(grid, x, y - 1, visited, dfs_number)
    
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # The visited dictionary to mark if a cell has been seen before or not. 
        # Instead of storing true or false, we store the dfs number in which this cell was visited. We will perform multiple
        # dfs operations given that there might be multiple separate islands (disconnected graph components)
        visited = {}
        
        # Stores, for every cell, what was the size of the island it was part of.
        largest = {}
        
        # Stores the count of nodes visited in a particular dfs. 
        dfs_count = {}
        
        # The dfs number starts from 0 and gets incremented by 1 everytime we see a node that wasn't visited previously.
        dfs_number = 0
        
        # Stores the number of nodes in the visited dictionary before performing the dfs. We use this to find out number of nodes visited int the current dfs.
        prev_count = 0
        
        # Largest island there is.
        ans = -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                # If we find a cell that has 1 in it and if it hasn't been visited befor
                if grid[i][j] == 1 and (i, j) not in visited:
                    
                    # Perform dfs starting from this cell. Pass the dfs_number variable. That would be stored in the visited dictionary for all the cells visited in this dfs. 
                    self.dfs(grid, i, j, visited, dfs_number)
                    
                    # Number of nodes visited in this particular dfs
                    dfs_count[dfs_number] = len(visited) - prev_count
                    
                    # Updated to reflect number of nodes in all that have been visited till now
                    prev_count = len(visited)
                    
                    # Increment this for the next dfs we would perform
                    dfs_number += 1
                
                # Largest stores the island size this cell belonged to, if it was 1, otherwise it belongs to no island.
                if grid[i][j] == 1:
                    largest[(i, j)] = dfs_count[visited[(i, j)]]
                else:
                    largest[(i, j)] = 0
                    
                ans = max(ans, largest[(i, j)])    
                       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                # Every 0 is a potential candidate to flip. 
                if grid[i][j] == 0:
                    current = 0
                    
                    # Set to store which island has been covered.
                    done = set()
                    
                    # If the cell down below i.e. (i + 1, j) is a valid cell and if the island that it belongs to has not already been covered, then add its size to the current size and mark that island as visited. 
                    if (i+1) < len(grid) and grid[i+1][j] == 1 and visited[(i+1, j)] not in done:
                        current += largest[(i + 1, j)]
                        done.add(visited[(i+1, j)])
                    
                    # If the cell to the top i.e. (i - 1, j) is a valid cell and if the island that it belongs to has not already been covered, then add its size to the current size and mark that island as visited. 
                    if (i-1) >= 0 and grid[i-1][j] == 1 and visited[(i-1, j)] not in done:
                        current += largest[(i - 1, j)]
                        done.add(visited[(i-1, j)])
                        
                    # If the cell to the right i.e. (i, j + 1) is a valid cell and if the island that it belongs to has not already been covered, then add its size to the current size and mark that island as visited.     
                    if (j+1) < len(grid[0]) and grid[i][j+1] == 1 and visited[(i, j+1)] not in done:
                        current += largest[(i, j + 1)]
                        done.add(visited[(i, j+1)])
                        
                    # If the cell to the left i.e. (i, j - 1) is a valid cell and if the island that it belongs to has not already been covered, then add its size to the current size and mark that island as visited.     
                    if (j-1) >= 0 and grid[i][j-1] == 1 and visited[(i, j-1)] not in done:
                        current += largest[(i, j - 1)]    
                        done.add(visited[(i, j-1)])
                    
                    # Record the maximum answer till now. The +1 is because we have flipped the cell (i, j) as well.
                    ans = max(ans, current + 1)
        return ans            
                    
                    
