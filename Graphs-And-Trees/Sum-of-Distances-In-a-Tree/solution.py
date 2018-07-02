class Solution(object):
    def reinitialise(self):
        self.parent = {}
        self.adj_list = {}
        self.distances_down = {}
        self.num_of_paths_down = {}
        self.visited = {}
        self.answer = {}
        self.N = 0
        
    def add_children(self, parent, child):
        if parent not in self.adj_list:
            self.adj_list[parent] = []
        self.adj_list[parent].append(child)    
        
    """
        This function finds out the answer to the question but only for the tree rooted at the given vertex. 
        Basically, it finds the following 2 things
        
        1. Number of nodes in the tree rooted at the given vertex (Number of nodes = Number of paths going down)
        2. Sum of all paths starting from given vertex as root and going down.
        
        Complexity O(N)
    """    
    def recurse(self, vertex):
        self.visited[vertex] = 1
        root_to_children_paths = 0
        sum_of_paths = 0
        for child in self.adj_list[vertex]:
            if child not in self.visited:
                self.parent[child] = vertex
                n_paths, s_paths = self.recurse(child)
                root_to_children_paths += n_paths + 1
                sum_of_paths += n_paths + s_paths + 1
        
        self.distances_down[vertex] = sum_of_paths
        self.num_of_paths_down[vertex] = root_to_children_paths
        return root_to_children_paths, sum_of_paths       
    
    """ 
        This will help us find the actual answer for all the given vertices. 
        We use the answers we have for the parent of the given vertex and then return the answers accordingly.
        
        Complexity O(N) since we used DP 
    """
    def find_distances(self, vertex):
        """ MEMOIZATION """
        if vertex in self.answer:
            return self.answer[vertex]
        
        sum_of_paths = self.find_distances(self.parent[vertex]) if vertex in self.parent else 0
        num_of_paths = self.N - 1
        own_answer = self.distances_down.get(vertex, 0)
        
        if sum_of_paths > 0:
            num_of_paths = num_of_paths - self.num_of_paths_down[vertex]
            sum_of_paths = sum_of_paths - self.distances_down[vertex] - self.num_of_paths_down[vertex] - 1
            own_answer += num_of_paths + sum_of_paths
        
        self.answer[vertex] = own_answer
        return self.answer[vertex]
    
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        self.reinitialise()
        
        if N == 1:
            return [0]
        
        self.N = N
        for s, d in edges:
            self.add_children(s, d)
            self.add_children(d, s)
        
        self.recurse(0)  
        ans = []
        print(self.distances_down[2], self.num_of_paths_down[2])
        for i in range(N):
            ans.append(self.find_distances(i))
        
        return ans
        
