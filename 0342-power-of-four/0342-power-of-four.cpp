class Solution {
public:
    bool isPowerOfFour(int n) {
        if(n<=0)
            return false; 
    return  n == pow(4, round(log(n) / log(4)));
    }
};