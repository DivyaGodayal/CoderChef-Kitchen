class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans_spiral_list = []
        
        index_i = 0
        index_j = 0
        
        rows = len(matrix)
        if rows == 0:
            return ans_spiral_list
        cols = len(matrix[0])
        total_elements = rows * cols
    
        # directions for right, down, left, up
        # thats the direction we follow to form a spiral
        directions = [(0,1),(1,0),(0,-1),(-1,0)] 
        
        di = 0
        count = 0
        
        # iterating in the spiral form till all the elements are printed
        while count < total_elements:
            # conditions to check for boundaries or already marked element.             
            while index_i >= 0 and index_i < rows and index_j >= 0  and index_j < cols and matrix[index_i][index_j] is not None:
                ans_spiral_list.append(matrix[index_i][index_j])
                # add none to mark an element as read or already in the spiral
                matrix[index_i][index_j] = None
                count += 1
                # updating the index as per the current direction
                index_i += directions[di][0]
                index_j += directions[di][1]
                
            # coming back to the boundaries 
            # if the index went across the boundaries
            index_i -= directions[di][0]
            index_j -= directions[di][1]
             
            # direction change for next iteration since one pass hit the boundary
            # pick the next direction from the directions array 
            # foreg. if we were going right, now we would change the direction and go down.
            di = (di + 1) % 4
            index_i += directions[di][0]
            index_j += directions[di][1]
            
        return ans_spiral_list
                
                
