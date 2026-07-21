class Solution {
public:
    bool isValid(string s) {
       stack<char> brackets;

       for(int i = 0; i < s.length(); i++) {
        if (brackets.empty()) {
            brackets.push(s[i]);
            continue;
        }

        char top = brackets.top();
        switch (top) {
            case '{':
                if (s[i] == '}') {
                    brackets.pop();
                } else {
                    brackets.push(s[i]);
                }
                break;
            case '[':
                if (s[i] == ']') {
                    brackets.pop();
                } else {
                    brackets.push(s[i]);
                }
                break;
            case '(':
                if (s[i] == ')') {
                    brackets.pop();
                } else {
                    brackets.push(s[i]);
                }
                break;
        }
       }

       return brackets.empty();
    }
};
