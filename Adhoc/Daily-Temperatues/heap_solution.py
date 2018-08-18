import heapq
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        # The heap used in the algorithm
        min_heap = []

        # Final answers array that we will return. This will contain, for every index, how far is the next warmer day.
        ans = [0] * len(temperatures)

        # Insert the first temperature and it's index into the min-heap
        # We insert a tuple of (value, index). The value is used to construct the heap.
        heapq.heappush(min_heap, (temperatures[0], 0))

        # Iterate on the remaining temperatures.
        for index,temp in enumerate(temperatures[1:]):

            # Keep removing smaller elements from the heap and assign the next warmer day accordingly
            while min_heap and temp > min_heap[0][0]:    
                ans[min_heap[0][1]] = index+1 - min_heap[0][1]
                heapq.heappop(min_heap)

            # Add the current temperature to the heap and continue
            heapq.heappush(min_heap, (temp, index+1))
            
                               
        return ans
