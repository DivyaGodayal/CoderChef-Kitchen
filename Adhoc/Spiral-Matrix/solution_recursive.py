class Solution:
    
    def answer(self, matrix, start_r, start_c, end_r, end_c):
        if start_r > end_r or start_c > end_c:
            return []
        
        ans = []
        i = start_r; j = start_r
        increments = [(0, 1, start_r + 1, end_c), (1, 0, end_r, end_c - 1), (0, -1, end_r - 1, start_c), (-1, 0, 0, 0)]
        increment_index = 0
        while True:
            ans.append(matrix[i][j])
            i += increments[increment_index][0]
            j += increments[increment_index][1]
            
            if i == start_r and j == start_c:
                break
            
            if not (i >= start_r and i <= end_r and j >= start_c and j <= end_c):
                increment_index += 1
                i = increments[increment_index - 1][2]
                j = increments[increment_index - 1][3]
                
                if not (i >= start_r and i <= end_r and j >= start_c and j <= end_c) or (i == start_r and j == start_c):
                    break
                
        ans.extend(self.answer(matrix, start_r + 1, start_c + 1, end_r - 1, end_c - 1))    
        return ans
    
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix:
            return []
        
        return self.answer(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)
                
