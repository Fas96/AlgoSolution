class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        vector<int> answer(nums.size());
        int evenIndex = 0;   
        int oddIndex = 1;    
        for (int n : nums) {
            if (n % 2 == 0) { 
                answer[evenIndex] = n;
                evenIndex += 2;
            } else { 
                answer[oddIndex] = n;
                oddIndex += 2;
            }
        }

        return answer;
    }
};