class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> num;
        int num1, num2;

        for (const string& token : tokens) {
            if (token == "+") {
                num1 = num.top();
                num.pop();
                num2 = num.top();
                num.pop();
                num.push(num1+num2);
            } else if (token == "-") {
                num1 = num.top();
                num.pop();
                num2 = num.top();
                num.pop();
                num.push(num2-num1);
            } else if (token == "*") {
                num1 = num.top();
                num.pop();
                num2 = num.top();
                num.pop();
                num.push(num1*num2);
            } else if (token == "/") {
                num1 = num.top();
                num.pop();
                num2 = num.top();
                num.pop();
                num.push(static_cast<int>(static_cast<double>(num2)/ num1));
            } else {
                num.push(stoi(token));
            }
        }

        return num.top();
    }
};
