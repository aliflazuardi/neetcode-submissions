class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> numSet(nums.begin(), nums.end());
        int seqLen = 0;

        for (int n : numSet) {
            if (numSet.find(n - 1) == numSet.end()) {
                int len = 1;
                while (numSet.find(n + len) != numSet.end()) {
                    len++;
                }
                seqLen = max(seqLen, len);
            }
        }
        return seqLen;
    }
};
