#include <vector>
#include <numeric>
#include <functional>
class Solution {
public:
    int waysToSplitArray(vector<int>& nums) {
        int ans = 0;
        int n = nums.size();
        vector<long long> ps(n);
        
        ps[0] = nums[0];
        for (int i = 1; i < n; ++i) {
            ps[i] = ps[i - 1] + nums[i];
        }
        
        long long total_sum = ps.back();
        
        for (int i = 0; i < n - 1; ++i) {
            if (ps[i] >= total_sum - ps[i]) {
                ans++;
            }
        }
        
        return ans;
    }
};