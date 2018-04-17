class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """

        # Get the intervals for each individual alphabet
        intervals_dicti = {}
        for index, char in enumerate(S):
            intervals_dicti.setdefault(char, []).append(index)

        # An interval is defined by the minimum and the maximum index. We are processing indexes in order.  
        # Hence, we don't sort to get the interval
        # eg:- "a" : [1,4,6,7,8] Therefore, the interval would be [1,8]
        intervals = []
        for key in intervals_dicti:
            intervals.append([intervals_dicti[key][0], intervals_dicti[key][-1]])

        # Sort the intervals by starting index
        intervals = sorted(intervals, key=lambda x: x[0]) # Sort by starting time
        # The first interval and hence the partition.
        current = intervals[0]
        ans = []
        for inter in intervals[1:]:
            if inter[0] < current[1]: # Overlap
                current[1] = max(current[1], inter[1]) # Extend the current interval
            else:
                # End the current partition, add it's length to the answer and start the next partition
                ans.append(current[1] - current[0] + 1)
                current = inter
        ans.append(current[1] - current[0] + 1)
        return ans

