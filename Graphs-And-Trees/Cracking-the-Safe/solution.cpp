#include <vector>
#include <unordered_map>
#include <math>

class Solution {
public:
    bool recurse(int k, string& ans, string& current, unordered_map<string, bool>& done, int n) {
        // If the number of passwords considered is equal to what we want, then we are done. 
        if (done.size() == pow(k, n)) {
            return true;
        }
        
        current = current.substr(1); // Substring from 1 onwards. Ignore the first character
        
        // Required in C++ to extend the size of string by 1.
        current.append("#");
        for(int i = 0; i < k; i++) {
            // Try out all possible digits at the last position
            current[current.size() - 1] = to_string(i)[0];
            
            // If we have not considered the current password, then process it. 
            if (done.find(current) == done.end() || done[current] == false)  {
                ans.append(to_string(i));
                done[current] = true;
                bool result = recurse(k, ans, current, done, n);        
                
                // If the recursion result says we considered all the passwords successfully, then we are done. 
                // Essentially, the way in which we process passwords and choose digits makes this condition sufficient.
                // Else, unmark the current password and try other options / paths in the graph.
                if (result != true) {
                    done[current] = false; 
                    ans.pop_back();
                } else {
                    return true;
                }   
            }
        }
        
        return false;
    }
    
    string crackSafe(int n, int k) {
        
        // Start with the first passord with all `k-1`s.
        string ans = string(n, to_string(k - 1)[0]) ;
        
        // Current string to modify.
        string current = string(n, to_string(k - 1)[0]) ;
        
        // Dictionary storing what all passwords have been considered on a path. Needed so as not to go into cycles.
        unordered_map<string, bool> done;
        done[ans] = true;
        recurse(k, ans, current, done, n);
        return ans;    
    }
};
