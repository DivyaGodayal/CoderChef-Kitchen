class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        
        # Sort the video clips by their starting times
        clips.sort()
        
        prev_end = 0
        N, idx, cnt = len(clips), 0, 0
        
        # Keep iterating until we don't have any more video clips left 
        # or we are done covering the entire range [0, T]
        while prev_end < T and idx < N:
            
            current_start, current_end = clips[idx]
            
            # If we can't extend the current range, we return -1
            # This checks for no overlap
            if current_start > prev_end:
                return -1
            
            # Find the video clip that gives the maximum extension to the current range
            max_extension = 0
            while idx < N and clips[idx][0] <= prev_end:
                max_extension = max(max_extension, clips[idx][1])
                idx += 1
            
            # Update the range accordingly
            prev_end = max_extension
            
            # Increment number of video clips
            cnt += 1
        
        return cnt if prev_end >= T else -1