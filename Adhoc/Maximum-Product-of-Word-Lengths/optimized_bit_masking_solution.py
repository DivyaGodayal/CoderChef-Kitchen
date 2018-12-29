class Solution:
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # Map for mask to the longest word having that mask
        map_ = {}
        for w in words:
            mask = 0

            # Preparing the mask for the current word
            for c in w:
                mask |= (1 << (122 - ord(c)))

            # Update the longest word for this mask
            map_[mask] = max(map_.get(mask, 0), len(w))

        N = len(words)
        ans = 0

        # Simply iterate over the masks and not the words
        # This cuts down on the overall complexity
        for m1 in map_:
            for m2 in map_:
                # If there's no intersection between the two masks, then
                # we can use the longest words corresponding to the two masks
                if not (m1 & m2):
                    ans = max(ans, map_[m1] * map_[m2])
        return ans            
