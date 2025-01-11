class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans;
        for(auto i=0;i<=n;i++){
            int cnt=0;
            int t=i;
            while(t != 0){
                if(t&1)cnt+=1;
                t= t>>1;
            }
            ans.push_back(cnt);
        }
        return ans;
    }
};