class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<char> stack;
        string result;
        if (k == num.size()) {
            return "0";
        }
        int rem = num.size() - k;
        for (char digit :num) {
            while (k >0 && !stack.empty() && stack.back()>digit) {
                stack.pop_back();
                k--;
            }
            stack.push_back(digit);
        }

 
        for (int i = 0; i < rem; ++i) {
            result += stack[i];
        }
        while (result.size() > 0 && result[0] == '0') {
            result.erase(0, 1);
        }
        if (result.empty()) {
            result = "0";
        }
        
        return result;
    }
};