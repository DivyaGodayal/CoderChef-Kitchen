import heapq
from collections import Counter


class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        """

        """ 
            This will count the frequency of individual tasks 
            in the list of given tasks and provide a dictionary 
            for the same 
        """
        freq = Counter(tasks)

        """ Create a Max Heap using the frequencies. We negate the values so as to get the max heap property. """
        heaplist = [(-freq[key], key) for key in freq]
        heapq.heapify(heaplist)

        interim_list = []
        steps = 0
        is_non_zero = False

        """ Continue until the heap is not empty.  """
        while heaplist:
            i = 0

            """ Pop until the heap finishes or until n+1 elements have been popped. n being the interval """
            while i <= n:
                if heaplist:
                    """ 
                        pop an element from the heap 
                        and add to a temporary list 
                        with updated frequency. Note 
                        the addition because we took 
                        negative frequency values initially 
                    """
                    frequency, character = heapq.heappop(heaplist)
                    if frequency + 1 < 0:
                        """ boolean variable to tell us if any non zero element is left or not. If not, then we are done """
                        is_non_zero = True
                    interim_list.append((frequency + 1, character))
                else:
                    break
                i += 1
            """ Note, the number of steps is always (n+1) except in the last stretch.  """
            steps += n + 1 if is_non_zero else i

            """ 
                Push elements from interim list 
                back to the heap. Note that we 
                only push the elements back if 
                they have non zero freequency.  
            """
            for element in interim_list:
                if element[0] < 0:
                    heapq.heappush(heaplist, element)
            interim_list = []
            is_non_zero = False
        return steps
