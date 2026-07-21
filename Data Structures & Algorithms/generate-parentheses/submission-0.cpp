class Solution {
private:
    vector<string> ans;

    void backtrack(int n, int openCount, int closedCount, string state) {
        if (openCount == n && openCount == closedCount) {
            this->ans.push_back(state);
            return;
        }        

        // add open parentheses
        if (openCount < n) {
            backtrack(n, openCount + 1, closedCount, state + "(");
        }

        // add close parentheses
        if (closedCount < openCount) {
            backtrack(n, openCount, closedCount + 1, state + ")");
        }
    }
public:
    vector<string> generateParenthesis(int n) {
        backtrack(n, 0, 0, "");
        return this->ans;
    }
};
