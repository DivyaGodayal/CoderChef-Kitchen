class Solution(object):
    
    def toggle_row(self, A, r, c):
        for i in range(c):
            A[r][i] = 1 - A[r][i]
    
    def toggle_column(self, A, r, c):
        count = 0
        # Count the number of 0s in the column
        for i in range(r):
            if A[i][c] == 0:        
                count += 1
        # If we have more number of 0s than 1s in the column, we toggle it.        
        if count > r/2:        
            for i in range(r):
                A[i][c] = 1 - A[i][c]
    
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        
        # Number of rows and columns in the matrix
        r = len(A)
        c = len(A[0])
        
        # First, we check the rows.
        for i in range(r):
            # If a row has a 0 in the first column i.e. a 0 in the MSB of the binary number represented by the row, toggle it
            if A[i][0] == 0:
                self.toggle_row(A, i, c)
        
        # Then we try and toggle the columns
        for i in range(1, c):
            self.toggle_column(A, r, i)
            
        ans = 0    
        for i in range(r):
            # Converting the row to a string representation and getting the decimal equivalent of it. 
            ans += int("".join(map(str, A[i])),2)
        
        return ans
