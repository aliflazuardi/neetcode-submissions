class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int l = 1;
        int r = INT_MAX;
        int k = 0;

        while (l <= r) {
            int m = l + ((r-l)/2);

            if (isValid(piles, h, m)) {
                r = m - 1;
                k = m;
            } else {
                l = m + 1;
            }
        }

        return k;
    }

    bool isValid(vector<int> piles, int h, int k) {
        int cnt = 0;

        for (const int& pile : piles) {
            cnt = cnt + pile/k;
            if (pile % k != 0) {
                cnt++;
            }
        }

        return cnt <= h;
    }
};
