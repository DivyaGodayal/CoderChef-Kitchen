class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.position_hash = {}
        self.hashwa = {}
        self.min = float("inf")
        self.max = -1

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        
        # Process every word in the dictionary
        for w in dict:
            # Find the minimum length of any word
            self.min = min(self.min, len(w))
            
            # Find the maximum length of any word
            self.max = max(self.max, len(w))
            
            # Iterate over every character, location in the word
            for pos, char in enumerate(w):
                
                # If no character was found at this location, create a new set()
                if pos not in self.position_hash:
                    self.position_hash[pos] = set()
                
                # Add this character to the characters' set for this location. Note: the usage of a set here.
                self.position_hash[pos].add(char)
            
            # Storing the actual word as well
            self.hashwa[w] = 1    
        
    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        length = len(word)
        # If the word doesn't obey our minimum and maximum length requirements, then False
        if length >= self.min and length <= self.max:
            # Iterate over every location in the search word.
            for i in range(length):
                # Iterate over all possible characters in this location from our dictionary
                for char in self.position_hash[i]:
                    # If this new modified string is in the dictionary, return True
                    if char != word[i] and (word[:i] + char + word[i+1:]) in self.hashwa:
                        return True
        return False            


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
