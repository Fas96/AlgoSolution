class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char, vector<int>> fq;
        int n = s.size();

        for (int i = 0; i < n; i++) {
            fq[s[i]].push_back(i);
        }

        int count = 0;
        for (auto& [char_key, indices] : fq) {
            if (!indices.empty()) {
                int left = *min_element(indices.begin(), indices.end());
                int right = *max_element(indices.begin(), indices.end());
                
                // Ensure valid range before creating unordered_set
                if (left + 1 < right) {
                    unordered_set<char> unique_chars(s.begin() + left + 1, s.begin() + right);
                    count += unique_chars.size();
                }
            }
        }
        return count;
    }
};