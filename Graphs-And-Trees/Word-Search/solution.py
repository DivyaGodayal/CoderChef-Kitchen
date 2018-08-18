class Solution(object):
    

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def recurseWord(index_x, index_y, length):
            # If the length of the word created so far is equal to the length of the searched word, then return True.
            if length == len(word):
                return True
            # Board bounds check.
            if index_x < 0 or index_y < 0 or index_x >= len(board) or index_y >= len(board[0]):
                return False 
            # If the letter in the current cell is not in the word then return False.
            letter = board[index_x][index_y]
            if letter != word[length]:
                return False          
            # To mark the cell visited for, put a # character
            # Since this cell should not be repeated for the given word.
            board[index_x][index_y] = '#'
            
            # Recursively call in all the 4 directions from this cell. 
            # DFS approach.
            ans = recurseWord(index_x + 1, index_y, length+1) 
            ans = ans or recurseWord(index_x, index_y + 1, length+1)
            ans = ans or recurseWord(index_x - 1, index_y, length+1)
            ans = ans or recurseWord(index_x, index_y - 1, length+1)
            
            # Once the current call has completed put back the character.
            board[index_x][index_y] = letter           
            return ans
        
        answer = False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                # Starting for the word from every cell in the grid, one by one.
                if recurseWord(i, j, 0):
                    return True
        return answer
                
                
       
            