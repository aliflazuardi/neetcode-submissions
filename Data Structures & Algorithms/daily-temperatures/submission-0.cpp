class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> ans(temperatures.size(), 0);
        stack<pair<int, int>> stack;

        for(int i = 0; i < temperatures.size(); i++) {
            int temp = temperatures[i];
            while (!stack.empty() && temp > stack.top().second) {
                pair<int, int> pair = stack.top();
                stack.pop();
                ans[pair.first] = i - pair.first;
            }

            stack.push({i, temp});
        } 

        return ans;
    }
};
