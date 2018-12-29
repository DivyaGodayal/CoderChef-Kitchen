from collections import Counter
class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # Create a Map of the word to a set of
        # characters. We use set because we need set intersection later on
        map_ = {}
        for w in words:
            map_[w] = set(Counter(w).keys())

        ans = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                # For every pair of words, see if their character sets have an intersection
                # If there's no intersection, they're a candidate
                if not map_[words[i]].intersection(map_[words[j]]):
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans            
