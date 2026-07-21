class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        int n = position.size();
        vector<pair<double, double>> cars(n);
        for (int i = 0; i < n; i++) {
            cars[i] = {position[i], speed[i]};
        }
        sort(cars.begin(), cars.end(), [](const pair<double, double> &a, const pair<double, double> &b) {
            return a.first > b.first;
        });
        
        stack<double> carStack;
        carStack.push((target - cars[0].first) / cars[0].second);
        for (int i = 1; i < n; i++) {
            double timeToReach = (target - cars[i].first) / cars[i].second;
            cout<<timeToReach<<" "<<carStack.top()<<endl;
            if (timeToReach > carStack.top()) {
                carStack.push(timeToReach);
            }
        }

        return carStack.size();
    }
};
