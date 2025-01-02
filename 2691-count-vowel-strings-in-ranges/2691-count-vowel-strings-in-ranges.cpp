class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& q) {
        vector<int> ans;
        string vw = "aeiou";
        vector<int> prefix;
        for (string& w : words) {
            if (vw.find(w.front()) != string::npos && vw.find(w.back()) != string::npos) {
                prefix.push_back(1);
            } else {
                prefix.push_back(0);
            }
        }
        
        vector<int> ac(prefix.size());
        partial_sum(prefix.begin(), prefix.end(), ac.begin());
        for (auto& query : q) {
            int x = query[0], y = query[1];
            if (x == 0) {
                ans.push_back(ac[y]);
            } else {
                ans.push_back(ac[y] - ac[x - 1]);
            }
        }
        
        return ans;
    }
};
