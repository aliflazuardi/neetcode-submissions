class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;

        int hl = 0;
        int hr = 0;
        int maxWater = 0;

        while (l < r) {
            hl = heights[l];
            hr = heights[r];

            int water = (r - l) * min(hl, hr);
            maxWater = max(maxWater, water);

            if (heights[l] <= heights[r]) {
                l++;
            } else {
                r--;
            }
        }

        return maxWater;
    }
};
