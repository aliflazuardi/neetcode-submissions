class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;

        for(int i = 0; i < nums.size(); i++) {
            int target_pair = target - nums[i];
            if (map.find(target_pair) != map.end()) {
                return {map[target_pair], i};
            }
            map.insert({nums[i], i});
        }
        return {};
    }
};
