class Solution {
public:
    int countPrefixSuffixPairs(vector<string>& words) {
         int n = words.size();
        int ans = 0;

        auto isPrefixAndSuffix = [](const std::string& a, const std::string& b) -> bool {
            return b.compare(0, a.size(), a) == 0 && b.compare(b.size() - a.size(), a.size(), a) == 0;
        };

        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (isPrefixAndSuffix(words[i], words[j])) {
                    ans++;
                }
            }
        }
        return ans;
    }
};