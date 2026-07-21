class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;

        for (int num : nums) {
            count[num] = count[num] + 1;
        }

        // initialize array size n to iterate frequency k times
        // this makes O(n) complexity possible
        vector<vector<int>> freq(nums.size() + 1);

        // set count as key and num as value
        for (const auto &c : count) {
            freq[c.second].push_back(c.first);
        }

        vector<int> ans;
        
        // iterate from back of freq array
        for (int i = freq.size() - 1; i > 0; --i) {
            for (int f : freq[i]) {
                ans.push_back(f);
                if (ans.size() == k) {
                    return ans;
                }
            }
        }

        return ans;
    }
};
