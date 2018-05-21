class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        # Dictionary to stored already solved equations.
        solved = {}
        
        # A dictionary to store all the denominators given a numerator. 
        num_to_denom = {}
        
        # A set of all the alphabets encountered in the numerator and the denominator.
        seen = set()
        
        # Iterating over the input
        for eq, val in zip(equations, values):
            
            # Add the num and denom to the seen set.
            seen.add(eq[0])
            seen.add(eq[1])
            
            # If we are given a / b, then we also have b / a. Store these values in the solved dictionary.
            solved[(eq[0], eq[1])] = val
            solved[(eq[1], eq[0])] = 1 / val
            
            # Store the denominator corresponding to the numerator. Do this for a / b and b / a both even though we were only given a / b
            if eq[0] not in num_to_denom:
                num_to_denom[eq[0]] = []
            if eq[1] not in num_to_denom:
                num_to_denom[eq[1]] = []    
            num_to_denom[eq[0]].append((eq[1], val))
            num_to_denom[eq[1]].append((eq[0], 1 / val))
        
        # Visited dictionary for dfs to prevent loops.
        visited = {}    
        def dfs(d, den):
            if d == den:
                return float(1)
            
            result = float(-1)
            
            # If we have d as the numerator in atleast one of the equations given.
            if d in num_to_denom:
                # Iterate over all its denominators
                for child, val in num_to_denom[d]:
                    # If not already visited, mark visited and recurse
                    if child not in visited:
                        visited[child] = 1
                        
                        # We have n / d and now we are recursing on d / k. We get n / k
                        result = dfs(child, den)
                        
                        # We found the answer :)
                        if result != float(-1):
                            return result * val
            return result    
            
        ans = []    
        for q in queries:
            num = q[0]
            den = q[1]
            # Base Case #1
            if (num, den) in solved:
                ans.append(solved[(num, den)])
            # Base Case #2    
            elif num not in seen or den not in seen:
                ans.append(float(-1))
            else:
                # Clear the visited dictionary before every dfs call.
                visited.clear()
                visited[num] = 1
                ans.append(dfs(num, den))
                
        
        
        return ans
        
