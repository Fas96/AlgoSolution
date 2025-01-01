class Solution {
public:
    int maxScore(std::string s) {
        int max_score = 0;
        for (int i = 1; i < s.length(); ++i) {
            int left_count = std::count(s.begin(), s.begin() + i, '0');
            int right_count = std::count(s.begin() + i, s.end(), '1');
            max_score = std::max(max_score, left_count + right_count);
        }
        return max_score;
    }
};
