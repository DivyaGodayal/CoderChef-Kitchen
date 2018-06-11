class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for i in range(rows):
                # Storing if the first column needs to be set to 0. Special handling for this because the first element
                # of the first row and the first column is the same i.e. matrix[0][0]
                if matrix[i][0] == 0:
                    is_col = True
                for j in range(1,cols):
                    # If an element is zero, we set the first element of the corresponding row and column to 0
                    if matrix[i][j]  == 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0

            # Use the information stored in first column to set entire row(s) to zero
            for i in range(1,rows):
                    if matrix[i][0] == 0:
                        for j in range(1,cols):
                            matrix[i][j] = 0

            # Use the information stored in first row to set entire column(s) to zero
            for j in range(1,cols):
                    if matrix[0][j] == 0:
                        for i in range(1,rows):
                            matrix[i][j] = 0

            # See if the first row needs to be set to zero as well
            if matrix[0][0] == 0:
                for j in range(cols):
                    matrix[0][j] = 0

            # See if the first column needs to be set to zero as well        
            if is_col:
                for i in range(rows):
                    matrix[i][0] = 0
