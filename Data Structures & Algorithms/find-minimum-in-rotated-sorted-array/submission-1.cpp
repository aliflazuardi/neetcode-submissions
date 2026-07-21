class Solution {
public:
    int findMin(vector<int> &nums) {
        int l = 0;
        int r = nums.size() - 1;
        int ans = nums[0];

        while (l <= r) {
            if (nums[l] < nums[r]) {
                return min(ans, nums[l]);
            }
            int m = (r - l)/2 + l;

            ans = min(ans, nums[m]);
            if(nums[m] >= nums[l]) {
                l = m + 1;
            } else {
                r = m - 1;
            }

        }

        return ans;
    }
};
