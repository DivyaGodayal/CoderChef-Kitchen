from collections import defaultdict
class Solution:
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        
        # Base case if the starting and ending bus stops are the same.
        if S == T:
            return 0
        
        # Create a set out of every bus route's stops.
        R = [set(r) for r in routes]
        
        # The BFS queue.
        Q = []
        
        # Don't add already visited nodes back to the queue.
        visited = {}
        
        # Adjacency list for our custom graph.
        graph = defaultdict(list)
        
        # For every bus route
        for i in range(len(R)):
            
            # If the starting bus stop is a part of this bus route, add it to the queue with level 1 (one bus ) and also mark as visited
            if S in R[i]:
                visited[i] = 1
                Q.append((i, 1))
            
            # Iterate on the remaining routes
            for j in range(i + 1, len(routes)):
                
                # If these two routes share any bus stop, then add an edge betweenn them
                if R[j]&R[i]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        # The BFS algorithm
        while Q:
            bus_route, level = Q.pop(0)
            
            # If our final stop is a part of this route, then return the `level` value which is the number of buses boarded till now.
            if T in R[bus_route]:
                return level
            
            # If this bus route is connected to some other bus routes.
            if bus_route in graph:
                
                # For all the connected bus routes to the current one.
                for neighbor in graph[bus_route]:
                    
                    # If this neighboring bus route (node) has not been processed till now, process it.
                    if neighbor not in visited:
                        visited[neighbor] = 1
                        
                        # Since we are changing the bus when jumping to another bus route, increase the level value
                        Q.append((neighbor, level + 1))
                        
        return -1                
            
        
