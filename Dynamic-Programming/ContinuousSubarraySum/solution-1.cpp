class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        
        int n=nums.size();
        for(int i=0;i<n-1;++i){
            for(int j=i+1;j<n;++j){
                int summation = 0;
                for(auto it=nums.begin()+i;it!=nums.begin()+j+1;++it){
                    summation+=*it;
                }
                    
                if(k==0){
                    if(summation==0){
                        return true;
                    }
                }else if(summation%k==0){
                    return true;
                }
            }
        }
        
        return false;
    }
};