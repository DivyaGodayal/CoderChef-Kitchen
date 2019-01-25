import heapq
from collections import Counter

class Node:

    # A node in the heap will contain two entries
    # A word and it's frequency. Since this is a custom
    # data type, we override the < and the == operators
    def __init__(self, word, frequency):
        self.freq = frequency
        self.word = word

    def __lt__(self, other):

        # For same frequencies, prefer the smaller word
        if self.freq == other.freq:
            return self.word < other.word

        # Otherwise, prefer the larger frequency word
        return self.freq > other.freq

    def __eq__(self, other):
        return other.freq == self.freq and other.word == self.word

class Solution:
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        # Build the initial frequency counter
        c = Counter(words)

        # Add all the words along with their frequencies to the heap
        new_list = [Node(word, freq) for word, freq in c.items()]

        # Heapify!
        heapq.heapify(new_list)

        # Extract K elements and return the final list.
        # Our overridden < and == operators ensure the validity of
        # extracting the top-K elements.
        return [heapq.heappop(new_list).word for _ in range(k)]


        
