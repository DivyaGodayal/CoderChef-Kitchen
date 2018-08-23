from collections import Counter
class Solution(object):
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
    
        # Left pointer
        l = 0
        # Right pointer
        r = 0 
        # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
        # Foreg. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
        formed = 0
        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = {}
        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None
        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            
            while l <= r and formed == required:
                character = s[l]
                # Save the smallest window until now.
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                # Move the left pointer ahead, this would help to look for a new window.
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1    
                
            r += 1    
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]    