import heapq
from collections import Counter

class Node:

    # A node in the heap will contain two entries
    # A word and it's frequency. Since this is a custom
    # data type, we override the < and the == operators
    def __init__(self, frequency, word):
        self.freq = frequency
        self.word = word

    def __lt__(self, other):

        # For same frequencies, prefer the larger word
        if self.freq == other.freq:
            return self.word > other.word

        # Otherwise, prefer the smaller frequency word
        return self.freq < other.freq

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

        # Empty heap initialization
        heap = []

        # Process each word of the frequency counter
        for word, freq in c.items():
            heapq.heappush(heap, Node(freq, word))

            # As soon as we have k+1 elements, pop the minimum
            if len(heap) > k:
                heapq.heappop(heap)

        # Obtain the remaining k elements. They will be in
        # reverse order since we have a min-heap. Hence, we reverse them
        final = [heapq.heappop(heap).word for _ in range(k)]
        return final[::-1]

        
