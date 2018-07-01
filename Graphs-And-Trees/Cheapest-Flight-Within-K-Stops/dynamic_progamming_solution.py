class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        
        # The adjacency matrix for the given graph network
        reachability_matrix = {}
        for i, j, c in flights:
            # Flight from i --> j with cost c
            if j not in reachability_matrix:
                reachability_matrix[j] = []
            reachability_matrix[j].append((i, c)) # j is reachable from i with cost c
        
        # Initialize the dynamic programming table with MAX values
        dp = [[float("inf") for _ in range(n)] for _ in range(K + 1)] 
        
        # The first loop is over the number of stops, because
        # to get an answer for k stops, we need all the answers for k - 1 stops.
        for k in range(K+1):
            
            # Base case for any value of k
            dp[k][src] = 0
            
            # Iterate over all the nodes
            for j in range(n):
                # If node `j` has neighbors, iterate over them
                if j != src and j in reachability_matrix:
                     for origin, cost in reachability_matrix[j]: 
                            # If no stops are allowed i.e. k == 0, then the minimum cost is that of the edge connecting the two nodes.
                            if k == 0:
                                if origin == src:
                                    dp[k][j] = min(dp[k][j], cost)
                            else:    
                                # Minimum cost is the minimum of current value of from the path from `origin` node. 
                                dp[k][j] = min(dp[k][j], cost + dp[k - 1][origin])
        return -1 if dp[k][dst] == float("inf") else dp[k][dst]                   
