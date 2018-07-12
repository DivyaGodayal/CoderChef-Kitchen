class MagicDictionary(object):
    
    """
        Given a word, generate all the possible structures for it
        For the word 'hello', we will have 
        
        *ello
        h*llo
        he*lo
        hel*o
        hell*
    """
    
    def _genneighbors(self, word):
        for i in xrange(len(word)):
            yield word[:i] + '*' + word[i+1:]

    # Process every word in the dictionary and create a Counter for all the neighbors of all the words.
    # A counter is not necessarily needed. We just need to store what all neighbors we have. 
    def buildDict(self, words):
        self.words = set(words)
        self.count = collections.Counter(nei for word in words
                                        for nei in self._genneighbors(word))
    
    # Search if any of the neighbors of the word appears in our dictionary.
    def search(self, word):
        return any(self.count[nei] > 1 or
                   self.count[nei] == 1 and word not in self.words
                   for nei in self._genneighbors(word))
