class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
          int ans = 0;
        std::unordered_map<std::string, int> prefixSuffixCount;
        
        for (const auto& word : words) {
            int n = word.size();
            for (int i = 0, j = n - 1; i < n; ++i, --j) {
                if (word.substr(0, i + 1) == word.substr(j, i + 1)) {
                    ans += prefixSuffixCount[word.substr(0, i + 1)];
                }
            }
            prefixSuffixCount[word]++;
        }
        return ans;
    }
};