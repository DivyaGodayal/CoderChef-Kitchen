class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # Map for holding the bitmasks for all the words.
        map_ = {}
        for w in words:
            # Initial mask is all 0's. We have to use the bitwise OR operator
            # to mark the bits corresponding to the characters.
            mask = 0

            # Preparing the bitmask for the word "w"
            for c in w:
                mask |= (1 << (122 - ord(c)))
            map_[w] = mask

        N = len(words)
        ans = 0
        for i in range(N):
            for j in range(i + 1, N):

                # Simply use bitwise AND to check for intersection.
                if not (map_[words[i]] & map_[words[j]]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans            
