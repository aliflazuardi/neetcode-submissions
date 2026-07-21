class MinStack {
private:
    vector<int> min;
    vector<int> stack;

public:
    MinStack() {
    }
    
    void push(int val) {
        if (min.size() == 0) {
            min.push_back(val);
        } else {
            int minVal = min[min.size()-1];
            if (val < minVal) {
                min.push_back(val);       
            } else {
                min.push_back(minVal);
            }
        }
        stack.push_back(val);
    }
    
    void pop() {
        stack.pop_back();
        min.pop_back();
    }
    
    int top() {
        int last_index = stack.size() - 1;
        return stack[last_index];
    }
    
    int getMin() {
        return min[min.size() -1 ];
    }
};
