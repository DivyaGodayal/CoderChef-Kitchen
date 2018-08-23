from collections import Counter
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""
        
        # Dictionary which keeps a count of all the unique characters in t.
        dict_t = Counter(t)
        
        # Number of unique characters in t, which need to be present in the desired window.
        required = len(dict_t)
        
        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        filtered_s = []
        for i, char in enumerate(s):
            if char in dict_t:
                filtered_s.append((i, char))
        
        # left and right pointers
        l, r = 0, 0
        
        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # Foreg. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0
        
        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}
        
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None
        
        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(filtered_s):
            
            # Add one character from the right to the window
            character = filtered_s[r][1]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if window_counts[character] == dict_t[character]:
                formed += 1
        
            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and formed == required:
                character = filtered_s[l][1]
                
                # Save the smallest window until now.
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                if end - start + 1 < ans[0]:
                    ans = (end - start + 1, start, end)
                    
                # Move the left pointer ahead, this would help to look for a new window.
                window_counts[character] -= 1
                if window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    
                
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1] 
        
