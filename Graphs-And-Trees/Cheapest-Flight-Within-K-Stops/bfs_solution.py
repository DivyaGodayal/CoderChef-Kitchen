from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        
        adj_list = defaultdict(list)
        for s, d, cost in flights:
            adj_list[s].append((d, cost)) 
        
        min_cost = {k: float("inf") for k in range(n)}
        min_cost[src] = 0
        queue = [src]
        stops = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                element = queue.pop(0)
                cost = min_cost[element]
                
                # No need to process children of the destination node. 
                if element == dst:
                    continue
                
                # If this node has any neighbors
                if element in adj_list:
                    for neighbor, direct_flight_cost in adj_list[element]:
                           
                        # No need to update the minimum cost if we have already exhausted our K stops. 
                        if stops == K and neighbor != dst:
                            continue
                        
                        # Improve the cost if it can be improved and add back to the queue.
                        if  direct_flight_cost + cost <  min_cost[neighbor]:
                            min_cost[neighbor] = direct_flight_cost + cost
                            queue.append(neighbor)
            stops += 1                
        return -1 if min_cost[dst] == float("inf") else  min_cost[dst]                        

