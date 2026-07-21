class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int zeroCnt = 0;
        for (const int& num : nums) {
            if (num == 0) {
                zeroCnt++;
                continue;
            }
            product = product * num;
        }
        
        if (zeroCnt >= 2) {
            for (int& num : nums) {
                num = 0;
            }
        } else if (zeroCnt == 1) {
            for (int& num : nums) {
                if (num == 0) {
                    num = product;
                } else {
                    num = 0;
                }
            }
        } else {
            for (int& num : nums) {
                num = product / num;
            }
        }

        return nums;
    }
};
