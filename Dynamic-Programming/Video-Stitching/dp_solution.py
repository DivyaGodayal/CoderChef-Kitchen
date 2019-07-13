class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        
        N = len(clips)
        memo = {}
        
        # Sort the video clips by their starting times
        clips.sort()
        
        # Recursive function
        def recurse(index, prev_end):
            
            # If we have already covered the required range, we don't need any more video clips
            if prev_end >= T:
                return 0
            
            # If there are no more video clips left or
            # we can't extend the current range any further, return a large 
            # value since we are minimising
            if index == N or clips[index][0] > prev_end:
                return N + 1
            
            # Check for cached results
            if (index, prev_end) in memo:
                return memo[(index, prev_end)]
            
            # Skip the current video clip and move ahead
            ans = recurse(index + 1, prev_end)
            
            # Valid candidate which extends the current overlap
            if clips[index][0] <= prev_end and clips[index][1] > prev_end:
                ans = min(ans, recurse(index + 1, clips[index][1]) + 1)
            
            # Cache the solution
            memo[(index, prev_end)] = ans
            return ans
        
        ans = recurse(0, 0)
        return ans if ans <= N else -1